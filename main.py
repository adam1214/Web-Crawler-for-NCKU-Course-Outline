'''
# -*-coding:utf-8 -*
import sys  
reload(sys)
sys.setdefaultencoding('utf-8')
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re
from string import digits

'''
Windows環境中，若程式出現"UnicodeEncodeError: ‘cp950’ codec can’t encode character"的錯誤，可於terminal輸入"chcp 65001"來解決
w：新建檔案寫入(檔案可不存在，若存在則清空，適用於第一次寫入的資料)
a：資料附加到舊檔案後面(游標指在EOF)
'''

# 判斷是否為數字
def is_number(num):
  pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
  result = pattern.match(num)
  if result:
    return True
  else:
    return False

with open('ncku_course.csv', 'r', newline='', encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    row_num = 1
    # 以迴圈讀取每一列
    for row in rows:
        if row_num == 5:
            break
        print(row_num)
        if row_num == 1:
            with open('result.csv', 'w', newline='') as tablefile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(tablefile)
                writer.writerow(["學院","系所名稱","系號-序號","課程碼-分班碼","屬性碼","年級","類別","科目名稱","學分","必/選修","教師姓名","已選課人數/餘額","時間","教室","課程大綱","先修課程或先備能力","教師聯絡資訊","評量方式","教學方法","課程教材","參考書目","課程概述","課程學習目標","課程進度"])
            tablefile.close()
        else:
            Prerequisite = ""
            Contact = ""
            Grading = ""
            Strategies = ""
            Material = ""
            References = ""
            Description = ""
            Objectives = ""
            Outline = ""

            # 下載Course Outline內容
            r = requests.get(row[14])
            r.encoding='big5'

            # 確認是否下載成功
            if r.status_code == requests.codes.ok:
                # 以 BeautifulSoup 解析 HTML 程式碼
                soup = BeautifulSoup(r.text, 'html.parser')
                divs = soup.find_all('div', 'block')

                for div in divs:

                    if div.text.find('先修課程或先備能力') != -1:
                        Prerequisite = div.text[1:]

                    if div.text.find('教師聯絡資訊') != -1:
                        Contact = div.text[1:]

                    if div.text.find('參考書目') != -1:
                        References = div.text[1:]

                    if div.text.find('課程概述') != -1:
                        Description = div.text[1:]

                    if div.text.find('課程學習目標') != -1:
                        Objectives = div.text[1:]

                    if div.text.find('評量方式') != -1:
                        #print(div.text)
                        str = div.text.splitlines()
                        index = len(str) - 3
                        L1 = [None] * (index-6)
                        L2 = [None] * (index-6)
                        for i in range(6,index):
                            num = ''.join([x for x in str[i] if x.isdigit()])
                            L1[i-6] = str[i].replace(num,'')
                        for i in range(7,index+1):
                            num = ''.join([x for x in str[i] if x.isdigit()])
                            L2[i-7] = num
                        Grading = list(zip(L1,L2))

                    if div.text.find('教學方法') != -1:
                        #print(div.text)
                        str = div.text.splitlines()  
                        index = len(str) - 3
                        L1 = [None] * (index-5)
                        L2 = [None] * (index-5)
                        for i in range(5,index):
                            num = ''.join([x for x in str[i] if x.isdigit()])
                            L1[i-5] = str[i].replace(num,'')
                        for i in range(6,index+1):
                            num = ''.join([x for x in str[i] if x.isdigit()])
                            L2[i-6] = num

                        Strategies = list(zip(L1,L2))

                    if div.text.find('課程教材') != -1:
                        #print(div.text)
                        Material = div.text[1:]
                        
                    if div.text.find('課程進度') != -1:
                        str = div.text.splitlines()[5]
                        string = ''
                        string_c = ''
                        num = 2
                        index = 1
                        L1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
                        for i in range (1 , 18):
                            match = re.search(L1[i] , str)
                            string_c = str[index:match.span()[0]]+'#'
                            string = string + string_c
                            index = match.span()[1]
                        string = string + str[index:len(str)]
                        L2 = string.split('#')

                        Outline = list(zip(L1,L2))
                        
            with open('result.csv', 'a', newline='') as tablefile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(tablefile)
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],Prerequisite,Contact,Grading,Strategies,Material,References,Description,Objectives,Outline])
            tablefile.close()  
            #break    
        row_num = row_num + 1
csvfile.close()
