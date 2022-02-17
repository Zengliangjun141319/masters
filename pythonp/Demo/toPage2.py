from selenium import webdriver
from ReuseChrome import ReuseChrome
from testPag import ex_url,ssid

driver2 = ReuseChrome(command_executor=ex_url, session_id=ssid)
driver2.get("http://www.sina.com.cn")
driver2.implicitly_wait(10)
driver2.close()