# dowloading 台中市路段動態資訊 to Google Drive(goish2468) 儲存備份 

import os

# 台中市路段動態資訊 下載網址
dowload_url = "http://opendata.taichung.gov.tw/dataset/376abc42-0b99-4bf9-862b-276d71965d77/download_all_resources"

# 以現在時間命名檔案名稱
import time
format_time = time.strftime("%Y-%m-%d %H.%M.%S",time.localtime())
fn = format_time+'.zip' 					# filename


# 下載檔案
import urllib.request
urllib.request.urlretrieve(dowload_url,fn) 
print('download complete...')


# 上傳檔案
from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth() 					# Creates local webserver and auto handles authentication.
from pydrive.drive import GoogleDrive
drive = GoogleDrive(gauth)
file = drive.CreateFile({'title': fn})  	# Create GoogleDriveFile instance .
file.SetContentFile(fn) 					# Set content of the file from given string.
file.Upload()
print('Upload OK')
               

