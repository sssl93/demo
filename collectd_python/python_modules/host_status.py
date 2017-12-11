#!/usr/bin/env python
# coding:utf-8
import collectd
from python_modules.common.utils import query
import time


class HostStatusPlugin(object):
    def __init__(self):
        self.config = None
        self.plugin = self.metric_type = 'host_status'
        self.plugin_instance = None

    def read(self):
        query_string = ''' select last(value),host from "collectd"."default"."cpu_value" 
                                  where time > now() - 10d group by host '''
        response = query(self.config['influxDB'], query_string)
        if response['result']:
            for item in response['data']:
                host = item[0]['host']
                active_time = time.strptime(item[0]['time'][0:26], '%Y-%m-%dT%H:%M:%S.%f')
                value = 1  # when host status is up store as figure 1 , status is down sotre as figure 0
                if time.mktime(active_time) < time.mktime(time.gmtime()) - 300:
                    value = 0
                self.dispatch(self.plugin, self.plugin_instance, self.metric_type, 'system.host_status', value, host)
                collectd.info('------%s, %s' % (host, value))

    def dispatch(self, plugin, plugin_instance, metric_type, type_instance, value, host=None):
        """Looks for the given stat in stats, and dispatches it"""
        collectd.debug("dispatching value %s.%s.%s.%s=%s"
                       % (plugin, plugin_instance, metric_type, type_instance, value))

        val = collectd.Values(type=metric_type)
        val.plugin = plugin
        val.type_instance = type_instance
        val.values = [value, ]
        if host:
            val.host = host
        val.dispatch()


Plugin = HostStatusPlugin()


def configuration(conf):
    """Received configuration information"""

    config = {}
    for item in conf.children:
        if len(item.values) == 1:
            config.update({item.key: item.values[0]})
        elif len(item.values) > 1:
            config.update({item.key: item.values})
        else:
            collectd.error('cannot load the configuration !')
    Plugin.config = config


def read():
    Plugin.read()


collectd.register_config(configuration)
# collectd.register_init(init)
collectd.register_read(read)
