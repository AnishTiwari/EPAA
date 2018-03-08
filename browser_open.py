from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

#  'SETTING THE OPTIONS FOR CHROME WINDOWS'
chrome_options = Options()
#  'chrome_options.add_argument("--kiosk")'
chrome_options.add_argument("test-type")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--js-flags=--expose-gc")
chrome_options.add_argument("--enable-precise-memory-info")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("test-type=browser")
chrome_options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://localhost/srec/current/Index.html')  # 'opening the website;'
while 1:
    if os.path.isfile('C:/Users/home/Downloads/file.txt'):
        faculty = driver.execute_script("return document.getElementById('facname').value")
        department = driver.execute_script("return document.getElementById('dept').value")
        year = driver.execute_script("return document.getElementById('year').value")
        subject_name = driver.execute_script("return document.getElementById('SubName').value")
        newpath = os.path.join("C:/", faculty, department, year, subject_name)
        # print(newpath)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        f = open("C:/Users/home/Downloads/file.txt", 'w')
        f.write(newpath)
        print(newpath)
        f.close()
        exit()
        driver.close()
