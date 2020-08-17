# Generated by Django 3.0.5 on 2020-04-14 13:54

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=128)),
                ('value', models.CharField(max_length=512)),
                ('group', models.CharField(db_index=True, max_length=128, verbose_name='组')),
            ],
            options={
                'verbose_name': '字典列表',
                'verbose_name_plural': '字典列表',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='菜单名')),
                ('icon', models.CharField(blank=True, max_length=32, null=True, verbose_name='图标字体')),
                ('href', models.CharField(max_length=128, verbose_name='链接地址')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('display', models.BooleanField(db_index=True, default=True, verbose_name='显示')),
                ('sort', models.IntegerField(db_index=True, default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单管理',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('createDate', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告管理',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(db_index=True, max_length=256, verbose_name='别名')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('keywords', models.CharField(blank=True, max_length=512, null=True, verbose_name='关键字')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='描述')),
                ('content', mdeditor.fields.MDTextField(verbose_name='内容')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('display', models.BooleanField(db_index=True, default=True, verbose_name='是否显示')),
                ('head', models.TextField(blank=True, null=True, verbose_name='头部脚本')),
                ('footer', models.TextField(blank=True, null=True, verbose_name='尾部脚本')),
            ],
            options={
                'verbose_name': '页面',
                'verbose_name_plural': '页面管理',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=256, verbose_name='网址')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('contactType', models.IntegerField(choices=[(0, 'QQ'), (1, '微信'), (2, '邮箱'), (3, '手机')], default=0, verbose_name='类型')),
                ('contact', models.CharField(max_length=128, verbose_name='联系方式')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sort', models.IntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': '友链',
                'verbose_name_plural': '友链管理',
            },
        ),
    ]
