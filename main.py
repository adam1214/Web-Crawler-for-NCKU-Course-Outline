import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# 下載Course Outline內容
r = requests.get('http://class-qry.acad.ncku.edu.tw/syllabus/online_display.php?syear=0108&sem=2&co_no=F731700&class_code=')
r.encoding='big5'
# 確認是否下載成功
if r.status_code == requests.codes.ok:
    # 以 BeautifulSoup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('div', 'block')
  
    for div in divs:
        #print('1111111111111')
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
            print(str.split('#'))

            #任意的多組列表
            a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            b = str.split('#')
            #字典中的key值即為csv中列名
            dataframe = pd.DataFrame({'Week':a,'Progress Description':b})
            #將DataFrame儲存為csv,index表示是否顯示行名，default=True
            dataframe.to_csv("result.csv",index=False,sep=',')
    