"# Data.Processing" 


| -- --    Value -- --    |   directory 名稱                            | 

| --      JSON.png   --   |  train_value.json: 路段名、日期、時間、速率值 |

| --   ican_09230.py --   |  讀取多個動態路段資訊(.XML), 寫入同一JSON檔(train_value.json) |

 讀取train.json(路段id,roadsection) → 依序讀取XML，檔案正常的話，擷取 datacollecttime:"資料收集時間"、value:"速率" ，發現額外路段(不在靜態資訊裡=>train.json) 也放入matchdata(dict) → 統計XML 總數(count_XML)，XML異常總數(xxml)，額外發現路段總數(fine)

| -- preprocess_v3.py  -- |  依序讀XML 並記錄datacollecttime，寫入time.json |

| -- sorted_time.json  -- |  將time.json 排序的結果 |

| -- sorted_time.png   -- |  演進圖 : time.json(未排序) 到 sorted.json(以排序) |

| -- special_route - 複製.py -- | 從 train.json 擷取 某一段路段(ex:66000m3JE02), 並依排序後的時間，補缺失資料(找不到的情況即往後找)，並以路段id為檔名存成json檔 |


| -- special_route.py        -- | ignore ， 因為時間未排序 |

| -- special_routev2.py      -- | 讀取 time.json 並處理成已排序的時間:sorted_time.json |

| -- 幾個data.PNG            -- | 6611 個檔案 (大約兩個月) 實際用上6573個檔案 |

| -- above is main  --     |  



