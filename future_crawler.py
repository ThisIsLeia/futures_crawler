# 按照輸入天數下載期交所檔案

# 還沒做好 main.py
# from main import crawler_manager
# target = crawler_manager.get_crawler('future')
# target.result()

from selenium import webdriver
import time
import os
import sys


def wait_for_downloads():
    print("Waiting for downloads", end="")
    while any([filename.endswith(".crdownload") for filename in
               os.listdir('C:/Users/88698/downloads')]):
        time.sleep(2)
        print(".", end="")
    print("done!")


def crawler(path, day):
    '''輸入要下載的天數 將載入最近x開盤日的資料'''
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0,
             'download.default_directory': 'Downloads'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(
        executable_path='D:/Course/python/chromedriver_win32/chromedriver.exe', chrome_options=options)
    driver.get(path)
    day = int(day) + 2
    for i in range(2, day):
        target = '/html/body/div[1]/div[4]/div[2]/div/div[2]/table[2]/tbody/tr[' + str(
            i) + ']/td[4]/input'
        driver.find_element('xpath', target).click()
        time.sleep(1)
    wait_for_downloads()
    driver.quit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        day = sys.argv[1]  # python3 檔名.py [下載天數]
        path = 'https://www.taifex.com.tw/cht/3/dlFutPrevious30DaysSalesData'
        crawler(path, day)
        print('success!')
    else:
        print('請在入口輸入欲下載天數')  # 印出可選擇標的

