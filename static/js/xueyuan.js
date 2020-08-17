var companydata;
var school='zzuli';
var year='2019';
var filename='allData';
function refreshPage() {

    school = $("#school").val();
    year = $("#year").val();
    filename = 'allData';
    if (filename) {
        echarts_3(filename);
        //意向薪资分析
        echarts_4(filename);
    }
}


$(function () {
    tips();
    echarts_3(filename);
    //意向薪资分析
    echarts_4(filename);
})


function tips() {
    var tips = '';
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/tips/tips.json", function (data3) {
        tipsData = data3;
    });
    tips = tipsData[0].value;
    $("#tips").html(tips);
}

function echarts_1(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echarts_1'));

    var data = [
        {value: 12, name: '大数据开发工程师'},
        {value: 13, name: '咨询研究员'},
        {value: 70, name: '考公务员'},
        {value: 52, name: '硬件开发工程师'},
        {value: 35, name: 'WEB开发工程师'},
        {value: 35, name: 'Python工程师'}
    ];

    var echarts_1Data;
    var yearSchool = filename;
    filename=filename+'hangye.json'
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        echarts_1Data = data3;
    });

    option = {
        backgroundColor: 'rgba(0,0,0,0)',
        tooltip: {
            trigger: 'item',
            formatter: "{b}: <br/>{c} ({d}%)"
        },
        color: ['#af89d6', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847'],
        legend: { //图例组件，颜色和名字
            x: '70%',
            y: 'center',
            orient: 'vertical',
            itemGap: 12, //图例每项之间的间隔
            itemWidth: 10,
            itemHeight: 10,
            icon: 'rect',
            data: ['行业一', '行业二', '行业三', '行业四', '行业五', '行业六'],
            textStyle: {
                color: [],
                fontStyle: 'normal',
                fontFamily: '微软雅黑',
                fontSize: 12,
            }
        },
        series: [{
            name: '行业占比',
            type: 'pie',
            clockwise: false, //饼图的扇区是否是顺时针排布
            minAngle: 20, //最小的扇区角度（0 ~ 360）
            center: ['35%', '50%'], //饼图的中心（圆心）坐标
            radius: [50, 75], //饼图的半径
            avoidLabelOverlap: true, ////是否启用防止标签重叠
            itemStyle: { //图形样式
                normal: {
                    borderColor: '#1e2239',
                    borderWidth: 2,
                },
            },
            label: { //标签的位置
                normal: {
                    show: true,
                    position: 'inside', //标签的位置
                    formatter: "{d}%",
                    textStyle: {
                        color: '#fff',
                    }
                },
                emphasis: {
                    show: true,
                    textStyle: {
                        fontWeight: 'bold'
                    }
                }
            },
            data: echarts_1Data
        }, {
            name: '',
            type: 'pie',
            clockwise: false,
            silent: true,
            minAngle: 20, //最小的扇区角度（0 ~ 360）
            center: ['35%', '50%'], //饼图的中心（圆心）坐标
            radius: [0, 40], //饼图的半径
            itemStyle: { //图形样式
                normal: {
                    borderColor: '#1e2239',
                    borderWidth: 1.5,
                    opacity: 0.21,
                }
            },
            label: { //标签的位置
                normal: {
                    show: false,
                }
            },
            data: echarts_1Data
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function echarts_2(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echarts_2'));
    var echarts_2data;
    var yearSchool = filename;
    filename=filename+'xinzi.json'
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        echarts_2data = data3;
    });
    /*$.ajaxSettings.async = false;
    $.getJSON("../static/data/2019zzulixinzi.json", function (data3) {
        echarts_2data = data3;
    });*/
    option = {
        backgroundColor: 'rgba(0,0,0,0)',
        tooltip: {
            trigger: 'item',
            // formatter: "{b}  <br/>{c}人次"
            formatter: function (params) {
                return params.name + "<br/>" + '占比: ' + (params.value * 100).toFixed(2) + '%';
            }
        },
        legend: {
            x: 'center',
            y: '2%',
            data: ['软件开发', '人工智能', '咨询研究', '硬件开发', '金融科技'],
            icon: 'circle',
            textStyle: {
                color: '#fff',
            }
        },
        calculable: true,
        series: [{
            name: '职业方向',
            type: 'pie',
            //起始角度，支持范围[0, 360]
            startAngle: 0,
            //饼图的半径，数组的第一项是内半径，第二项是外半径
            radius: [20, 60],
            //支持设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
            center: ['50%', '50%'],
            //是否展示成南丁格尔图，通过半径区分数据大小。可选择两种模式：
            // 'radius' 面积展现数据的百分比，半径展现数据的大小。
            //  'area' 所有扇区面积相同，仅通过半径展现数据大小
            roseType: 'area',
            //是否启用防止标签重叠策略，默认开启，圆环图这个例子中需要强制所有标签放在中心位置，可以将该值设为 false。
            avoidLabelOverlap: false,
            label: {
                normal: {
                    show: true,
                    formatter: '{b}'
                },
                emphasis: {
                    show: true
                }
            },
            labelLine: {
                normal: {
                    show: true,
                    length2: 1,
                },
                emphasis: {
                    show: true
                }
            },
            data: echarts_2data
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function map(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('map'));

    var nameColor = " rgb(55, 75, 113)"
    var name_fontFamily = '宋体'
    var name_fontSize = 35
    var mapName = 'china'
    var data = []
    var geoCoordMap = {};
    var toolTipData = [];

    /*获取地图数据*/
    myChart.showLoading();
    var mapFeatures = echarts.getMap(mapName).geoJson.features;
    myChart.hideLoading();

    var mapData;
    var yearSchool = filename;
    filename=filename+'city.json'
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        mapData = data3;
    });
    /*$.ajaxSettings.async = false;
    $.getJSON("../static/data/2019fromto.json", function (data3) {
        mapData = data3;
    });*/

    mapFeatures.forEach(function (v) {
        // 地区名称
        var name = v.properties.name;
        // 地区经纬度
        geoCoordMap[name] = v.properties.cp;
        var to, tonum;
        var from, fromnum;
        for (var i = 0; i < mapData.length; i++) {
            if (name == mapData[i].province) {
                to = mapData[i].to;
                tonum = mapData[i].tonum;
                from = mapData[i].from;
                fromnum = mapData[i].fromnum;
                break;
            }
        }
        ;
        // mapData.forEach(function (v) {
        //     if (name == v.province) {
        //         to = v.to;
        //         tonum = v.tonum;
        //         from = v.from;
        //         fromnum = v.fromnum;
        //     }
        // });
        data.push({
            name: name,
            value: Math.round(Math.random() * 100 + 10)
        });
        toolTipData.push({
            name: name,
            value: [
                {
                    name: to,
                    value: tonum
                },
                {
                    name: from,
                    value: fromnum
                }
            ]
        })
    });

    var max = 480,
        min = 9; // todo
    var maxSize4Pin = 50,
        minSize4Pin = 20;

    var convertData = function (data) {
        var res = [];
        for (var i = 0; i < data.length; i++) {
            var geoCoord = geoCoordMap[data[i].name];
            if (geoCoord) {
                res.push({
                    name: data[i].name,
                    value: geoCoord.concat(data[i].value),
                });
            }
        }
        return res;
    };

    option = {


        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                if (typeof (params.value)[2] == "undefined") {
                    var toolTiphtml = ''
                    for (var i = 0; i < toolTipData.length; i++) {
                        if (params.name == toolTipData[i].name) {
                            toolTiphtml += toolTipData[i].name + ':<br>'
                            for (var j = 0; j < toolTipData[i].value.length; j++) {
                                toolTiphtml += toolTipData[i].value[j].name + ':' + toolTipData[i].value[j].value + "<br>"
                            }
                        }
                    }
                    console.log(toolTiphtml)
                    // console.log(convertData(data))
                    return toolTiphtml;
                } else {
                    var toolTiphtml = ''
                    for (var i = 0; i < toolTipData.length; i++) {
                        if (params.name == toolTipData[i].name) {
                            toolTiphtml += toolTipData[i].name + ':<br>'
                            for (var j = 0; j < toolTipData[i].value.length; j++) {
                                toolTiphtml += toolTipData[i].value[j].name + ':' + toolTipData[i].value[j].value + "<br>"
                            }
                        }
                    }
                    console.log(toolTiphtml)
                    // console.log(convertData(data))
                    return toolTiphtml;
                }
            }
        },
        legend: {
            orient: 'vertical',
            y: 'bottom',
            x: 'right',
            data: ['credit_pm2.5'],
            textStyle: {
                color: '#fff'
            }
        },
        visualMap: {
            show: false,
            min: 0,
            max: 1000,
            left: 'left',
            top: 'bottom',
            text: ['高', '低'], // 文本，默认为数值文本
            calculable: true,
            seriesIndex: [1],
            inRange: {
                // color: ['#3B5077', '#031525'] // 蓝黑
                // color: ['#ffc0cb', '#800080'] // 红紫
                // color: ['#3C3B3F', '#605C3C'] // 黑绿
                //  color: ['#0f0c29', '#302b63', '#24243e'] // 黑紫黑
                // color: ['#23074d', '#cc5333'] // 紫红
                //   color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#1488CC', '#2B32B2'] // 浅蓝
                // color: ['#00467F', '#A5CC82','#ffc0cb'] // 蓝绿红
                // color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#00467F', '#A5CC82'] // 蓝绿
                color: ['#22e5e8', '#5688f9', '#482ee8'], // 蓝绿
                symbolSize: [10, 1000]

            }
        },
        /*工具按钮组*/
        toolbox: {
            show: false,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {

                dataView: {
                    readOnly: false
                },
                restore: {},
                saveAsImage: {}
            }
        },
        geo: {
            show: true,
            map: mapName,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            roam: true,
            itemStyle: {
                normal: {
                    areaColor: '#031525',
                    borderColor: '#097bba'
                },
                emphasis: {
                    areaColor: '#2B91B7'
                }
            }
        },
        series: [{
            name: '散点',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(data),
            symbolSize: function (val) {
                return val[2] / 10;
            },
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgba(255,255,0,0.8)'
                }
            }
        },
            {
                type: 'map',
                map: mapName,
                geoIndex: 0,
                aspectScale: 0.75, //长宽比
                showLegendSymbol: false, // 存在legend时显示
                label: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: false,
                        textStyle: {
                            color: '#fff'
                        }
                    }
                },
                roam: true,
                itemStyle: {
                    normal: {
                        areaColor: '#031525',
                        borderColor: '#3B5077',
                    },
                    emphasis: {
                        areaColor: '#2B91B7'
                    }
                },
                animation: false,
                data: data
            },
            {
                name: '点',
                type: 'scatter',
                coordinateSystem: 'geo',
                symbol: 'pin', //气泡
                symbolSize: function (val) {
                    var a = (maxSize4Pin - minSize4Pin) / (max - min);
                    var b = minSize4Pin - a * min;
                    b = maxSize4Pin - a * max;
                    return a * val[2] + b;
                },
                label: {

                    normal: {
                        show: false,
                        formatter: function (params) {
                            return params.data.value[2]
                        },
                        textStyle: {
                            color: '#fff',
                            fontSize: 9,
                        }
                    }
                },
                itemStyle: {

                    normal: {
                        color: 'rgba(255,255,0,0)', //标志颜色
                    }
                },
                zlevel: 6,
                data: convertData(data),
            },
            {
                name: 'Top 5',
                type: 'effectScatter',
                coordinateSystem: 'geo',
                data: convertData(data.sort(function (a, b) {
                    return b.value - a.value;
                }).slice(0, 5)),
                symbolSize: function (val) {
                    return val[2] / 10;
                },
                showEffectOn: 'render',
                rippleEffect: {
                    brushType: 'stroke'
                },
                hoverAnimation: true,
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: true
                    }
                },
                itemStyle: {
                    normal: {
                        color: 'rgba(255,255,0,0.8)',
                        shadowBlur: 10,
                        shadowColor: '#05C3F9'
                    }
                },
                zlevel: 1
            },

        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function echarts_3(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echarts_3'));
    var echarts_3Data = [];
    var yearSchool = filename;
    filename='xueyuanjiuyelv.json';
    var j = 0;
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        for (var i=0;i<data3.length;i++){
            if (data3[i].school_code == school && data3[i].year == year){
                echarts_3Data[j]=data3[i];
                j++;
            }
        }
        // echarts_3data = data3;
    });
    /*$.ajaxSettings.async = false;
    $.getJSON("../static/data/2019zzulijiuyelv.json", function (data3) {
        echarts_3data = data3;
    });*/
    echarts_3dataName = [];
    echarts_3dataValue = [];
    for (var i = 0; i < echarts_3Data.length; i++) {
        echarts_3dataName[i] = echarts_3Data[i].name;
        echarts_3dataValue[i] = (echarts_3Data[i].value * 100).toFixed(2);
    }
    option = {

        tooltip: {
            trigger: 'axis'
        },
        legend: {
            orient: 'vertical',
            data: ['简易程序案件数']
        },
        grid: {
            left: '3%',
            right: '3%',
            top: '8%',
            bottom: '10%',
            containLabel: true
        },
        color: ['#a4d8cc', '#25f3e6'],
        toolbox: {
            show: false,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },

        calculable: true,
        xAxis: [
            {
                type: 'category',

                axisTick: {show: false},

                boundaryGap: false,
                axisLabel: {
                    textStyle: {
                        color: '#ccc',
                        fontSize: '12'
                    },
                    lineStyle: {
                        color: '#2c3459',
                    },
                    interval: {default: 0},
                    rotate: 50,
                    formatter: function (params) {
                        var newParamsName = "";// 最终拼接成的字符串
                        var paramsNameNumber = params.length;// 实际标签的个数
                        var provideNumber = 4;// 每行能显示的字的个数
                        var rowNumber = Math.ceil(paramsNameNumber / provideNumber);// 换行的话，需要显示几行，向上取整
                        /**
                         * 判断标签的个数是否大于规定的个数， 如果大于，则进行换行处理 如果不大于，即等于或小于，就返回原标签
                         */
                        // 条件等同于rowNumber>1
                        if (paramsNameNumber > provideNumber) {
                            /** 循环每一行,p表示行 */
                            var tempStr = "";
                            tempStr = params.substring(0, 4);
                            newParamsName = tempStr + "...";// 最终拼成的字符串
                        } else {
                            // 将旧标签的值赋给新标签
                            newParamsName = params;
                        }
                        //将最终的字符串返回
                        return newParamsName
                    }

                },
                data: echarts_3dataName
            }
        ],
        yAxis: {

            type: 'value',
            min: 70,
            max: 100,
            axisLabel: {
                textStyle: {
                    color: '#ccc',
                    fontSize: '12',
                }
            },
            axisLine: {
                lineStyle: {
                    color: 'rgba(160,160,160,0.3)',
                }
            },
            splitLine: {
                lineStyle: {
                    color: 'rgba(160,160,160,0.3)',
                }
            },

        }
        ,
        series: [
            {
                // name:'简易程序案件数',
                type: 'line',
                areaStyle: {

                    normal: {
                        type: 'default',
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 0.8, [{
                            offset: 0,
                            color: '#25f3e6'
                        }, {
                            offset: 1,
                            color: '#0089ff'
                        }], false)
                    }
                },
                smooth: true,
                itemStyle: {
                    normal: {areaStyle: {type: 'default'}}
                },
                data: echarts_3dataValue
            }
        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function echarts_4(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echarts_4'));

    //数据
    var echarts_4Data=[];
    var yearSchool = filename;
    filename='xueyuan.json';
    var j = 0;
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        for (var i=0;i<data3.length;i++){
            if (data3[i].school_code == school && data3[i].year == year){
                echarts_4Data[j]=data3[i];
                j++;
            }
        }
        // echarts_4Data = data3;
    });
    /*$.ajaxSettings.async = false;
    $.getJSON("../static/data/2019zzulixueyuan.json", function (data3) {
        echarts_4Data = data3;
    });*/
    option = {

        tooltip: {
            trigger: 'item',
            /*formatter: "{b}: <br/>  {c} ({d}%)",*/
            formatter: function (params) {
                if (params.seriesName != "") {
                    return params.name + "<br/>" +
                        "学生人数：" + params.value + "(" + (params.data.xueyuan_bili * 100).toFixed(2) + "%)<br/>" +
                        "就业人数：" + params.data.xueyuan_jiuye_num + "<br/>" +
                        "就业率：" + (params.data.jiuyelv * 100).toFixed(2) + "%";
                }
            },
        },


        toolbox: {
            show: false,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {
                    show: true,
                    type: ['pie', 'funnel']
                },
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        series: [

            {
                name: '排名',
                type: 'pie',
                color: ['#af89d6', '#f5c847', '#ff999a', '#0089ff', '#25f3e6', '#f5c847', '#ff999a', '#0089ff', '#25f3e6', '#f5c847', '#ff999a', '#0089ff', '#25f3e6', '#f5c847', '#ff999a', '#0089ff', '#25f3e6', '#f5c847', '#ff999a', '#0089ff', '#25f3e6'],
                radius: [60, 300],
                center: ['50%', '50%'],
                roseType: 'area',
                data: echarts_4Data
            }
        ]
    };


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function echarts_5(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echarts_5'));

    //数据
    var echarts_5Data;
    var yearSchool = filename;
    filename=filename+'channel.json'
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        echarts_5Data = data3;
    });
    /*$.ajaxSettings.async = false;
    $.getJSON("../static/data/2019zzulichannel.json", function (data3) {
        echarts_5Data = data3;
    });*/
    var dataValue = [];
    var xData = function () {
        var data = ['软件工程', '人工智能', '大数据', '金融学', '会计学'];
        data = [];
        for (var i = 0; i < echarts_5Data.length; i++) {
            data[i] = echarts_5Data[i].name;
            dataValue[i] = (echarts_5Data[i].value * 100).toFixed(2);
        }

        return data;
    }();

    var data = [28, 22, 20, 16, 12]

    option = {
        // backgroundColor: "#141f56",

        tooltip: {
            show: "true",
            trigger: 'item',
            backgroundColor: 'rgba(0,0,0,0.4)', // 背景
            padding: [8, 10], //内边距
            // extraCssText: 'box-shadow: 0 0 3px rgba(255, 255, 255, 0.4);', //添加阴影
            formatter: function (params) {
                if (params.seriesName != "") {
                    return params.name + ' ：  ' + params.value + '%';
                }
            },

        },
        grid: {
            borderWidth: 0,
            top: 20,
            bottom: 35,
            left: 55,
            right: 30,
            textStyle: {
                color: "#fff"
            }
        },
        xAxis: [{
            type: 'category',
            axisTick: {
                show: false
            },
            axisLine: {
                show: true,
                lineStyle: {
                    color: '#363e83',
                }
            },
            axisLabel: {
                inside: false,
                rotate: 45,
                textStyle: {
                    color: '#bac0c0',
                    fontWeight: 'normal',
                    fontSize: '12',
                },
                // formatter:function(val){
                //     return val.split("").join("\n")
                // },
            },
            // data: xData,
            data: xData
        }, {
            type: 'category',
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false
            },
            splitArea: {
                show: false
            },
            splitLine: {
                show: false
            },
            data: xData,
        }],
        yAxis: {
            type: 'value',
            axisTick: {
                show: false
            },
            axisLine: {
                show: true,
                lineStyle: {
                    color: '#32346c',
                }
            },
            splitLine: {
                show: true,
                lineStyle: {
                    color: '#32346c ',
                }
            },
            axisLabel: {
                textStyle: {
                    color: '#bac0c0',
                    fontWeight: 'normal',
                    fontSize: '12',
                },
                formatter: '{value}',
            },
        },
        series: [{
            // name: '生师比(%)',
            type: 'bar',
            itemStyle: {
                normal: {
                    show: true,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#00c0e9'
                    }, {
                        offset: 1,
                        color: '#3b73cf'
                    }]),
                    barBorderRadius: 50,
                    borderWidth: 0,
                },
                emphasis: {
                    shadowBlur: 15,
                    shadowColor: 'rgba(105,123, 214, 0.7)'
                }
            },
            zlevel: 2,
            barWidth: '20%',
            // data: data,
            data: dataValue
        },
            {
                name: '',
                type: 'bar',
                xAxisIndex: 1,
                zlevel: 1,
                itemStyle: {
                    normal: {
                        color: '#121847',
                        borderWidth: 0,
                        shadowBlur: {
                            shadowColor: 'rgba(255,255,255,0.31)',
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowOffsetY: 2,
                        },
                    }
                },
                barWidth: '20%',
                data: [30, 30, 30, 30, 30]
            }
        ]
    }


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function echarts_6(filename) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echarts_6'));
    var echarts_6data;
    var yearSchool = filename;
    filename=filename+'pipei.json'
    $.ajaxSettings.async = false;
    $.getJSON("../static/data/"+yearSchool+"/"+filename, function (data3) {
        echarts_6data = data3;
    });
    /*$.ajaxSettings.async = false;
    $.getJSON("../static/data/2019zzulipipei.json", function (data3) {
        echarts_6data = data3;
    });*/
    var xAxisMonth = [],
        barData = [],
        lineData = [];
    for (var i = 0; i < echarts_6data.length; i++) {
        xAxisMonth.push(echarts_6data[i].name);
        barData.push({
            "name": xAxisMonth[i],
            "value": echarts_6data[i].value
        });
        lineData.push({
            "name": xAxisMonth[i],
            "value": echarts_6data[i].ratio
        });
    }
    echarts_6dataName = [];
    echarts_6dataValue = [];
    for (var i = 0; i < echarts_6data.length; i++) {
        echarts_6dataName = echarts_6data[i].name;
        echarts_6dataValue = echarts_6data[i].value;
    }

    option = {
        // backgroundColor: "#020d22",
        title: '',
        grid: {
            top: '10%',
            left: '18%',
            bottom: '3%',
            right: '5%',
            containLabel: true
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'none'
            },
            formatter: function (params) {
                return params[0]["data"].name + "<br/>" + '占比: ' + (params[1]["data"].value * 100).toFixed(2) + '%';
            }
        },
        xAxis: [{
            type: 'category',
            show: false,
            data: echarts_6dataName,
            axisLabel: {
                textStyle: {
                    color: '#b6b5ab'
                }
            }
        },
            {
                type: 'category',
                position: "bottom",
                data: xAxisMonth,
                boundaryGap: true,
                // offset: 40,
                splitLine: {
                    show: false,
                    lineStyle: {
                        color: "rgba(255,255,255,0.2)"
                    }
                },
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    color: "rgba(255,255,255,0.2)"
                },
                axisLabel: {
                    textStyle: {
                        color: '#b6b5ab'
                    }
                }
            }

        ],
        yAxis: [{
            show: true,
            offset: 52,
            splitLine: {
                show: false,
                lineStyle: {
                    color: "rgba(255,255,255,0.2)"
                }
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: true,
                color: "rgba(255,255,255,0.2)"
            },
            axisLabel: {
                show: true,
                color: '#b6b5ab'
            }
        }, {
            show: false,
            type: "value",
            // name: "合格率(%)",
            nameTextStyle: {
                color: '#ccc'
            },
            axisLabel: {
                color: '#ccc'
            },
            splitLine: {
                show: false
            },
            axisLine: {
                show: true
            },
            axisTick: {
                show: true
            }
        }],
        color: ['#e54035'],
        series: [{
            name: '训练人次',
            type: 'pictorialBar',
            xAxisIndex: 1,
            barCategoryGap: '-80%',
            // barCategoryGap: '-5%',
            symbol: 'path://d="M150 50 L130 130 L170 130  Z"',
            itemStyle: {
                normal: {
                    color: function (params) {
                        var colorList = [
                            'rgba(13,177,205,0.8)', 'rgba(29,103,182,0.6)',
                            'rgba(13,177,205,0.8)', 'rgba(29,103,182,0.6)',
                            'rgba(13,177,205,0.8)', 'rgba(29,103,182,0.6)'
                        ];
                        return colorList[params.dataIndex];
                    }
                },
                emphasis: {
                    opacity: 1
                }
            },
            data: barData,
        },
            {
                symbol: 'image://data:image/png;base64,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',
                symbolSize: 42,
                name: "完成率",
                type: "line",
                yAxisIndex: 1,
                data: lineData,
                itemStyle: {
                    normal: {
                        borderWidth: 5,
                        color: {
                            colorStops: [{
                                offset: 0,
                                color: '#821eff'
                            },

                                {
                                    offset: 1,
                                    color: '#204fff'
                                }
                            ],
                        }
                    }
                }
            }
        ]
    }


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}







