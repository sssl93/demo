#!/usr/bin/env python
import urllib2, re
import json


def derivative(current, previous, time_difference, unit=1):
    """
    The derivative is computed on a single field and behaves similarly to the InfluxQL derivative function
    unit: default 1 second
    """
    return float((current - previous)) / (time_difference / unit)


def format_series(result):
    all_data = []
    for item in result:
        for series in item['series']:
            all_data.append(map(lambda x: dict(zip(series['columns'], x)), series['values']))
    return all_data


def query(address, query_string):
    url = 'http://%s/query?pretty=true' % (address,)
    data_string = 'q=%s' % (query_string,)
    req = urllib2.Request(url, data=data_string)
    response = urllib2.urlopen(req)
    data = format_series(json.loads(response.read())['results'])
    result = {'result': True, 'msg': response.msg, 'data': data}
    if response.code > 400:
        result['result'] = False
    return result


def insert(address, db, measurement, data, rp=None, username=None, password=None, precision=None):
    """
    :param address: influxDB ip:port
    :param db: sets the target database for the write
    :param measurement: target measurement to insert
    :param data: dict which contain the tag and fields
    :param rp: sets the target retention policy for the write. If not present the default retention policy is used
    :param username: if authentication is enabled, you must offer the username
    :param password: if authentication is enabled, you must offer the password
    :param precision: sets the precision of the supplied Unix time values. [n,u,ms,s,m,h] default nanoseconds[n]
    :return: dict
    """

    url = 'http://%s/write?db=%s?rp=%s?u=%s?p=%s?precision=%s' % (address, db, rp, username, password, precision)
    empty_params = re.compile(r'\?\w+=None').findall(url)
    for i in empty_params:
        url = url.replace(i, '')
    value = data.pop('value') if data.has_key('value') else ''
    unit = data.pop('unit') if data.has_key('unit') else ''
    timestamp = data.pop('time') if data.has_key('time') else ''
    key_value = []
    map(lambda x: key_value.append('='.join(x)), data.items())
    tag_string = ','.join(key_value)  # insert the tag && value into influx
    fields_string = 'value=%s,unit="%s" %s' % (value, unit, timestamp)  # insert the fields && value into influx
    if tag_string:
        data_string = '%s,%s %s' % (measurement, tag_string, fields_string)
    else:
        data_string = '%s %s' % (measurement, fields_string)
    req = urllib2.Request(url, data=data_string)
    response = urllib2.urlopen(req)
    result = {'result': True, 'msg': response.msg}
    if response.code > 400:
        result['result'] = False
    return result


def create_database(address, db_name):
    """
    :param address:  influxDB ip:port
    :param db_name:  new DB name
    :return: True or False
    """
    url = "http://%s/query" % (address)
    data_string = 'q=CREATE DATABASE %s' % (db_name,)
    req = urllib2.Request(url, data=data_string)
    response = urllib2.urlopen(req)
    result = {'result': True, 'msg': response.msg}
    if response.code > 400:
        result['result'] = False
    return result


def drop_database(address, db_name):
    """
    :param address:  influxDB ip:port
    :param db_name:  DB name
    :return:  True or False
    """
    url = "http://%s/query" % (address)
    data_string = 'q=DROP DATABASE %s' % (db_name,)
    req = urllib2.Request(url, data=data_string)
    response = urllib2.urlopen(req)
    result = {'result': True, 'msg': response.msg}
    if response.code > 400:
        result['result'] = False
    return result


if __name__ == '__main__':
    import time

    # insert('192.168.30.10:8086', 'test', 'disk', {'type': 'disk', 'type_ins': 'MEM', 'value': 10.3, 'unit': 'GB'})
    # create_database('192.168.30.10:8086', 'test')
    # insert('192.168.30.10:8086', 'test', 'system_test', {'time': int(time.time() * 10 ** 9), 'value': '1', 'unit': '%'})
    x = query('192.168.0.121:8086', 'select last(value),host from "collectd"."default"."cpu_value" where time > now() - 10d group by host ')
    pass
