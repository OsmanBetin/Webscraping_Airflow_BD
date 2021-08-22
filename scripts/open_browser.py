from selenium import webdriver
import os
from functions import generate_full_path

cur_dir = os.getcwd()
dir_base = 'Webscraping_Airflow_BD'
dir_driver = 'SeleniumDriver'
driver_name = 'chromedriver'

full_path_driver = generate_full_path(cur_dir, dir_base, dir_driver)
full_path_driver = full_path_driver + '/' + driver_name
print(full_path_driver)




driver = webdriver.Chrome(full_path_driver)
driver.get('https://www.baloto.com/resultados/')