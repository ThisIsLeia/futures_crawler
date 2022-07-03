# 解壓縮到指定資料夾
# 篩選及合併所需資料

import os
import pandas as pd
import zipfile
import glob

unzip_target = 'C:/Users/88698/Downloads/*.zip'
for name in glob.glob(unzip_target):
    print(name)
    unZip = zipfile.ZipFile(name)
    unZip.extractall('data')
unZip.close()

# 要處理的檔案路徑
Folder_Path = 'D:/Course/python/strategies/crawler/data'
# 處理後存檔的路徑
SaveFile_Path = 'D:/Course/python/strategies/crawler/tidied'
# 拚接後要保存的檔案名
SaveFile_Name = 'taiwanfuture_all_TX.csv'
# 選取所需資料
Column_Product_Select = 'TX     '
# Due_Select = '202208'
# 修改目前工作目錄
os.chdir(Folder_Path)
# 將該資料夾下的所有檔案名存入一個列表
file_list = os.listdir()
print(Folder_Path + '/' + file_list[0])

# 讀取第一個CSV檔案並包含表頭
# 編碼預設UTF-8，為讀取中文更改為 GB18030
# 合約當月的第三個禮拜的週三 為近月合約
df = pd.read_csv(Folder_Path + '/' + file_list[0], encoding="GB18030", low_memory=False)
df.columns = ['Date', 'Product', 'DueMonth', 'Time',
              'Price', 'Volume', 'NearMPrice', 'FarMPrice', 'OpenEx']
# 選取台指期的row
df = df.loc[df['Product'] == Column_Product_Select]
# 選取目標到期日的row
# df = df.loc[(df['DueMonth']) == Due_Select]

# 刪除不會用到的直行
df = df.drop(['Volume', 'NearMPrice', 'FarMPrice', 'OpenEx'], axis=1)
# 將讀取的第一個CSV檔案寫入合併後的檔案保存
df.to_csv(SaveFile_Path+'/' + SaveFile_Name, encoding="GB18030", index=False)

# 遞迴瀏覽列表中的各個CSV檔案名，並追加到合併後的檔案
for i in range(1, len(file_list)):
        df = pd.read_csv(Folder_Path + '/' + file_list[i], encoding="GB18030", low_memory=False)
        df.columns = ['Date', 'Product', 'DueMonth', 'Time',
                      'Price', 'Volume', 'NearMPrice', 'FarMPrice', 'OpenEx']
        df = df.loc[df['Product'] == Column_Product_Select]
        # df = df.loc[df['DueMonth'] == Due_Select]
        # df = df.drop(['Volume', 'NearMPrice', 'FarMPrice', 'OpenEx'], axis=1)
        df.to_csv(SaveFile_Path+'/' + SaveFile_Name, encoding="GB18030",
                  index=False, header=False, mode='a+')
