# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Option = Options()
Option.add_argument("--headless")
Option.add_argument("--disable-gpu")

URL = "https://edu.hellobi.com/course/157/lessons"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'pgv_pvi=177695744; _ga=GA1.2.1233537806.1554709428; _gid=GA1.2.2105483929.1554709428; pt_3fae31ac=uid=sU5FBemG3YcBlzgULnVeSA&nid=1&vid=cTVjR/fxdp93f/w20Pxq9w&vn=1&pvn=1&sact=1554709534894&to_flag=0&pl=8q7ilDwjuKwUqZ6cGnaXEw*pt*1554709534251; pgv_si=s7184666624; sqv__user_login=287FkI5ha5hum5pYa5LYqMnVk9TF0pWXwGEa5N4Z4etN8OMYvPMa77pOGdEZ9xQkIQFVoZHVkazWraDUmI6RkZ-emmpjbmzFbMiZaWack2XGmJnJyJxhcZVtlZaXY5fL; poptimese=1; Hm_lvt_2d2777148aa1618ef79baf55c005df84=1554709428,1554709531,1554793140,1554874280; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InZUUzlkd214UE4zMkNuWFpFK1wvMHhBPT0iLCJ2YWx1ZSI6IlJIVzhpTzZNcFZXd1liY2hCV3JVR3B4Y3FZa0FyNDBsaDU2cXJqWXR4aFBvUlFCUjFYTTE1THZ4Nitsc0Z0MTB2OTRHb250eUI0dW9Wb2l4Y2J0VzJ0eEw4cWRLb1F0REpWVTNqNlwvWXZZMnF4ZEpNN3BYdVZEaUYwZkNteFdUWlRmMTNmTGdZaTkzeUM2T1lZOXBMTUE9PSIsIm1hYyI6ImFmODJkYzc3YWQ5MWViYzkxNGMzOTZmNGI0NjYzNzJlY2RiYjBiMDVmMGQ3NzA4OWVjODUxZThkZTI3N2EwZDEifQ%3D%3D; XSRF-TOKEN=eyJpdiI6Ik0zQ3cxeGorOVpUNzd6QjRtOGxaT0E9PSIsInZhbHVlIjoiR1wvYXlnSW53V1JuUVFMN3RvTlwvcjhsV0NLRURjanE2ajlcL1wva2FwdEp5WWRlY2I2RVVVRFVESVVwT205NmxEQ1BKZm9UZmpyYXJKOGkrQytLMUs3TGt3PT0iLCJtYWMiOiIyN2Q5OGI0NTE3Yzk5NmMyM2ZlOThiMTUzYjg0ODBiZTE1OTliYjExNjM1NmU4YjYyODM2YmJlMDdlYjk3ZmUzIn0%3D; laravel_session=eyJpdiI6IjRsZVFDYXAzSG8xOVdJcjhDM2g5c1E9PSIsInZhbHVlIjoiaVdXZnRjeGlRZlVKV1QzaGhKcjZ0N3pcL0FKbmllKzh1djMzbUhOSVZGUFwvVzhWa3lHQVBvdjBqK3ZpWGZnQ2d4YUNKXC8rNVlmVFozNmJ3OHpyVGJ4b3c9PSIsIm1hYyI6IjAzYzA5MWEzZDFlMjkxNDJkZDdlZmU2OGExMDVhNDI3NjZiMWMwZGI3MjFlN2MxYjJhMWQ5ZTAwY2JiMzY1MWEifQ%3D%3D; Hm_lpvt_2d2777148aa1618ef79baf55c005df84=1554874557',
    'Host': 'edu.hellobi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://edu.hellobi.com/course/157/lessons',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
