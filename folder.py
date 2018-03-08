import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options)

faculty = driver.execute_script("return document.getElementById('facname').value")
department = driver.execute_script("return document.getElementById('dept').value")
year = driver.execute_script("return document.getElementById('year').value")
subject_name = driver.execute_script("return document.getElementById('SubName').value")
newpath = os.path.join("C:/",faculty,department,year,subject_name)
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)
