import sys
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import requests
from bs4 import BeautifulSoup
import datetime
import urllib.request

# goish2468
GDriveJSON = 'WeatherRecord.json'
GSpreadSheet = 'https://docs.google.com/spreadsheets/d/1EHfk717lCx4Rwa9LsigflDxVnCKWUIUhCse7QPb8Gww/edit'

url  = 'https://taqm.epa.gov.tw/taqm/tw/AqiForecast.aspx'
html  = requests.get(url).text
soup = BeautifulSoup(html,'lxml')

# get date
date1 = soup.find('span',{'id':'ctl04_labDay1'})
d1 = date1.text

# get aqi
loc_aqi_1 = soup.find('td',{'id':'ctl04_tdPsi1_3_2'})
day1a=loc_aqi_1.text

quote_page = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taichung_City.htm'
page = urllib.request.urlopen(quote_page)
soup2 = BeautifulSoup(page,'html.parser')

name_box = soup2.find('tbody').find_all('tr')

data = []

for tr in name_box:
    counter = 0 
    for td in tr:
        if td.string != None:
            if(counter==1 or counter==3 or counter==8):
                data+=[td.string]
            counter = counter + 1


t1 = data[0]
h1 = data[1]
r1 = data[2]
t2 = data[3]
h2 = data[4]
r2 = data[5]
t3 = data[6]
h3 = data[7]
r3 = data[8]	



try:	
	scope = ['https://spreadsheets.google.com/feeds']	
	key = SAC.from_json_keyfile_name(GDriveJSON, scope)
	gc = gspread.authorize(key)
	worksheet = gc.open_by_url(GSpreadSheet).worksheet('工作表1')
	print('Success write in')
except Exception as ex:
	print('fail to write.', ex)
	sys.exit(1)
worksheet.append_row([str(datetime.datetime.now()),d1,day1a,t1,h1,r1,t2,h2,r2,t3,h3,r3])
print('add one row to sheet1' ,GSpreadSheet)