headers1 = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cookie": 'pgv_pvi=177695744; _ga=GA1.2.1233537806.1554709428; _gid=GA1.2.2105483929.1554709428; pt_3fae31ac=uid=sU5FBemG3YcBlzgULnVeSA&nid=1&vid=cTVjR/fxdp93f/w20Pxq9w&vn=1&pvn=1&sact=1554709534894&to_flag=0&pl=8q7ilDwjuKwUqZ6cGnaXEw*pt*1554709534251; pgv_si=s7184666624; sqv__user_login=287FkI5ha5hum5pYa5LYqMnVk9TF0pWXwGEa5N4Z4etN8OMYvPMa77pOGdEZ9xQkIQFVoZHVkazWraDUmI6RkZ-emmpjbmzFbMiZaWack2XGmJnJyJxhcZVtlZaXY5fL; poptimese=1; Hm_lvt_2d2777148aa1618ef79baf55c005df84=1554709428,1554709531,1554793140,1554874280; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InZUUzlkd214UE4zMkNuWFpFK1wvMHhBPT0iLCJ2YWx1ZSI6IlJIVzhpTzZNcFZXd1liY2hCV3JVR3B4Y3FZa0FyNDBsaDU2cXJqWXR4aFBvUlFCUjFYTTE1THZ4Nitsc0Z0MTB2OTRHb250eUI0dW9Wb2l4Y2J0VzJ0eEw4cWRLb1F0REpWVTNqNlwvWXZZMnF4ZEpNN3BYdVZEaUYwZkNteFdUWlRmMTNmTGdZaTkzeUM2T1lZOXBMTUE9PSIsIm1hYyI6ImFmODJkYzc3YWQ5MWViYzkxNGMzOTZmNGI0NjYzNzJlY2RiYjBiMDVmMGQ3NzA4OWVjODUxZThkZTI3N2EwZDEifQ%3D%3D; _gat=1; XSRF-TOKEN=eyJpdiI6InJ1d1JnZ1Znd3ZOTVdQRWRweTFtdXc9PSIsInZhbHVlIjoiMjdBeVNDRU9cLzJQVE9uY1pIb1BkTitrNlRJbm96anJNaWplQWM2eDRTZWVicGRCN1B0XC83cjVRSytwUkxtTlwvZ0NnbENUc29WQ0VUSWJpbjRuK0hxVkE9PSIsIm1hYyI6ImNlMDM3OWY0M2QwODBkYzZmMTQyODY5MmZmMjFhYzZmNjNiZWM5YjA3ZmRhNGFjNWUxOGI1N2U1NWMyNmJmNGQifQ%3D%3D; laravel_session=eyJpdiI6ImF2Q09EaUFUU2RyTmUyN3JMbEZRXC93PT0iLCJ2YWx1ZSI6IkxaZnY0RUNZOTF0ejB0bUw1eWZyZlVTTHdPUkxlMXVnazltK01BcFJDbWhWMUVqaXJJdTZINWFyRVhYdGdrQ3N0ODY3R3VVWWJPdm8reGdjelwvM3ludz09IiwibWFjIjoiNzM4ZjE5ZWRhOWUyZmRiYTQ2M2RiNzNiNjQ4ODg3ZTU0ZjlmMjJkYzFhZmY5NjBjM2FiMDI4MTQ2N2JmNTUxMCJ9; Hm_lpvt_2d2777148aa1618ef79baf55c005df84=1554874414',
    "pragma": "no-cache",
    "referer": "https://edu.hellobi.com/course/157/lessons",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}


def get_text(url):
    response = requests.get(url, headers=headers, verify=False)
    return response


def get_video_url(url):
    response = get_text(url).text
    soup = BeautifulSoup(response, 'lxml')
    video_urls = soup.select("#course-item-list a")
    for video_url in video_urls:
        yield video_url['href']


def download_video(url):
    driver = webdriver.Chrome(chrome_options=Option)
    driver.get('https://passport.hellobi.com/sso/login')
    driver.find_element_by_xpath('//*[@id="register_form"]/div[1]/input').send_keys('463230674@qq.com')
    driver.find_element_by_xpath('//*[@id="register_form"]/div[2]/input').send_keys('9+7=2bmq')
    driver.find_element_by_xpath('//*[@id="register_form"]/button[2]').click()
    dictcookie = driver.get_cookies()
    jsoncookie = json.dumps(dictcookie)
    with open("cookies.json", 'w') as f:
        f.write(jsoncookie)
    tag = 0
    for url1 in get_video_url(url):
        tag += 1
        if tag > 30:
            driver.get(url1)
            time.sleep(2)
            response = driver.page_source
            soup = BeautifulSoup(response, 'lxml')
            video_download_url = soup.select('#SewisePlayer0 .sewiseplayer-video video')[0]['src']
            title = soup.select('.course-title span')[0].text.split('/')[-1]
            filename = title+video_download_url.split('/')[-1]
            path = os.path.join('video', filename)
            content = requests.get(video_download_url, headers=headers1).content
            with open(path, 'wb') as f:
                f.write(content)
                f.close()
                print("%s下载成功" % filename)
        else:
            continue
                
if __name__ == "__main__":
    download_video(URL)





