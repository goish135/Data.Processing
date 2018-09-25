# main
1. auto_dowload_upload.py: 自動下載和上傳至雲端備份

# Google API 
2. client_secrets.json: 憑證
3. settings.yaml: 自動驗證

# 部署程式至heroku
4. clock.py 
每五分鐘執行auto_dowload_upload.py
5. Procfile: 啟動定時程式
clock: python clock.py
6. requirement.txt
告訴Heroku該 下載那些Python套件

 


 