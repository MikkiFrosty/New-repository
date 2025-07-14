from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def test_search():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com/")
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "searchbox_input")))
    driver.find_element(By.ID, "searchbox_input").send_keys("ЫВАПРОЛkjlk", Keys.ENTER)
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "THG_yNtlhifBrJDatoUn")))
    element=driver.find_element(By.CLASS_NAME, "THG_yNtlhifBrJDatoUn")
    assert element.text=="По запросу «ЫВАПРОЛkjlk» ничего не найдено."