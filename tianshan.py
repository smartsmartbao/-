import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Option=Options()
Option.add_argument("--headless")
Option.add_argument("--disable-gpu")

URL="https://edu.hellobi.com/course/157/lessons"
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "pgv_pvi=177695744; _ga=GA1.2.1233537806.1554709428; _gid=GA1.2.2105483929.1554709428; poptimese=1; sqv__user_login=ps-Wv5ONmJeem2eCb2LbqpbYlKbFpMeXjl0h4-FMD-YY8bRHwR9H7upO5vsdxxcm7gRWc5Gnw6ykqafTm8G_jGqfa5lompnEnMhmk2pslmeTm5qbyG6TcWNpnJWalsXG; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkxWQmJqVVwvdXFPK0pOd09sTGpJYnJ3PT0iLCJ2YWx1ZSI6Inpaam0yWlo1OWNmRFwvWVlBZlwvNGQ3XC91ZENlNkd0QVZGdnBId0R2cVorUkJLYnNFQnlXVkhTb0kzYzJPN2ZqM2IxNDNTdlRoamc0V2c3OVVUNFNvXC9iSnVoUmZXRkxFWTJ6eDJoNk04b1VMQ0lSXC9Zb3ZQY1QzdjFJVjhxOUNmQmZsdXI5NDhpUmxTYlhJMXArWlY0RGx3PT0iLCJtYWMiOiJiMDg5YTg5NjZiMDBhMWI2ZmRlZmQ0MjZiM2U4ZmRkNjNhOWM3ODVkNjdiYzU3NWEzMzEwOWRlZWQ0N2I0MTdhIn0%3D; pt_3fae31ac=uid=sU5FBemG3YcBlzgULnVeSA&nid=1&vid=cTVjR/fxdp93f/w20Pxq9w&vn=1&pvn=1&sact=1554709534894&to_flag=0&pl=8q7ilDwjuKwUqZ6cGnaXEw*pt*1554709534251; pgv_si=s7184666624; Hm_lvt_2d2777148aa1618ef79baf55c005df84=1554709428,1554709531,1554793140; _gat=1; XSRF-TOKEN=eyJpdiI6IlZ3b0Rvb1wvZHc4ZkpcLzVOcXU2aTBlQT09IiwidmFsdWUiOiJIUWpCMzhwZHYybTZ2RWY2dGdHXC9XTnhwUnJXZnZqaXcxSkM4bWJ2Q3BmbHhvczBYTG5FUU5TZVA5eU1waWVCY3hCUHRsN1NEamlLdXlaUmdHMGhQM2c9PSIsIm1hYyI6IjAzMjc1M2JlOWYwMmY3ZGVmMmM3Yzc0Yjc3MzIxZWRjYjNkZGEyYzAzNmYzM2QzMjRhZTg4YzUwNDI1MTdkODAifQ%3D%3D; laravel_session=eyJpdiI6IkZUZ3NyODRERFhpTzVSOXFqVjl0bkE9PSIsInZhbHVlIjoiVzZSZmRXOEgzR2ZcL3JLQ0VNaUp4MjFZbUJJVmV4RGNaUzdDOUpKaU1PZERhaVpTQVBsUTUrUlY5NjZTeDJUaUxtTFJieGVoZnYzSDRld2dlUEx5cHhBPT0iLCJtYWMiOiIwMjIwZjI0NDRiNzBkOTIwYTAzM2Q4NjZjMzYwOWE0MjJiMjM0Y2VjYTczYzUxYjJhY2U0Yjg4MDUxMGI4YzJkIn0%3D; Hm_lpvt_2d2777148aa1618ef79baf55c005df84=1554794657",
    "Host": "edu.hellobi.com",
    "Pragma": "no-cache",
    "Referer": "https://edu.hellobi.com/course/157",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
