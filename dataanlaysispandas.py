import matplotlib as plt
import os.path
import pandas as pd
from selenium import webdriver
import glob
from selenium.webdriver.chrome.options import Options
import numpy as np

chrome_options = Options()
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("test-type")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--js-flags=--expose-gc")
chrome_options.add_argument("--enable-precise-memory-info")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("test-type=browser")
chrome_options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('file:///C:/xampp/htdocs/srec/current/Index.html')  # 'opening the website;'


while 1:
    if os.path.isfile('C:/Users/admin/Downloads/file.txt'):
        faculty = driver.execute_script("return document.getElementById('facname').value")
        department = driver.execute_script("return document.getElementById('dept').value")
        year = driver.execute_script("return document.getElementById('year').value")
        subject_name = driver.execute_script("return document.getElementById('SubName').value")
        newpath = os.path.join("C:/",faculty,department,year,subject_name)

        if not os.path.exists(newpath):
            os.makedirs(newpath)
        for f in glob.glob("C:/Users/admin/Downloads/file.txt"):
            os.remove(f)
            

    if os.path.isfile('/home/ujjwalaryal/Downloads/go.txt'):
        path = r'/home/ujjwalaryal/Downloads'  # use your path
        allFiles = glob.glob(path + "/*.csv")
        df = pd.DataFrame()
        list_ = []
        for file_ in allFiles:
            df = pd.read_csv(file_, index_col=None)
            list_.append(df)
        df = pd.concat(list_)
        df = df[
            ['NO', 'NAME', 'ROLLNO', 'QN1', 'QN2', 'QN3', 'QN4', 'QN5', 'QN6', 'QN7', 'QN8', 'QN9', 'QN10', 'QN11a',
             'QN11b',
             'QN12a', 'QN12b', 'QN13a', 'QN13b', 'TOTAL', 'PERCENT', 'RESULT']]
        summa = df
        new_header = summa.iloc[0]  # grab the first row for the header
        summa = summa[1:]  # take the data less the header row
        summa.columns = new_header  # set the header row as the summa header
        orgco = summa.iloc[2:]
        orgcovalue = orgco.groupby(orgco.columns, axis=1).sum()
        orgcovalue = orgcovalue.reset_index()
        orgcovalue['index'] = orgcovalue.index + 3
        df = df.reset_index()
        df['index'] = df.index
        new = df.set_index('index').join(orgcovalue.set_index('index'))
        summa = df
        new_header = summa.iloc[1]
        summa = summa[3:]  # getting rows for cl's
        summa.columns = new_header
        orgcl = summa
        orgclvalue = orgcl.groupby(orgcl.columns, axis=1).sum()
        orgclvalue = orgclvalue.reset_index()
        del orgclvalue[1]
        old = df.set_index('index').join(orgclvalue.set_index('index'))
        answer = new.merge(old)
        col_list = list(answer)
        col_list.remove('ROLLNO')
        col_list.remove('NAME')
        col_list.remove('NO')
        col_list.remove('RESULT')
        answer.loc['Column_Total'] = answer[col_list].sum(axis=0)
        answer.to_csv('/home/ujjwalaryal/Desktop/srec_project/result/last.csv')

