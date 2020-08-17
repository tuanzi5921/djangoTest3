import xlrd
import json
import requests

def openWorkbook():
    # 读取excel表的数据
    workbook = xlrd.open_workbook(r'F:\ceshishuju\beifen\city.xlsx')
    # 选取需要读取数据的那一页
    sheet = workbook.sheet_by_index(0)
    # 获得行数和列数
    rows = sheet.nrows
    cols = sheet.ncols
    # 创建一个数组用来存储excel中的数据
    p = []
    for i in range(1, rows):
        d = {}
        for j in range(0, cols):
            q = '%s' % sheet.cell(0, j).value
            d[q] = sheet.cell(i, j).value
        ap = []
        for k, v in d.items():
            if isinstance(v, float):  # excel中的值默认是float,需要进行判断处理，通过'"%s":%d'，'"%s":"%s"'格式化数组

                if (v<1):
                    # 针对百分比数据处理，保留四位小数
                    ap.append('"%s":%0.4f' % (k, v))
                else:
                    # 若数据为整数，则转为整数
                    ap.append('"%s":%d' % (k, v))
                    # ap.append('"%s":%0.4f' % (k, v))
            else:
                ap.append('"%s":"%s"' % (k, v))
        s = '{%s}' % (','.join(ap))  # 继续格式化
        p.append(s)
    t = '[%s]' % (','.join(p))  # 格式化
    data=json.dumps(t,ensure_ascii=False)
    print(data.replace("\\",""))
    # with open('student4.json',"w",encoding='utf-8') as f:
    #     f.write(t)
#openWorkbook()
url="http://111.111.111.111:8000/pushdata/"
headers={"Content-Type":"application/json"}
data=openWorkbook()
re=requests.post(url=url,headers=headers,data=data)
print(re.text)