angular.module('myApp', ['createEchart'])

    .controller('myCtrl', function ($scope, CreateEchartOption, MonitorHttpService) {
        var dashOptions = {
            series: ['cluster.osd.used', 'cluster.osd.free', 'cluster.osd.total'],
        };
        var twolineOptions = {
            legend: ['read.bandwidth', 'write.bandwidth'],
            series: ['cluster.read.bandwidth', 'cluster.write.bandwidth'],
            optional_meters: ['cluster.iops'],
            optional_legend: ['op/s'],
            areaStyle: {},
        };
        var lineOptions = {
            legend: ['load_1m', 'load_5m', 'load_15m'],
            series: ['load.1m', 'load.5m', 'load.15m'],
            areaStyle: {},
        };
        var pieOptions = {
            legend: ['total'],
            series: ['cluster.pg.nums'],
            optional_meters: ['cluster.pg.active+clean'],
            optional_legend: ['active+clean'],
            areaStyle: {}
        }


        // create dash chart
        MonitorHttpService.post('http://localhost:8001/api/monitor-alarm/monitor/cluster-osd-info/', {
            "meters": ["cluster.total", "cluster.used", "cluster.free"],
            "tag": "cluster",
            "monitor_type": "ceph",
            "func": "last",
            "auto_unit": true
        }).then(function (data) {
            $scope.dashChartData = CreateEchartOption.dashChartCreateOptions(dashOptions, data)
        });

        // create pie chart
        MonitorHttpService.post('http://localhost:8001/api/monitor-alarm/monitor/cluster-pg-nums', {
            "meters": ["cluster.pg.active+clean", "cluster.pg.nums"],
            "tag": "cluster",
            "monitor_type": "ceph",
            "func": "last",
            "auto_unit": false
        }).then(function (data) {
            $scope.pieChartData = CreateEchartOption.pieChartCreateOptions(pieOptions, data)
        })

        //create twoline chart
        MonitorHttpService.post('http://localhost:8001/api/monitor-alarm/monitor/cluster-io/', {
            "meters": ["cluster.read.bandwidth", "cluster.write.bandwidth", "cluster.iops"],
            "tag": "cluster",
            "monitor_type": "ceph",
            "func": "mean",
            "period": 1,
            "offset": 0,
            "auto_unit": true
        }).then(function (data) {
            $scope.twoLineData = CreateEchartOption.twolineCreateOptions(twolineOptions, data, '集群IO')
        });

        //create line chart
        MonitorHttpService.post('http://localhost:8001/api/monitor-alarm/monitor/node-1-summary/', {
            "meters": ["load.1m", "load.5m", "load.15m"],
            "monitor_type": "system",
            "func": "mean",
            "hostname": "node-1",
            "period": 1,
            "offset": 0
        }).then(function (data) {
            $scope.lineData = CreateEchartOption.lineCreateOptions(lineOptions, data, "Cluster 负载")
        });

        //get trigger history
        MonitorHttpService.get('http://localhost:8001/api/monitor-alarm/alarm/system/alarm1/trigger-history/').then(
            function (data) {
                console.log(data)
            })
    });
