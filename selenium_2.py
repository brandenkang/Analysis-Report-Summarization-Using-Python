import pandas as pd
import psycopg2 as pg2 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DB_HOST = "businessreport.cukht8dyquli.ap-northeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "AnserTech"
DB_PASSWORD = "Anser!1234#"
DB_PORT = "5432"
download_dir = 'C:\pdf'
options = Options()
options.add_experimental_option('prefs',{
    "download.default_directory" : download_dir,
    "download.prompt_for_download" : False,
    "download.directory_upgrade" : True,
    "plugins.always_open_pdf_externally" : True
})
conn = pg2.connect("host = {} dbname={} user={} password={} port={}".format(DB_HOST , DB_NAME , DB_USER , DB_PASSWORD ,DB_PORT))
cur = conn.cursor()
conn.autocommit = True
driver = webdriver.Chrome('/Users/BrandenKang/Desktop/reports_summary/chromedriver' , options = options)
cur.execute("select link from analyst where id > 1 and id < 10")
for (link, ) in cur.fetchall():
    try:
        driver.get(link)
        time.sleep(0.5)
    except:
        print(link)