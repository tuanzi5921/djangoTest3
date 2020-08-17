from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template.loader import get_template
# Create your views here.

def add_test(request):
    # user1 = User(name='李四',age=76)
    # user2 = User(name='王五',age=55)
    # user3 = User(name='赵六',age=66)

    # User.name = '张三'
    # User.age = 37
    # 两种方法保存皆可
    # User.save(user1)
    # 该方法不用执行save
    User.objects.create(name='张飞',age=28)
    # User.objects.get_or_create(name='赵子龙',age=21)
    # user3.save(user3)


    return HttpResponse("保存数据成功")

def del_test(request):
    User.objects.get(id=4).delete()
    return HttpResponse("删除数据成功")

def edit_test(request):
    rs = User.objects.get(id=3)
    rs.name = '曹操'
    rs.save()
    s= ("修改id=%s name=%s 的数据成功"%(rs.id,rs.name))
    # 全表修改数据
    User.objects.all().update(city='Beijing')
    return HttpResponse(s)

def select_test(request):
    # 查询所有数据
    rs = User.objects.all()
    # 索引
    rs[0]
    rs[0:3]# 查询0-3
    for i in rs:
        print(i)
    # 查询单条数据
    # rs = User.objects.get(id=3)
    # 按条件查询
    rs = User.objects.filter(id=3,name='李四',age=30)
    # rs = User.objects.filter()

    # 按条件查询数据
    # 通过具体的方法去查询对应的数据进行筛选
    rs = User.objects.filter(age__gt=18,age__exact=11,age__in=11,age__isnull=2)
    print(rs)

    return HttpResponse("查询数据成功")

def appTest(request):
    s = get_template('testApp/index2.html')
    html = s.render()

    return HttpResponse(html)