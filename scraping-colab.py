from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome Driverにセットするオプションの設定。
# やっとかないとエラーになるよ！
options = webdriver.ChromeOptions()
options.add_argument('--headless') # ヘッドレスモードを有効にする。
options.add_argument('--no-sandbox') # sandboxモードを解除する。この記述がないとエラーになってしまう。
options.add_argument('--disable-dev-shm-usage') # /dev/shmパーティションの使用を禁止し、パーティションが小さすぎることによる、クラッシュを回避する。

# Webドライバーをセット
driver = webdriver.Chrome('chromedriver',options=options)

# ターゲットURL
URL = "https://www.teijitaisya.com/"

# URLにpostしてページ情報を取得する
driver.get(URL)

#暗黙の待機（秒）
driver.implicitly_wait(10)




# -------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get(URL)

# ページ内のすべての要素が読み込まれるまで待機します。10秒たったらタイムアウトにします。
element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located
)

# visibility_of_element_located	指定した要素の表示される
# text_to_be_present_in_element	指定したテキストが表示される
# presence_of_all_elements_located	ページ内のすべての要素が読み込まれる
# presence_of_element_located	DOM要素内に指定した要素が現れる
# alert_is_present	Alertが表示される
# element_to_be_clickable	要素がクリック出来る状態になる
# ---------------------------------------

# タグ名で要素を取得する。
results = driver.find_elements(By.TAG_NAME,"a")

# By.CLASS_NAME
# クラス属性	#p-postList__titleというクラス名の要素を取得します。
# results = driver.find_elements(By.CLASS_NAME, “p-postList__title”)

# By.TAG_NAME
# タグ名	#aタグをすべて取得します。
# results = driver.find_elements(By.TAG_NAME,”a”)

# By.NAME
# name属性	username = driver.find_elements(By.NAME,”username”)
# password = driver.find_elements(By.NAME,”password”)

# By.ID
# 	id属性	results = driver.find_elements(By.ID,”username”)
# By.LINK_TEXT	リンクテキスト	results = driver.find_elements(By.LINK_TEXT,”詳細ページはこちらです”)
# By.PARTICAL_LINK_TEXT	リンクテキストに含まれる一部の文字列	results = driver.find_elements(By.PARTICAL_LINK_TEXT,”詳細ページ”)
# By.XPATH	XPATH	login_form = driver.find_element_by_xpath(“/html/body/form[1]”)
# または、
# login_form = driver.find_element_by_xpath(“//form[1]”)
# By.CSS_SELECTOR	CSSセレクタ	results = driver.find_elements(By.CSS_SELECTOR,”p.content”)
