from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('/home/osmanfernandez/ProjectsBal/Webscraping_Airflow_BD/SeleniumDriver/chromedriver')
driver.get('https://www.baloto.com/resultados/')

# Selecting Baloto or Revancha options
revancha = 'revancha_popup'
baloto = 'baloto_popup'


def click_on_bal_revancha(driver, option):
    driver.execute_script(f'document.querySelector("#{option}").click();')

time.sleep(5)
click_on_bal_revancha(driver, revancha)
# revancha = driver.find_element_by_xpath('//*[@id="revancha_popup"]')
# driver.execute_script(f'document.querySelector("#{revancha}").click();')


time.sleep(20)
click_on_bal_revancha(driver, baloto)
# revancha = driver.find_element_by_xpath('//*[@id="baloto_popup"]')
# driver.execute_script(f'document.querySelector("#{baloto}").click();')
