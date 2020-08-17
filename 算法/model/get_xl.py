from aip import AipNlp
import json
import time
import re

APP_ID = '19616480'
API_KEY = 'GPhewywNcB5baPxgDqAKUHsK'
SECRET_KEY = 'BENauxDENkOLBWAQgPPUgx8S3PsMOP9f'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

suc=0
fal=0


f = open('F:\\ceshishuju\\test.json',encoding='utf-8')
f_error = open('F:\\ceshishuju\\test1.json','a+',encoding='utf-8')
f_xiangliang = open('F:\\ceshishuju\\test9.json','a+',encoding='utf-8')
com_dic = json.load(f)

#统计逗号个数，相当于返回分词个数，用于控制下面for循环次数
def fun_c(text):
    a=0
    for ch in text:
        if ch==',':
            a+=1
    print("分词个数为：",a )
    return a

for index in range(len(com_dic)):
    #temp迭代每条
    temp = com_dic[index]
    #item是一个字典
    try:
        #正则表达式摘取格式
        pat = "(.*?),"
        rst = re.compile(pat).findall(temp['words'])
        rst2 = re.compile(pat).findall(temp['words2'])
        #vec_f为整型代表无向量分词的个数，   vec_j为返回的1024维列表：代表分词有向量表示的向量和，   vec_jz为1024维列表：代表分词向量均值
        vec_f = 0
        #1024维列表初始化
        vec_a=[0]*1024
        vec_b=[0]*1024
        vec_bz=[0]*1024
        #sum_w为标题分词的个数，    sum2_w为类型分词的个数      ：用于下面的for循环，循环像百度语音接口请求返回含有词向量，无则跳过
        print("标题分词的词向量分析如下：")
        print(rst)
        sum_w=fun_c(temp['words'])
        for i in range(sum_w):
            words = client.wordEmbedding(rst[i]);
            try:
                words_a = words['vec']
                print(words_a)
                vec_b=[(vec_b[i]+words_a[i]) for i in range(0,len(vec_b))]
            except :
                print("无vec的分词为：",rst[i])
                vec_f=vec_f+1
                time.sleep(3)
                continue
        print("标题获取的vec个数为：",sum_w-vec_f)
        vec_bz=[(vec_bz[i]+vec_b[i])/(sum_w-vec_f) for i in range(0,len(vec_bz))]
        print("标题向量均值为：",vec_bz)
        print("标题向量均值维数为：",len(vec_bz))
        #temp.update(xiangliang=vec_bz)

        vec_f = 0
        # 1024维列表初始化
        vec_l = [0] * 1024
        vec_lz = [0] * 1024
        print('\n')
        print("类型分词的词向量分析如下：")
        print(rst2)
        sum2_w = fun_c(temp['words2'])
        for i in range(sum2_w):
            words2 = client.wordEmbedding(rst2[i]);
            try:
                words_l = words2['vec']
                print(words_l)
                vec_l=[(vec_l[i]+words_l[i]) for i in range(0,len(vec_l))]
            except :
                print("无vec的分词为：",rst[i])
                vec_f=vec_f+1
                time.sleep(3)
                continue
        print("类型获取的vec个数为：",sum2_w-vec_f)
        #当sum2_-vec_f=0时，即是下式子除0了，即是抛出该条
        vec_lz=[(vec_lz[i]+vec_l[i])/(sum2_w-vec_f) for i in range(0,len(vec_lz))]
        print("类型向量均值为：",vec_lz)
        print("类型向量均值维数为：",len(vec_lz))

        print('\n')
        print("------------------------------------一个item的分析分隔符-----------------------------------------")
        #向标题加类型的向量均值：vec_a
        vec_a=[(vec_lz[i]+vec_bz[i])/2 for i in range(0,len(vec_lz))]
        temp.update(xiangliang_a=vec_a)
        #temp.update(xiangliang2=vec_lz)
        # ensure_ascii=False：输出原有的语言文字，可通过该参数实现中文写入。indent：缩进量，一般省略。
        json.dump(temp,open('F:\\ceshishuju\\test9.json','a+',encoding='utf-8'),ensure_ascii=False,indent=4)
    except:
        fal = fal+1
        # 标题词向量均值为0的抛出，写入test1.json
        json.dump(com_dic[index],open('F:\\ceshishuju\\test1.json','a+',encoding='utf-8'),ensure_ascii=False,indent=4)
        time.sleep(3)
        continue
    else:
        suc = suc + 1
        time.sleep(3)
        continue

print("转换成功：",suc)
print("转换失败：",fal)
    