headers1={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cookie": "pgv_pvi=177695744; _ga=GA1.2.1233537806.1554709428; _gid=GA1.2.2105483929.1554709428; sqv__user_login=ps-Wv5ONmJeem2eCb2LbqpbYlKbFpMeXjl0h4-FMD-YY8bRHwR9H7upO5vsdxxcm7gRWc5Gnw6ykqafTm8G_jGqfa5lompnEnMhmk2pslmeTm5qbyG6TcWNpnJWalsXG; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkxWQmJqVVwvdXFPK0pOd09sTGpJYnJ3PT0iLCJ2YWx1ZSI6Inpaam0yWlo1OWNmRFwvWVlBZlwvNGQ3XC91ZENlNkd0QVZGdnBId0R2cVorUkJLYnNFQnlXVkhTb0kzYzJPN2ZqM2IxNDNTdlRoamc0V2c3OVVUNFNvXC9iSnVoUmZXRkxFWTJ6eDJoNk04b1VMQ0lSXC9Zb3ZQY1QzdjFJVjhxOUNmQmZsdXI5NDhpUmxTYlhJMXArWlY0RGx3PT0iLCJtYWMiOiJiMDg5YTg5NjZiMDBhMWI2ZmRlZmQ0MjZiM2U4ZmRkNjNhOWM3ODVkNjdiYzU3NWEzMzEwOWRlZWQ0N2I0MTdhIn0%3D; pt_3fae31ac=uid=sU5FBemG3YcBlzgULnVeSA&nid=1&vid=cTVjR/fxdp93f/w20Pxq9w&vn=1&pvn=1&sact=1554709534894&to_flag=0&pl=8q7ilDwjuKwUqZ6cGnaXEw*pt*1554709534251; pgv_si=s7184666624; Hm_lvt_2d2777148aa1618ef79baf55c005df84=1554709428,1554709531,1554793140; XSRF-TOKEN=eyJpdiI6IkNERGV5RzJzZUhZM3dId1MyZmFxUUE9PSIsInZhbHVlIjoiYXJpcFwvazltdWdoenI5RXFDbW1rZEwza0hqMFwvUTRKdGRNaDVnVXZKZ2gzQ01CaVVpcVhqd3phSjJBSWZHXC9FbjNPd0pWMTh6XC85dEVxRkZWXC9OYU9odz09IiwibWFjIjoiMWU3NjY3NDFkYTMzMTk5ZTI5NTQ3YjE3Mzk4ODA0MzYyMDFkNzdjMTYwYjczMTZlZGM2NDZjYjM2OWU5M2Y3NCJ9; laravel_session=eyJpdiI6IlNwRWVxNjg5NUlVXC9IZkhLdmRiSHZnPT0iLCJ2YWx1ZSI6ImVmdXZhdmg1Y3Q0RUtNWHRJbU1Vb2tLYVpzVXNOZDd1dmxUY242U0JTYlNGZzZ6Slp1MW5rZk9vdEdhUEY1WitRMTI3emVEMUpkRFk3VFdCZno0Z0t3PT0iLCJtYWMiOiIxN2E0MWQ5ZjI1ZjYyOTgxNmMxODRhYmZlNTg4OTc5ZGRjNmE2ODk3OWMyYzU5YTc2OTE4ODJkOWZiNjMzODU1In0%3D; Hm_lpvt_2d2777148aa1618ef79baf55c005df84=1554801743",
    "pragma": "no-cache",
    "referer": "https://edu.hellobi.com/course/157/lessons",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
def get_text(url):
    response=requests.get(url,headers=headers)
    return response
def get_video_url(url):
    response=get_text(url).text
    soup=BeautifulSoup(response,'lxml')
    video_urls=soup.select("#course-item-list a")
    for video_url in video_urls:
        yield video_url['href']

def download_video(url):
    driver = webdriver.Chrome(chrome_options=Option)
    driver.get('https://passport.hellobi.com/sso/login')
    driver.find_element_by_xpath('//*[@id="register_form"]/div[1]/input').send_keys('463230674@qq.com')
    driver.find_element_by_xpath('//*[@id="register_form"]/div[2]/input').send_keys('9+7=2bmq')
    driver.find_element_by_xpath('//*[@id="register_form"]/button[2]').click()
    dictcookie=driver.get_cookies()
    jsoncookie=json.dumps(dictcookie)
    with open("cookies.json",'w') as f:
        f.write(jsoncookie)
    for url1 in get_video_url(url):
        driver.get(url1)
        response=driver.page_source
        soup=BeautifulSoup(response,'lxml')
        video_download_url=soup.select('#SewisePlayer0 .sewiseplayer-video video')[0]['src']
        title=soup.select('.course-title span')[0].text.split('/')[-1]
        filename=title+video_download_url.split('/')[-1]
        path=os.path.join('video',filename)
        content=requests.get(video_download_url,headers=headers1).content
        with open(path,'wb') as f:
            f.write(content)
            print("%s下载成功"%filename)
if __name__ =="__main__":
    download_video(URL)





