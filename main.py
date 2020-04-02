import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

'''
w：新建檔案寫入(檔案可不存在，若存在則清空，適用於第一次寫入的資料)
a：資料附加到舊檔案後面(游標指在EOF)
'''

# 下載Course Outline內容
r = requests.get('http://class-qry.acad.ncku.edu.tw/syllabus/online_display.php?syear=0108&sem=2&co_no=F731700&class_code=')
r.encoding='big5'
# 確認是否下載成功
if r.status_code == requests.codes.ok:
    # 以 BeautifulSoup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('div', 'block')

    for div in divs:

        if div.text.find('先修課程或先備能力') != -1:
            with open('result.csv', 'w', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])  
            csvfile.close()

        if div.text.find('教師聯絡資訊') != -1:
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])  
            csvfile.close()

        if div.text.find('參考書目') != -1:
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])  
            csvfile.close()

        if div.text.find('課程概述') != -1:
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])  
            csvfile.close()

        if div.text.find('課程學習目標') != -1:
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])  
            csvfile.close()

        if div.text.find('評量方式') != -1:
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])  
            csvfile.close()

        if div.text.find('教學方法') != -1:
            #print(div.text)           
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])
                #writer.writerow(['method', '%'])
                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])     
            csvfile.close()

        if div.text.find('課程教材') != -1:
            #print(div.text)
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])

                str = div.text.splitlines()
                for sub_str in str:
                    writer.writerow([sub_str])       
            csvfile.close()
           
        if div.text.find('課程進度') != -1:
            str = div.text.splitlines()[5]
            str=str.replace("10", "#")
            str=str.replace("11", "#")
            str=str.replace("12", "#")
            str=str.replace("13", "#")
            str=str.replace("14", "#")
            str=str.replace("15", "#")
            str=str.replace("16", "#")
            str=str.replace("17", "#")
            str=str.replace("18", "#")
            str=str.replace("1", "")
            str=str.replace("2", "#")
            str=str.replace("3", "#")
            str=str.replace("4", "#")
            str=str.replace("5", "#")
            str=str.replace("6", "#")
            str=str.replace("7", "#")
            str=str.replace("8", "#")
            str=str.replace("9", "#")
            str=str.replace("##", "#")
            #print(str.split('#'))

            #任意的多組列表
            a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            b = str.split('#')
            with open('result.csv', 'a', newline='') as csvfile:
                # 建立 CSV 檔寫入器
                writer = csv.writer(csvfile)
                # 寫入一列空白資料做區隔
                writer.writerow([''])
                #字典中的key值即為csv中列名
                dataframe = pd.DataFrame({'Week':a,'Progress Description':b})
                dataframe = dataframe.reindex(columns=['Week', 'Progress Description'])
                #將DataFrame儲存為csv,index表示是否顯示行名，default=True
                dataframe.to_csv(csvfile,index=False,sep=',')
            csvfile.close()
    