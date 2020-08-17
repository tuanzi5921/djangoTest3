from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                    # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC           # available since 2.26.0
import csv
import re
import sys
import os
import random

class Boss:
    def __init__(self):
        # 设置 chrome 无界面化模式
        self.chrome_options = Options()
        self.driver = webdriver.Chrome()

    def get_url(self,search='人工智能'):
        xuhao = 1
        # 创建文件
        wr.csv_init(search)
        for y in range(1, 11):
            try:
                self.driver.switch_to.window(sreach_window)
            except:
                pass
            url = 'https://www.zhipin.com/c101020100/?query=' + str(search) + '&page=' + str(y) + '&ka=page -' + str(y)
            self.driver.get(url)

            # 获取当前窗口
            sreach_window = self.driver.current_window_handle
            # 每页有 29 条内容
            for x in range(1, 30):
                data = []
                    # 公司名称
                try:
                    xpath_gongsi_name = '//*[@id="main"]/div/div[2]/ul/li[' + str(x) + ']/div/div[1]/div[2]/div/h3/a'
                    WebDriverWait(self.driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_gongsi_name)))
                    gongsi_name = self.driver.find_element_by_xpath(xpath_gongsi_name).text
                except:
                    gongsi_name = ""
                    print(gongsi_name)


                # 薪资
                try:
                    xpath_xinzi = '//*[@id="main"]/div/div[2]/ul/li[' + str(x) + ']/div/div[1]/div[1]/div/div[2]/span'
                    WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_xinzi)))
                    xinzi = self.driver.find_element_by_xpath(xpath_xinzi).text
                except:
                    xinzi = ""
                    print(xinzi)

                # 岗位名称
                try:
                    xpath_gangwei = '//*[@id="main"]/div/div[2]/ul/li[' + str(x) + ']/div/div[1]/div[1]/div/div[1]/span[1]'
                    WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_gangwei)))
                    gangwei = self.driver.find_element_by_xpath(xpath_gangwei).text
                except:
                    gangwei = ""
                    print(gangwei)

                # 公司大小
                try:
                    xpath_size = '//*[@id="main"]/div/div[2]/ul/li[' + str(x) + ']/div/div[1]/div[2]/div/p/text()[2]'
                    WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_size)))
                    type_size = self.driver.find_element_by_xpath(xpath_size).text
                    gongsi_size = re.findall('\d+-\d+人', type_size)[0]  # 正则表达式提取数字，返回一个列表

                    if gongsi_size == '':
                        gongsi_size = re.findall('\d+', type_size)  # 正则表达式提取数字，返回一个列表
                        gongsi_type = type_size.split(gongsi_size)[0]
                    else:
                        gongsi_type = type_size.split(gongsi_size)[0]
                except:
                    gongsi_size = ""
                    gongsi_type = ""
                    print(gongsi_size)
                    print(gongsi_type)

                # 学历
                try:
                    xpath_xueli = '//*[@id="main"]/div/div[2]/ul/li[' + str(x) + ']/div/div[1]/div[1]/div/div[2]/p/text()[2]'
                    WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located((By.XPATH, xueli)))
                    jingyan_xueli = self.driver.find_element_by_xpath(xpath_xueli).text
                except:
                    gongsi_xueli = ""
                    print(gongsi_xueli)

                data.append(xuhao)
                data.append(gongsi_name)
                data.append(gongsi_size)
                data.append(gongsi_type)
                data.append(gangwei)
                data.append(gongsi_xueli)
                data.append(xinzi)
              # data.append(dizhi)
                wr.write(data)
                print("已完成" + str(xuhao) + "条")
                time.sleep(random.randint(1, 5))
                xuhao += 1
            else:
                self.driver.refresh()

class WriteDataToCSV:
    def csv_init(self, path):
        self.path = str(path) + ".csv"
        # 1. 创建文件对象
        self.f = open(self.path, 'a+', encoding='gbk', newline="")
        # 2. 基于文件对象构建 csv写入对象
        self.csv_writer = csv.writer(self.f)
        # 3. 构建列表头
        self.csv_writer.writerow(["序号", "企业名称", "企业规模", "性质/行业", "岗位名称", "学历要求",
                             "工作经验", "专业要求", "薪酬范围", "工作地点"])
        # 4. 关闭文件
        self.f.close()
    def write(self, data):
        with open(self.path, 'a+', encoding='gbk', newline="") as f:
            csv_writer = csv.writer(f)
            # 4. 写入csv文件内容
            csv_writer.writerow(data)
if __name__ == '__main__':
    wr = WriteDataToCSV()
    Boss().get_url()