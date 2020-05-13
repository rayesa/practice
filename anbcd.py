from selenium import webdriver
import time


class Orange():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/novro/PycharmProjects/Test/drivers/chromedriver.exe')

    def Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        self.driver.find_element_by_name("txtUsername").send_keys("admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(3)
    def AssignLeave(self):
        self.driver.find_element_by_xpath("//span[text()='Assign Leave']").click()
        self.driver.find_element_by_xpath("//h1[text()='Assign Leave']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//b[text()='Dashboard']").click()

    def Logout(self):
        self.driver.find_element_by_xpath("//a[text()='Welcome Admin']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[text()='Logout']").click()
O = Orange()
O.Login()

O.AssignLeave()
O.Logout()
