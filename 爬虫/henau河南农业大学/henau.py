# http://job.henau.edu.cn/module/newsdetail/id-40194

import csv
from time import sleep
import xlwt
import lxml
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}

url = 'http://job.henau.edu.cn/module/newsdetail/id-40194'

excel1 = xlwt.Workbook()
# 设置单元格
sheet1 = excel1.add_sheet('Job', cell_overwrite_ok=True)
sheet1.write(0, 0, '生源人数')
sheet1.write(0, 1, '就业去向')
sheet1.write(0, 2, '薪酬')
sheet1.write(0, 3, '就业渠道')
sheet1.write(0, 4, '学院')
sheet1.write(0, 5, '学院人数')
sheet1.write(0, 6, '专业')
sheet1.write(0, 7, '专业人数')
sheet1.write(0, 8, '学院就业率')
sheet1.write(0, 9, '专业就业率')
sheet1.write(0, 10, '公司规模')
sheet1.write(0, 11, '岗位匹配度')
sheet1.write(0, 12, '行业经济性质')
def toexcel():
    print()


def getPerPageInfo(url,number):
    html = requests.get(url, headers=headers).text
    mytree = lxml.etree.HTML(html)
    postList = mytree.xpath('//ul[@class="sojob-list"]/li')
    # print(postList)
    number2 = number+1
    print("抓取下面这一页数据")
    print(number)
    for post in postList:
        if number2 == 81 :
            break
        postTitle = post.xpath('.//div[@class="job-info"]/h3/a/text()')[0]
        postInfo = post.xpath('.//div[@class="job-info"]/p/span//text()')
        postadd = post.xpath('.//div[@class="job-info"]/p/a//text()')
        postSalary = postInfo[0]
        postEDU = postInfo[1]
        postExperience = postInfo[2]
        postName = post.xpath('.//p[@class="company-name"]/a/text()')
        posturl = post.xpath('.//div[@class="job-info"]/h3/a/@href')[0]
        gongsiguimo = requests.get(posturl,headers=headers).text
        mytree2 = lxml.etree.HTML(gongsiguimo)
        postList2 = mytree2.xpath('.//ul[@class="new-compintro"]/li//text()')
        guimo1 = postList2[1]
        guimo2 = postList2[3]
        guimo2 = guimo2.strip('行业经济：')
        guimo3 = postList2[4]
        guimo2 = guimo2.strip('公司规模：')
        postxingzhi = post.xpath('.//p[@class="field-financing"]/span/text()')
        postfuli = post.xpath('.//p[@class="temptation clearfix"]/span//text()')
        postfuli1 = ''
        for fuli in postfuli:
            postfuli1 = postfuli1 + " "+fuli

        # postfuli1 = postfuli[0]
        # postfuli2 = postfuli[1]
        # postfuli3 = postfuli[2]
        # postfuli4 = postfuli1+postfuli2+postfuli3

        infoList = [postTitle, postSalary,postadd, postEDU, postExperience,postName,postxingzhi,postfuli1,guimo1,guimo2]
        print(number2,postTitle, postSalary, postEDU, postExperience,postName,postxingzhi,postfuli1)
        sheet1.write(number2, 0, number2)
        sheet1.write(number2, 1, infoList[0])
        sheet1.write(number2, 2, infoList[1])
        sheet1.write(number2, 3, infoList[2])
        sheet1.write(number2, 4, infoList[3])
        sheet1.write(number2, 5, infoList[4])
        sheet1.write(number2, 6, infoList[5])
        sheet1.write(number2, 7, infoList[6])
        sheet1.write(number2, 8, infoList[7])
        sheet1.write(number2, 9, infoList[9])
        sheet1.write(number2, 10, infoList[10])
        sheet1.write(number2, 11, infoList[11])
        excel1.save("henau.xlsx")
        number2+=1
        # 将得到的数据用csv格式存储
        writer.writerow(infoList)  # writerows()会把单个字符写入到一个单元格中，而writerow()会把一个字符串写入一个单元格中
        sleep(0.3)


if __name__ == '__main__':
    csvHeader=[]
    with open('./henau.csv', 'a+', encoding='utf-8', errors='ignore', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csvHeader)
        number = 0
        for i in range(101):
            url = url + str(i)
            getPerPageInfo(url,number)
            number+=40
            sleep(0.5)  # 每一页爬取时延迟一会，防止对别人服务器造成太大压力

excel1.save("henau.xlsx")