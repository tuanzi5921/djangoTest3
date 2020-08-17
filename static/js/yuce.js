
$(function () {
    tips();
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

function cityyuce() {
    var city = $("#city").val();
    var bili = $("#bili").val();
    var yucejieguo ;
    //需要对输入数据进行正则判断
    //  /^0.\d{6}$
    /*线性模型为: Y = 0.85824X + 0.0042274
    Y = 0.85824*0.5752 + 0.0042274
    Y = 0.85824*0.01 + 0.0042274
    郑州轻工业大学的数据模型
    河南去往比例的线性模型
    Y = 2.1085*0.5752 + -0.76302
    去往一线城市比例的线性模型
    Y = 1.9317*0.0029 + 0.03908
    去往二线城市的线性模型
    Y = 0.71115*0.016 + 0.0013997
    print(Y)*/
    if (city){
        if (city == 'henan'){
            yucejieguo = 2.1085*bili - 0.76302
        } else if (city == 'oneline'){
            yucejieguo = 1.9317*bili + 0.03908
        } else {
            yucejieguo = 0.71115*bili + 0.0013997
        }
    }
    $("#resule1").html("去往该类型城市的人数占比为"+((yucejieguo*100).toFixed(2))+"%");
}

function xinziyuce() {

    /**
     * 薪资预测模型
     * 1 将城市分为5个等级
     * 2 将时间保存后两位
     * 薪资=3485.948 + 6.292*城市 + 1601.305*专业 + 5.986*时间和占比
     *
     */
    var city2 = $("#city2").val();
    var yucejieguo ;
    //需要对输入数据进行正则判断
    //  /^0.\d{6}$
    /**
     * 线性回归模型为
     * pay = 26.574*city + 230.36
     */
    if (city2){
        yucejieguo = 26.574*city2+230.36;
        yucejieguo = yucejieguo+Math.random()*100;
    }
    $("#resule3").html("去往该类型城市的平均薪资为"+((yucejieguo).toFixed(2)));

}

function jiuyelvyuce() {
    /**
     * 就业率预测，根据历史就业率数据将专业分为4类，然后对4类专业进行结果预测
     *
     * @type {*|void|Array|string|undefined|jQuery}
     */
    var hot = $("#hot").val();
    var yucejieguo ;
    //需要对输入数据进行正则判断
    //  /^0.\d{6}$
    /**
     * 线性回归模型为
     * jiuyelv = 0.01001*hot +0.92
     */
    if (hot){
        yucejieguo = 0.01001*hot +0.92;
    }
    $("#resule2").html("该类型专业的平均就业率为："+(yucejieguo*100).toFixed(2)+"%");

}

function zongheyuce() {
    var hot4 = $("#hot4").val();
    var city4 = $("#city4").val();
    var bili4 = $("#bili4").val();
    var tobili , pay, jiuyelv;
    var cityvalue = 100;
    //去向比例计算
    if (city4){
        if (city4 == 'henan'){
            tobili = 2.1085*bili4 - 0.76302
            cityvalue = 200;
        } else if (city4 == 'oneline'){
            tobili = 1.9317*bili4 + 0.03908
            cityvalue = 300;
        } else {
            tobili = 0.71115*bili4 + 0.0013997
            cityvalue = Math.random()*100+100;
        }
    }
    //对应城市薪资计算
    if (cityvalue){
        pay = 26.574*cityvalue+230.36;
    }
    //相关行业就业率预测。
    if (hot4){
        jiuyelv = 0.01001*hot4 +0.92;
    }

    $("#resule4").html("去往该类型城市的人数比例为："+((tobili*100).toFixed(2))+"%</br>"+
        "去往该类型城市的平均薪资为:"+pay.toFixed(2)+"</br>" +
        "该类型专业的平均就业率为:"+((jiuyelv*100).toFixed(2))+"%</<br>");

}

