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
# driver = webdriver.Chrome()
# driver.get("https://www.google.co.jp")
# time.sleep(3)

# # HTML取得
# res = requests.get("https://google.co.jp/")
# soup = BeautifulSoup(res.content, 'html.parser')

# # ログインしないで使うボタンを押す
# driver.find_elements_by_tag_bame('button')[0].click()

# # アカウントログイン

# # 検索条件を入力する欄を検索
# search_bar = driver.find_element_by_name("q")
# search_bar.send_keys("python")
# search_bar.submit()
# time.sleep(2)

# # Mapを開く
# driver.find_element_by_class_name('gb_Ue')[0].click()
# time.sleep(2)

# # リンク文字を取得して配列に格納
# link_string = []
# link_url = []
# link_string.append([url.get('String') for url in soup.find_all('a')])
# link_url.append([url.get('link') for url in soup.find_all('a')])
# ---------------------------------------------------


# -----test スクレイピング---------------------------
driver = webdriver.Chrome()
driver.get("https://saigai.gsi.go.jp/jusho/download/")
time.sleep(3)

# HTML取得
res = requests.get("https://saigai.gsi.go.jp/jusho/download/")
soup = BeautifulSoup(res.content, 'html.parser')

# 都道府県を取得して配列に格納
tofuken = []
def parse_li(li):
  for child in "li":
    if type(child) == NavigableString:
      tofuken.append(child.string)
    elif type(child) == Tag:
    # リスト構造ではない child のみ返り値に含める
      if child.find_all('li') == []:
        tofuken.append(child.get_text())
  return ''.join(tofuken)

# 各都道府県を押してデータ取ってくるループ
for i in range(len(tofuken)):
  try:
    city = driver.find_element_by_link_text(tofuken[i])
    city.click()

  except:
    pass

time.sleep(3)
# ---------------------------------------------------


time.sleep(400)




# 閉じる
driver.quit()
