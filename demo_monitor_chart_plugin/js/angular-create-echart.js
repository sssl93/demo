/*** Directives and services for responding to MonitorChart in AngularJS
 * @version v1.0.1
 * depends on echarts.js  http://echarts.baidu.com/
 */
(function (window, angular, undefined) {
    'use strict';
    angular.module('createEchart', [])
        .factory('CreateEchartOption', CreateEchartOption)
        .factory('MonitorHttpService', MonitorHttpService)

        .directive('lineChart', function () {
            return {
                restrict: 'A',
                scope: {
                    options: "="
                },
                link: function ($scope, element, attrs) {
                    var options = $scope.options || {'series': []};
                    var xAxis = angular.extend(xAxisTemplate(), options.xAxis);
                    var yAxis = [{
                        type: 'value',
                        boundaryGap: [0, '100%']
                    }];

                    var series = genSeries(options.series);

                    var optionTemplate = {
                        title: options.title,
                        tooltip: {
                            trigger: 'axis',
                            position: function (pt) {
                                return [pt[0], '10%'];
                            }
                        },
                        xAxis: xAxis,
                        yAxis: yAxis,
                        grid: {
                            left: '8%',
                            right: '10%',
                            bottom: '4%',
                            containLabel: true
                        },
                        legend: options.legend,
                        series: series
                    };

                    var myChart = echarts.init(element[0]);
                    myChart.setOption(optionTemplate);

                    $scope.$watch("options", function (newOptions, oldValue) {
                        if (newOptions) {
                            myChart.setOption(setOptionDatas(newOptions));
                        }
                        myChart.resize();
                    });

                    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
                        myChart.resize();
                    });

                    function setOptionDatas(options) {
                        return {
                            xAxis: angular.extend(xAxisTemplate(), options.xAxis),
                            yAxis: options.yAxis,
                            series: genSeries(options.series),
                            legend: options.legend,
                            title: options.title
                        }
                    }

                    function genSeries(configs) {

                        var series = [];

                        configs.forEach(function (config) {
                            series.push(angular.extend(serieTemplate(), config));
                        });

                        return series;
                    }

                    function xAxisTemplate() {
                        return {
                            type: 'category',
                            boundaryGap: false,
                            data: []
                        };
                    }

                    function serieTemplate() {
                        return {
                            name: '',
                            type: 'line',
                            smooth: true,
                            symbol: 'none',
                            sampling: 'average',
                            areaStyle: {normal: {}},
                            lineStyle: {normal: {}},
                            data: []
                        };
                    }
                }
            }
        })
        .directive('twolineChart', function () {
            return {
                restrict: 'A',
                scope: {
                    options: "="
                },
                link: function ($scope, element, attrs) {
                    var options = $scope.options || {'series': []};
                    var xAxis = angular.extend(xAxisTemplate(), options.xAxis);
                    var yAxis = [{
                        type: 'value',
                        boundaryGap: [0, '100%']
                    }, {
                        type: 'value',
                        name: 'iops',
                        boundaryGap: [0, '100%']
                    }];

                    var series = genSeries(options.series);

                    var optionTemplate = {
                        title: options.title,
                        tooltip: {
                            trigger: 'axis',
                            position: function (pt) {
                                return [pt[0], '10%'];
                            }
                        },
                        xAxis: xAxis,
                        yAxis: yAxis,
                        grid: {
                            left: '8%',
                            right: '8%',
                            bottom: '4%',
                            containLabel: true
                        },
                        legend: options.legend,
                        series: series
                    };

                    var myChart = echarts.init(element[0]);
                    myChart.setOption(optionTemplate);

                    $scope.$watch("options", function (newOptions, oldValue) {
                        if (newOptions) {
                            myChart.setOption(setOptionDatas(newOptions));
                        }
                        myChart.resize();
                    });

                    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
                        myChart.resize();
                    });

                    function setOptionDatas(options) {
                        return {
                            xAxis: angular.extend(xAxisTemplate(), options.xAxis),
                            yAxis: options.yAxis,
                            series: genSeries(options.series),
                            legend: options.legend,
                            title: options.title
                        }
                    }

                    function genSeries(configs) {

                        var series = [];

                        configs.forEach(function (config) {
                            series.push(angular.extend(serieTemplate(), config));
                        });

                        return series;
                    }

                    function xAxisTemplate() {
                        return {
                            type: 'category',
                            boundaryGap: false,
                            data: []
                        };
                    }

                    function serieTemplate() {
                        return {
                            name: '',
                            type: 'line',
                            smooth: true,
                            symbol: 'none',
                            sampling: 'average',
                            areaStyle: {normal: {}},
                            data: []
                        };
                    }
                }
            }
        })
        .directive('dashChart', function () {
            return {
                restrict: 'A',
                scope: {
                    options: "="
                },
                link: function ($scope, element, attrs) {
                    var options = $scope.options || {};
                    var option = {
                        tooltip: {
                            trigger: 'item',
                            formatter: "{a}{b}: {c}%"
                        },
                        series: [
                            {
                                type: 'gauge',
                                min: 0,
                                max: 100,
                                splitNumber: 5,
                                radius: '80%',
                                axisLine: {
                                    lineStyle: {
                                        color: [[0.16, '#1BA39C'], [0.82, '#546570'], [1, '#C23531']],
                                        width: 5
                                    }
                                },
                                axisTick: {
                                    length: 3
                                },
                                splitLine: {
                                    length: 8
                                },
                                pointer: {
                                    width: 2
                                },
                                title: {
                                    textStyle: {
                                        fontSize: 12
                                    }
                                },
                                detail: {
                                    textStyle: {
                                        fontSize: 18
                                    },
                                    offsetCenter: [0, '80%'],
                                    formatter: '{value}%'
                                },
                                data: [{value: options.data, name: ''}]
                            }
                        ]
                    };
                    var myChart = echarts.init(element[0]);
                    myChart.setOption(option);

                    $scope.$watch('options', function (newOptions, oldvalue) {
                        if (newOptions) {
                            myChart.setOption({
                                series: [{data: [{value: newOptions.data, name: '使用率'}]}]
                            });
                        }
                    });
                }
            }
        })
        .directive('circleChart', function () {
            return {
                restrict: 'A',
                scope: {
                    options: "="
                },
                link: function ($scope, element, attrs) {
                    var options = $scope.options;
                    var labelTop = {
                        normal: {
                            // color: '#C23531',
                            color: 'green',
                            label: {
                                show: true,
                                position: 'center',
                                formatter: '{d}%',
                                textStyle: {
                                    baseline: 'top'
                                }
                            }
                        }
                    };
                    var labelBottom = {
                        normal: {
                            color: '#bbb',
                            label: {
                                show: false,
                                position: 'center'
                            }
                        }
                    };
                    option = {
                        series: [
                            {
                                type: 'pie',
                                radius: [25, 35],
                                data: [
                                    {name: 'used', value: 0, itemStyle: labelTop},
                                    {name: 'free', value: 100, itemStyle: labelBottom}
                                ]
                            }
                        ]
                    };
                    var myChart = echarts.init(element[0]);
                    myChart.setOption(option);

                    $scope.$watch('options', function (newOptions, oldvalue) {
                        myChart.setOption({
                            series: [{
                                data: [{value: newOptions[0], itemStyle: labelTop}, {value: newOptions[1]}],
                                itemStyle: labelBottom
                            }]
                        });
                    });
                }
            }
        })
        .directive('pieChart', function () {
            return {
                restrict: 'A',
                scope: {
                    options: "="
                },
                link: function ($scope, element, attrs) {
                    var options = $scope.options || {};
                    var option = {
                        tooltip: {
                            // trigger: 'item',
                            formatter: "{b}: {c} ({d}%)"
                        },
                        legend: {
                            orient: 'vertical',
                            x: 'left',
                            data: options.legend
                        },
                        series: [
                            {
                                type: 'pie',
                                selectedMode: 'single',
                                radius: [0, '30%'],
                                data: options.pgSeriesData,
                                labelLine: {
                                    normal: {
                                        show: false
                                    }
                                },
                                label: {
                                    normal: {
                                        show: false
                                    }
                                }
                            },
                            {
                                type: 'pie',
                                radius: ['50%', '65%'],
                                data: options.totalSeriesData
                            }
                        ]
                    };
                    var myChart = echarts.init(element[0]);
                    myChart.setOption(option);

                    $scope.$watch('options', function (newOptions, oldvalue) {
                        if (newOptions) {
                            myChart.setOption({
                                legend: {data: newOptions.legend},
                                series: [{data: newOptions.pgSeriesData}, {data: newOptions.totalSeriesData}]
                            });
                        }
                    });
                }
            }
        });

    function CreateEchartOption() {

        function setMax(max) {
            max = 2 * Math.ceil(max);
            if (max >= 10) {
                var len = max.toString().length;
                var ji = Math.pow(10, len - 1);
                max /= ji;
                max = Math.round(max);
                max = max * ji;
            }
            return max;
        }

        function optionBase(option, items, title, legendKey) {
            var legend, times;
            //legendKey = 'pod_name';
            if (legendKey) {
                legend = items.map(function (x) {
                    return x['datas'][0][legendKey]
                });
            } else {
                legend = angular.copy(option.legend || option.series);
                legend = legend.concat(option.optional_legend || option.optional_meters);
            }
            times = items[0]['datas'].map(function (x) {
                return x['time']
            });
            return {
                title: {text: title},
                legend: {data: legend},
                xAxis: {data: times}
            }
        }

        var lineCreateOptions = function (option, items, title, legendKey) {
            /***
             * @option eg. {
                legend: ['load_1m', 'load_5m', 'load_15m'],
                series: ['load.1m', 'load.5m', 'load.15m'],
                areaStyle: {},
            }
             * @items the monitor data
             * @tit the title of  chart
             * @legendKey you can set the legend from the data
             */
            var newOpt = optionBase(option, items, title, legendKey);
            newOpt.yAxis = [{
                name: items[0]['datas'][0]['unit'],
                type: 'value',
                boundaryGap: [0, '100%']
            }];
            newOpt.series = [];
            var dataList = [];
            for (var i = 0; i < items.length; i++) {
                var ser = {
                    name: newOpt['legend']['data'][i],
                    data: items[i]['datas'].map(function (x) {
                        return x['value']
                    })
                };
                dataList = dataList.concat(ser.data);
                if (option.areaStyle) {
                    ser.areaStyle = option.areaStyle;
                }
                newOpt.series.push(ser);
            }

            dataList = dataList.filter(function (x) {
                return x !== undefined
            });
            newOpt.yAxis[0]['max'] = setMax(Math.max.apply(null, dataList));
            newOpt.yAxis[0]['interval'] = newOpt.yAxis[0]['max'] / 5;
            return newOpt;
        };

        var twolineCreateOptions = function (option, items, title) {
            /***
             the "meters" whose unit is on the left side
             the option must contain "optional_meters" whose unit is on the right side
             *@option eg. {
                legend: ['read.bandwidth', 'write.bandwidth'],
                series: ['cluster.read.bandwidth', 'cluster.write.bandwidth'],
                optional_meters: ['cluster.iops'],
                optional_legend: ['op/s'],
                areaStyle: {},
            }
             *@items the monitor data
             * @title the title of chart
             */
            var leftData = [], rightData = [];
            var allData = {};
            for (var i = 0; i < items.length; i++) {
                var meter = items[i]['datas'][0]['type_instance'];
                allData[meter] = items[i]['datas'].map(function (x) {
                    return x['value']
                });
                if (option.series.indexOf(meter) > -1) {
                    leftData.push(items[i]['datas'])
                } else if (option.optional_meters.indexOf(meter) > -1) {
                    rightData.push(items[i]['datas'])
                }
            }
            var unit = [leftData[0][0]['unit'], rightData[0][0]['unit']];
            var newOpt = optionBase(option, items, title);
            newOpt.series = [];
            var maxArray = [];
            var sdata, mdata, ser;

            function formatSeries(meters, legend, yAxisIndex) {
                for (var i = 0; i < meters.length; i++) {
                    sdata = allData[meters[i]];
                    mdata = sdata.filter(function (element) {
                        return element !== undefined;
                    });
                    maxArray.push(Math.max.apply(null, mdata));
                    ser = {
                        'name': legend[i],
                        'data': sdata,
                        'yAxisIndex': yAxisIndex
                    };
                    if (option.areaStyle) {
                        ser.areaStyle = option.areaStyle;
                    }
                    newOpt.series.push(ser);
                }
            }

            formatSeries(option.series, option.legend || option.series, 0); //left line
            formatSeries(option.optional_meters, option.optional_legend || option.optional_meters, 1);//right line

            var max1 = setMax(Math.max.apply(null, maxArray.slice(0, 2)));
            var max2 = setMax(Math.max.apply(null, maxArray.slice(2, maxArray.length)));

            newOpt.yAxis = [{
                name: unit[0],
                type: 'value',
                boundaryGap: [0, '100%'],
                min: 0,
                max: max1,
                interval: max1 / 5
            }, {
                name: unit[1],
                type: 'value',
                boundaryGap: [0, '100%'],
                min: 0,
                max: max2,
                interval: max2 / 5
            }];
            return newOpt;
        };

        var dashChartCreateOptions = function (option, items, title) {
            /***
             * @option eg. {
                series: ['cluster.osd.used', 'cluster.osd.free' , 'cluster.osd.total' ],
            }
             */
            var newOpt = {'unit': items[0][option.series[0] + '.unit']};
            for (var key in items[0]) {
                if (key.endsWith('.used')) {
                    newOpt['used'] = items[0][key].toFixed(2);
                } else if (key.endsWith('.total')) {
                    newOpt['total'] = items[0][key].toFixed(2);
                } else if (key.endsWith('.free')) {
                    newOpt['free'] = items[0][key].toFixed(2)
                }
            }
            newOpt['data'] = (newOpt['used'] / newOpt['total'] * 100).toFixed(1);
            return newOpt
        };

        var pieChartCreateOptions = function (option, items, title) {
            /***
             * @option eg. {
                    legend: ['total'],
                    series: ['cluster.pg.nums'],
                    optional_meters: ['cluster.pg.active+clean'],
                    optional_legend: ['active+clean'],
                    areaStyle: {}
                }
             */
            var newOpt = {};
            var i, key;
            var totalLegend = option['legend'] || option['series']
            var optionalLegend = option['optional_legend'] || option['optional_meters'];
            newOpt['legend'] = totalLegend.concat(optionalLegend);
            newOpt['totalSeriesData'] = [];
            newOpt['pgSeriesData'] = [];

            for (i in option.series) {
                key = option.series[i];
                newOpt['totalSeriesData'].push({
                    value: items[0][key],
                    name: totalLegend[i]
                });
            }
            for (i in option.optional_meters) {
                key = option.optional_meters[i];
                if (items[0][key]) {
                    newOpt['pgSeriesData'].push({
                        value: items[0][key],
                        name: optionalLegend[i]
                    });
                }

            }
            return newOpt

        };

        return {
            'lineCreateOptions': lineCreateOptions,
            'twolineCreateOptions': twolineCreateOptions,
            'dashChartCreateOptions': dashChartCreateOptions,
            'pieChartCreateOptions': pieChartCreateOptions
        };
    }

    function MonitorHttpService($http, $q) {
        return {
            'get': function (apiUrl) {
                var defer = $q.defer();
                $http({
                    method: 'GET',
                    url: apiUrl
                }).success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(data);
                });
                return defer.promise;
            },
            'post': function (apiUrl, postData) {
                var defer = $q.defer();
                $http({
                    method: 'POST',
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    url: apiUrl,
                    data: $.param(postData)
                }).success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(data);
                });
                return defer.promise;
            }
        };
    }

})(window, window.angular);