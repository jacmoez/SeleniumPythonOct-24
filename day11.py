import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Relc():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_browser(self):
        self.driver.get("https://hotel-qa.gtriip.com/relc/guest/home/")
        time.sleep(1)

    def check_in_login(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.ID, "id_reservation_no").send_keys("100955")
        self.driver.find_element(By.ID, "id_check_in_date").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[5]/td[2]").click()
        self.driver.find_element(By.ID, "btn-step-next").click()

    def session_case(self):
        self.driver.find_element(By.CSS_SELECTOR, ".label-thumbnail").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "btn-ok").click()

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".pb-4 > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn-upload:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .file-upload").send_keys(
            "/Users/user/Downloads/Telegram Desktop/sla_passport.jpg")
        self.driver.find_element(By.ID, "btn-next").click()
        self.driver.find_element(By.ID, "btn-save").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()
        self.driver.find_element(By.ID, "canvas-signature").click()
        self.driver.find_element(By.ID, "btn-next").click()
        self.driver.find_element(By.ID, "id_email").send_keys("soelinaung165346@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) .check-icon").click()
        self.driver.find_element(By.CSS_SELECTOR, "#terms-conditions .check-icon").click()
        self.driver.find_element(By.ID, "btn-submit").click()
        time.sleep(5)
        print("Registration Successfully")

    def proceed_to_check_in(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/form/div[4]/div/button").click()
        time.sleep(3)

    def check_in_complete(self):
        time.sleep(5)
        print(1)

        # self.driver.find_element(By.XPATH, "/html/body/div/form/span[2]/div/div/div[2]/span/input")
        # print(self.driver.find_element(By.XPATH, "/html/body/div/form/span[2]/div/div/div[2]/span/input"))
        #.send_keys("4242 4242 4242 4242 4240"))
        self.driver.find_element(By.XPATH, "/html/body/div/form/span[2]/div/div/div[2]/span/input").send_keys("23456767")
        time.sleep(3)
        self.driver.find_element(By.NAME, "exp-date").send_keys("03 / 30")
        self.driver.find_element(By.NAME, "cvc").send_keys("737")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)




    def main(self):
        self.open_browser()
        self.check_in_login()
        self.session_case()
        #self.register()
        self.proceed_to_check_in()
        self.check_in_complete()


Relc().main()