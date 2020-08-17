from aip import AipNlp
import json
import time

#采用百度分词的分词函数
def chinese_word_cut(mytext):
    item = client.lexer(mytext)
    final = ''
    for index in item['items']:
        if (index['pos']=='nw' or index['pos']=='an' or index['pos']=='nt' or index['pos']=='nz' or index['pos']=='z' or index['pos']=='y' or index['pos']=='q' or index['pos']=='e' or index['pos']=='d' or index['pos']=='n'or index['pos']=='a' or index['pos']=='v'):
            final = final + index['item']+','
    return (final)

####记录成功与失败条目
suc=0
fal=0
#打开评论文件
f = open('F:\\ceshishuju\\fenci\\xueyuan.json',encoding='utf-8')
f_error = open('F:\\ceshishuju\\fenci\\xueyuanexception.json','a+',encoding='utf-8')
f_wordcut = open('F:\\ceshishuju\\fenci\\xueyuanfenci.json','a+',encoding='utf-8')
com_dic = json.load(f)
""" 你的 APPID AK SK """
APP_ID = '19616480'
API_KEY = 'GPhewywNcB5baPxgDqAKUHsK'
SECRET_KEY = 'BENauxDENkOLBWAQgPPUgx8S3PsMOP9f'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

for index in range(len(com_dic)):
    #temp迭代每条
    temp = com_dic[index]
    #item是一个字典
    try:
        wordscut = chinese_word_cut(temp['xueyuan']);
        wordscut2 = chinese_word_cut(temp['name']);
        temp.update(words=wordscut)
        temp.update(words2=wordscut2)
        #  ensure_ascii=False：输出原有的语言文字，可通过该参数实现中文写入。indent：缩进量，一般省略。
        json.dump(temp,open('F:\\ceshishuju\fenci\\xueyuanfenci.json','a+',encoding='utf-8'),ensure_ascii=False,indent=4)
    except:
        fal = fal+1
        json.dump(com_dic[index],open('F:\\ceshishuju\\fenci\\xueyuanexception.json','a+',encoding='utf-8'),ensure_ascii=False,indent=4)
        time.sleep(0.5)
        continue
    else:
        suc = suc + 1
        time.sleep(0.5)
        continue

print("转换成功：",suc)
print("转换失败：",fal)
