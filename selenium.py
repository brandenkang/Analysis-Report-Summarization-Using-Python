from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/Users/BrandenKang/Desktop/reports_summary/chromedriver')
driver.get("http://consensus.hankyung.com/apps.analysis/analysis.list?&sdate=2020-09-26&edate=2020-10-26&report_type=CO&pagenum=80&order_type=10010000&now_page=1")

driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr[1]/td[9]/div/a/img').text


