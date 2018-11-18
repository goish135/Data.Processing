"# Data.Processing" 


| -- --    Value -- --    |

| --      JSON.png   --   |  train_value.json: 路段名、日期、時間、速率值

| --   ican_09230.py --   |  讀取多個動態路段資訊(.XML), 寫入同一JSON檔(train_value.json)

 讀取train.json(路段id,roadsection) → 依序讀取XML，檔案正常的話，擷取 datacollecttime:"資料收集時間"、value:"速率" ，發現額外路段(不在靜態資訊裡=>train.json) 也放入matchdata(dict) → 統計XML 總數(count_XML)，XML異常總數(xxml)，額外發現路段總數(fine)

| -- preprocess_v3.py  -- | 

| -- sorted_time.json

| -- sorted_time.png

| -- special_route - 複製.py

| -- special_route.py

| -- special_routev2.py

| -- 幾個data.PNG

| -- above is main  --     |



