import pandas as pd
import re
from pyecharts.charts import Funnel,Pie,Geo
from pyecharts import options as opts
import matplotlib.pyplot as plt

file = pd.read_excel(r'51job2.xls',sheet_name='Job')
f = pd.DataFrame(file)
pd.set_option('display.max_rows',None)

add = f['公司地点']
sly = f['薪资']
edu = f['学历要求']
exp = f['工作经验']
address =[]
salary = []
education = []
experience = []
for i in range(0,len(f)):
    try:
        a = add[i].split('-')
        address.append(a[0])
        print(address[i])
        print(sly[i])
        s = re.findall(r'\d*\.?\d+',sly[i],re.S)
        s1= float(s[0])
        s2 =float(s[1])
        salary.append([s1,s2])
        print(salary[i])
        education.append(edu[i])
        print(education[i])
        experience.append(exp[i])
        print(experience[i])
    except:
       pass

min_s=[]							#定义存放最低薪资的列表
max_s=[]							#定义存放最高薪资的列表
for i in range(0,len(experience)):
    min_s.append(salary[i][0])
    max_s.append(salary[i][0])
#matplotlib模块如果显示不了中文字符串可以用以下代码。
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

my_df = pd.DataFrame({'experience':experience, 'min_salay' : min_s, 'max_salay' : max_s})				#关联工作经验与薪资
data1 = my_df.groupby('experience').mean()['min_salay'].plot(kind='line')
plt.show()
my_df2 = pd.DataFrame({'education':education, 'min_salay' : min_s, 'max_salay' : max_s})				#关联学历与薪资
data2 = my_df2.groupby('education').mean()['min_salay'].plot(kind='line')
plt.show()

def get_edu(list):
    education2 = {}
    for i in set(list):
        education2[i] = list.count(i)
    return education2
dir1 = get_edu(education)
# print(dir1)
"""
Piec = (Pie().add("",[list(z) for z in zip(["201{}年/{}季度".format(y,z)for y in range(2) for z in range(1,3)], 
[4.80,4.10,5.80,5.20])],radius=["0%", "75%"], #设置内径外径
rosetype="radius", #玫瑰图有两种类型
label_opts=opts.LabelOpts(is_show=True),).set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例")))return cpie_rosetype().render_notebook()
"""
attr= dir1.keys()
value = dir1.values()
pie = Pie("学历要求",)
pie.add("", [attr,value],  center=[50, 50], radius=[30, 75], rosetype='radius',
        label_opts=opts.LabelOpts(is_show=True) )
pie.render()

def get_address(list):
    address2 = {}
    for i in set(list):
        address2[i] = list.count(i)
    address2.pop('异地招聘')
    # 有些地名可能不合法或者地图包里没有可以自行删除，之前以下名称都会报错，现在好像更新了
    #address2.pop('山东')
    #address2.pop('怒江')
    #address2.pop('池州')
    return address2
dir2 = get_address(address)
#print(dir2)

geo = Geo("大数据人才需求分布图", title_color="#2E2E2E",
          title_text_size=24,title_top=20,title_pos="center", width=1300,height=600)
attr2 = dir2.keys()
value2 = dir2.values()
geo.add("",attr2, value2, type="effectScatter", is_random=True, visual_range=[0, 1000], maptype='china',symbol_size=8, effect_scale=5, is_visualmap=True)
geo.render('大数据城市需求分布图.html')

def get_experience(list):
    experience2 = {}
    for i in set(list):
         experience2[i] = list.count(i)
    return experience2
dir3 = get_experience(experience)
#print(dir3)

attr3= dir3.keys()
value3 = dir3.values()
funnel = Funnel("工作经验漏斗图",title_pos='center')
funnel.add("", attr3, value3,is_label_show=True,label_pos="inside", label_text_color="#fff",legend_orient='vertical',legend_pos='left')
funnel.render('工作经验要求漏斗图.html')
