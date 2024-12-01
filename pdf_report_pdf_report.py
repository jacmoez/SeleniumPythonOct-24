from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import time


class PDFReport:

    def __init__(self):
        self.results = []

    def add_test_result(self, test, msg):
        self.results.append([test, msg])

    def save_pdf(self, pdf_file="report.pdf"):

        doc = SimpleDocTemplate(pdf_file, pagesize=A4)
        elements = []
        data = [["Test", "Result"]] + self.results
        table = Table(data)

        style = TableStyle([
            ("GRID",(0,0),(-1,-1), 1, colors.black)
        ])
        table.setStyle(style)
        elements.append(table)
        doc.build(elements)


pdf_report = PDFReport()


class TestSwagTest:
    driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://www.saucedemo.com/")
        pdf_report.add_test_result("Test 1:"," Open browser Success")

    def test_login_test(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")

        self.driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.ENTER)
        pdf_report.add_test_result("Test 2:"," Login Success")

    def test_check_page_go(self):
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url

        assert expected_url == actual_url
        assert  "Swag Labs" in self.driver.title
        pdf_report.add_test_result("Test 3: ", "verify Success")

    def test_add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        self.driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()

        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        pdf_report.add_test_result("Test 4 :"," Add Item to Cart")

    def test_remove_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        pdf_report.add_test_result("Test 5 :"," Remove 1 item")

    def test_view_order_item(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        pdf_report.add_test_result("Test 6 :"," View Order Item")

    def test_check_cart_page_go(self):
        ps = self.driver.page_source

        pdf_report.add_test_result("Test 7 :"," Cart Page Arrived " if "Your Cart" in ps else "Wrong Page!")

    def test_remove_item_from_cart(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-onesie").click()

        pdf_report.add_test_result("Test 8:"," Remove item from cart - Cart Page")

    def test_check_out(self):
        self.driver.find_element(By.ID, "checkout").click()
        pdf_report.add_test_result("Test 9 :"," Click Check Out Button")

    def test_check_checkout_page_go(self):
        ps = self.driver.page_source

        pdf_report.add_test_result("Test 10 :"," Checkout Page Arrived " if "Checkout: Your Information" in ps else "Wrong Page!")

    def test_check_out_information(self):
        self.driver.find_element(By.ID, "first-name").send_keys("QA")

        self.driver.find_element(By.ID, "last-name").send_keys("Testing")

        self.driver.find_element(By.ID, "postal-code").send_keys("11111")

        self.driver.find_element(By.ID, "continue").click()
        pdf_report.add_test_result("Test 11 :"," Checkout Continue Success!")

    def test_check_payment(self):
        item_total = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax_total = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        pdf_report.add_test_result("Item Total : ", item_total)
        pdf_report.add_test_result("Tax Price : ", tax_total)
        pdf_report.add_test_result("Total Price : ", total_price)
        pdf_report.add_test_result("Test 12 : ","Payment Success!")

    def test_finish(self):
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        ps = self.driver.page_source
        pdf_report.add_test_result("Test 13 :"," Finish Page Arrived " if "Thank you for your order!" in ps else "Wrong Page!")

    def main(self):
        self.test_open_browser()
        self.test_login_test()
        self.test_check_page_go()
        self.test_add_to_cart()
        self.test_remove_item()
        self.test_view_order_item()
        self.test_check_cart_page_go()
        self.test_remove_item_from_cart()
        self.test_check_out()
        self.test_check_checkout_page_go()
        self.test_check_out_information()
        self.test_check_payment()
        self.test_finish()
        pdf_report.save_pdf()


TestSwagTest().main()
