# collectd python plugins demo

* Preface
```
The porject is monitor physics host status which is working on the collectd.
When resived the cpu_value from the host , the host status is active (influxDB store figure 1)
otherwise host status is down (influxDB store figure 0)
```

* Before the start
```
1, please install collectd && influxDB
2, enabled the cpu plugins in the collectd
```
* Usage
```bash
# cp ./config/host_status.conf /etc/collectd/collectd.conf.d/
# mkdir -p /usr/lib/collectd/plugins/
# cp -r ./python_modules /usr/lib/collectd/plugins/
# service collectd restart
```