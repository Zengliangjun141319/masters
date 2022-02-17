from selenium import webdriver

class testPag():

    def one(self):
        self.driver = webdriver.Chrome()
        self.ex_url = self.driver.command_executor._url
        self.ssid = self.driver.session_id
        self.driver.get("http://www.baidu.com")

ex_url = testPag.ex_url
ssid = one.ssid
if __name__ == "__main__":
    testPag()




