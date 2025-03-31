from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
URL     = "http://127.0.0.1:4723"
driver  = webdriver.Remote(URL, options=options)

def login_one():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]').click()
    view_elements = driver.find_elements(AppiumBy.XPATH, '//android.view.View')
    # for view in view_elements:
    #     print(view.get_attribute("content-desc"))
    print(view_elements[6].get_attribute("content-desc"))
    print(view_elements[7].get_attribute("content-desc"))

def login_two():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    element.click()
    element.send_keys("qwert")
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]').click()
    view_elements = driver.find_elements(AppiumBy.XPATH, '//android.view.View')
    # for view in view_elements:
    #      print(view.get_attribute("content-desc"))
    print(view_elements[6].get_attribute("content-desc"))
    # print(view_elements[7].get_attribute("content-desc"))

def login_three():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    element.click()
    element.send_keys("qwert")
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]').click()
    view_elements = driver.find_elements(AppiumBy.XPATH, '//android.view.View')
    # for view in view_elements:
    #      print(view.get_attribute("content-desc"))
    print(view_elements[6].get_attribute("content-desc"))
    # print(view_elements[7].get_attribute("content-desc"))

def login_four():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    element.click()
    element.send_keys("qwert")
    time.sleep(2)
    element = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    element.click()
    element.send_keys("123456")
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]').click()


def Select_Box_One():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Select Box Demo").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Select a fruit").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Orange").click()

def Select_Box_Two():
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys("Ger")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "🇩🇪\nGermany\nDE").click()

def Select_Box_Two_scroll():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Select Box Demo").click()
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View')
    width = element.size["width"]
    height = element.size["height"]
    start_x = width / 2
    start_y = height * 0.8
    end_x = width / 2
    end_y = height * 0.2

    actions = ActionChains(driver)
    actions.move_to_element_with_offset(element, 0, start_y - height / 2)
    actions.click_and_hold()
    actions.move_by_offset(0, end_y - start_y)
    actions.release()
    actions.perform()


# login_one()
# login_two()
# login_three()
# login_four()
# Select_Box_One()
# Select_Box_Two()
Select_Box_Two_scroll()


