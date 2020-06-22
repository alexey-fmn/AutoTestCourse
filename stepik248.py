from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Firefox()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	price1 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

	click1 = browser.find_element_by_id ('book')
	click1.click()

	answer1 = browser.find_element_by_id ('input_value')
	m = answer1.text
	y = calc(m)
	print ('x = ', m)
	print ('y = ', y)

	input1 = browser.find_element_by_id ('answer')
	input1.send_keys(y)

	click2 = browser.find_element_by_id ('solve')
	click2.click()


finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(9)
	# закрываем браузер после всех манипуляций
	browser.quit()