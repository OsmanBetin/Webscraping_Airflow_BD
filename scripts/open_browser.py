from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import os
from functions import generate_full_path, click_on_bal_revancha
from read_config import get_value_config
import time

cur_dir = os.getcwd()
dir_base = 'Webscraping_Airflow_BD'
dir_driver = 'SeleniumDriver'
driver_name = 'chromedriver'

# Get the full path Config file
full_path_driver = generate_full_path(cur_dir, dir_base, dir_driver)
full_path_driver = full_path_driver + '/' + driver_name
print(full_path_driver)

# Get the URL - max retires - time out
url = get_value_config('web_page')
max_retries = get_value_config('max_retries')
time_out = get_value_config('time_out_short')
# Get the options to Select: Baloto or Revancha options
revancha_pop = get_value_config('revancha_popup')
baloto_pop = get_value_config('baloto_popup')
# driver = webdriver.Chrome(full_path_driver)
# driver.get('https://www.baloto.com/resultados/')

retry = 0
while retry < max_retries:
    driver = webdriver.Chrome(full_path_driver)
    driver.get(url)
    time.sleep(time_out)
    try:
        # Get the string proximo sorteo
        element = driver.find_elements_by_id('date_timer')
        text = element[0].text
    except Exception as e:
        text = ''

    if len(text) > 0:
        print('Web page already charged')
        print('Next game: ', text)

        click_on_bal_revancha(driver, revancha_pop)
        time.sleep(10)
        click_on_bal_revancha(driver, baloto_pop)

        retry = max_retries
    else:
        print(f'Web page is Not ready! Retry number {retry}')
        driver.close()
        retry += 1
