from os import link
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import requests
from bs4 import BeautifulSoup
import requests
from bs4.element import Tag, NavigableString

# デフォルト待機
# driver.implicitly_wait(10)


# --------------------エラーメッセージを消す--------
# options = Options()
# options.add_argument('--disable-logging')
# options.add_argument('--log-level=3')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# # ブラウザを開く
# driver = webdriver.Chrome(options=options)

# ChromeOptions = webdriver.ChromeOptions()
# ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
# time.sleep(3)
# ---------------------------------------------------


# -----googleを開く----------------------------------
driver = webdriver.Chrome()
driver.get("https://www.google.co.jp")
time.sleep(3)

# HTML取得
res = requests.get("https://google.co.jp/")
soup = BeautifulSoup(res.content, 'html.parser')

# ログインしないで使うボタンを押す
driver.find_elements_by_tag_bame('button')[0].click()

# アカウントログイン

# 検索条件を入力する欄を検索
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()
time.sleep(2)

# Mapを開く
driver.find_element_by_class_name('gb_Ue')[0].click()
time.sleep(2)

# リンク文字を取得して配列に格納
link_string = []
link_url = []
link_string.append([url.get('String') for url in soup.find_all('a')])
link_url.append([url.get('link') for url in soup.find_all('a')])
# ---------------------------------------------------


time.sleep(400)




# 閉じる
driver.quit()
