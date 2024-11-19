# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class Eleven:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#
#     def open_browser(self):
#         self.driver.get("https://staging.d3hi9g2bzkelg7.amplifyapp.com/")
#         time.sleep(3)
#         print("Test 1 : Open Browser Success!")
#
#     def product(self):
#         self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div[1]/li[1]/a/div/h5").click()
#         time.sleep(3)
#         print("Test 2 : Product Click")
#         time.sleep(10)
#         print("Testing ")
#         self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/ul/li[1]/div[1]/h1").click()
#         time.sleep(30)
#     print("Test 4 : 7 - Select")
#
#     def main(self):
#         self.open_browser()
#         self.product()
#
# Eleven().main()
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ParaBank:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def setup(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        print("Test 1 : Open Page Success!")
        time.sleep(3)

    def register(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/p[2]/a").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.firstName").send_keys("AMS")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.lastName").send_keys("LTD")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.address.street").send_keys("Main Road")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.address.city").send_keys("Rangoon")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.address.state").send_keys("Yangon Region")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys("1111")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys("095069887")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.ssn").send_keys("12/AkAk003453")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.username").send_keys("AMS")
        time.sleep(2)
        self.driver.find_element(By.ID, "customer.password").send_keys("123456")
        time.sleep(2)
        self.driver.find_element(By.ID, "repeatedPassword").send_keys("123456", Keys.ENTER)

        time.sleep(3)
        print("Test 2 :  Register Success" )

    def login(self):
        self.driver.find_element(By.NAME, "username").send_keys("AMS")
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys("123456", Keys.ENTER)
        time.sleep(3)
        print("Test 3 : Login Success!")

    def account_overview(self):
        acc_number = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/a").text
        acc_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        acc_avail = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text
        acc_total = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/b").text

        print("Account Number :",acc_number )
        print("Account Balance :", acc_balance)
        print("Available Amount :", acc_avail)
        print("Total :",acc_total)
        print("="*30)

    def logout(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/ul/li[8]/a").click()
        time.sleep(2)
        print("Test 4 : Logout Success!" )

    def open_new_account(self):
        self.driver.find_element(By.LINK_TEXT, "Open New Account").click()
        time.sleep(2)
        print("Test 5 : Open New Account Success" )

    def main(self):
        self.setup()
        #self.register()
        self.login()
        self.account_overview()
        #self.logout()
        self.open_new_account()


ParaBank().main()