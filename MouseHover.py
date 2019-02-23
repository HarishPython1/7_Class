from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("file:///C:/Users/QSP/Desktop/webtable.html")
driver.maximize_window()
driver.implicitly_wait(30)
ele = driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print(len(ele))
first_part="//*[@id='emp']/thead/tr/th["
second_part="]"




