import requests
from bs4 import BeautifulSoup

# 下載Course Outline內容
r = requests.get('http://class-qry.acad.ncku.edu.tw/syllabus/online_display.php?syear=0108&sem=2&co_no=F731700&class_code=')
r.encoding='big5'
# 確認是否下載成功
if r.status_code == requests.codes.ok:
    # 以 BeautifulSoup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    divs = soup.find_all('div', 'block')
  
    for div in divs:
        print(div.text)
    