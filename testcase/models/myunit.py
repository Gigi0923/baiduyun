from selenium import webdriver
import unittest
import os
class MyTest(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.login_url="https://login.bce.baidu.com/"
		self.username=""
		self.password=""
		self.login_url="https://login.bce.baidu.com/"
		self.newprovidename="gr4"
		self.newcontactname="Gi8"
		self.newcontactphone=""
		self.admin_username=""

	def tearDown(self):
		self.driver.quit()
