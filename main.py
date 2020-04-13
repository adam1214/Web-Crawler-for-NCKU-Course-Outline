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
import codecs

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

tablefile = codecs.open('result.csv', 'w', encoding="utf_8_sig") 
# 建立 CSV 檔寫入器
writer = csv.writer(tablefile)

with open('ncku_course.csv', 'r', newline='', encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    row_num = 1
    for row in rows:
        '''
        if row_num == 10:
            break
        '''
        print(row_num)
        if row_num == 1:
            writer.writerow(["學院","系所名稱","系號-序號","課程碼-分班碼","屬性碼","年級","類別","科目名稱","學分","必/選修","教師姓名","已選課人數/餘額","時間","教室","課程大綱","先修課程或先備能力","教師聯絡資訊","評量方式","教學方法","課程教材","參考書目","課程概述","課程學習目標","課程進度"])
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
                        wk1_data = ""
                        wk2_data = ""
                        wk3_data = ""
                        wk4_data = ""
                        wk5_data = ""
                        wk6_data = ""
                        wk7_data = ""
                        wk8_data = ""
                        wk9_data = ""
                        wk10_data = ""
                        wk11_data = ""
                        wk12_data = ""
                        wk13_data = ""
                        wk14_data = ""
                        wk15_data = ""
                        wk16_data = ""
                        wk17_data = ""
                        wk18_data = ""

                        wk1 = soup.find(id='wk1')
                        wk2 = soup.find(id='wk2')
                        wk3 = soup.find(id='wk3')
                        wk4 = soup.find(id='wk4')
                        wk5 = soup.find(id='wk5')
                        wk6 = soup.find(id='wk6')
                        wk7 = soup.find(id='wk7')
                        wk8 = soup.find(id='wk8')
                        wk9 = soup.find(id='wk9')
                        wk10 = soup.find(id='wk10')
                        wk11 = soup.find(id='wk11')
                        wk12 = soup.find(id='wk12')
                        wk13 = soup.find(id='wk13')
                        wk14 = soup.find(id='wk14')
                        wk15 = soup.find(id='wk15')
                        wk16 = soup.find(id='wk16')
                        wk17 = soup.find(id='wk17')
                        wk18 = soup.find(id='wk18')

                        if wk1 != None:
                            wk1_data = wk1.text
                        if wk2 != None:
                            wk2_data = wk2.text 
                        if wk3 != None:
                            wk3_data = wk3.text
                        if wk4 != None:
                            wk4_data = wk4.text  
                        if wk5 != None:
                            wk5_data = wk5.text
                        if wk6 != None:
                            wk6_data = wk6.text
                        if wk7 != None:
                            wk7_data = wk7.text
                        if wk8 != None:
                            wk8_data = wk8.text
                        if wk9 != None:
                            wk9_data = wk9.text
                        if wk10 != None:
                            wk10_data = wk10.text
                        if wk11 != None:
                            wk11_data = wk11.text
                        if wk12 != None:
                            wk12_data = wk12.text
                        if wk13 != None:
                            wk13_data = wk13.text
                        if wk14 != None:
                            wk14_data = wk14.text
                        if wk15 != None:
                            wk15_data = wk15.text
                        if wk16 != None:
                            wk16_data = wk16.text
                        if wk17 != None:
                            wk17_data = wk17.text
                        if wk18 != None:
                            wk18_data = wk18.text                                                 

                        L1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
                        L2 = [wk1_data,wk2_data,wk3_data,wk4_data,wk5_data,wk6_data,wk7_data,wk8_data,wk9_data,wk10_data,wk11_data,wk12_data,wk13_data,wk14_data,wk15_data,wk16_data,wk17_data,wk18_data]
                        Outline = list(zip(L1,L2))
                        #print(Outline)
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],Prerequisite,Contact,Grading,Strategies,Material,References,Description,Objectives,Outline])   
        row_num = row_num + 1
csvfile.close()
tablefile.close()