import os
import requests
from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://consensus.hankyung.com/apps.analysis/analysis.list?&sdate=2020-09-26&edate=2020-10-26&report_type=CO&pagenum=80&order_type=10010000&now_page=1"

#If there is no such folder, the script will create one automatically
folder_location = r'/Users/BrandenKang/Desktop/reports_summary'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# for link in soup.select("a[href$='pdf']"):
#     print('hello')
# #Name the pdf files using the last portion of each link which are unique in this case
#     filename = os.path.join(folder_location,link['href'].split('/')[-1])
#     with open(filename, 'wb') as f:
#         f.write(requests.get(urljoin(url,link['href'])).content)

