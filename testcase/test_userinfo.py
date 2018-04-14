from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
import unittest, sys
sys.path.append("./page_obj")
sys.path.append("./models")
from models import myunit
from page_obj.Login import LoginPage
from page_obj.usercenter import useraccountcenter
from page_obj.usercenter import newgroup
from page_obj.overview_page import Overviewpage
from page_obj.overview_page import goto_customnavigition
from page_obj.user_login import test_cloudaccount_login
from page_obj.user_login import test_user_login
from page_obj.usercenter_group_contact import goto_usercenter
from page_obj.usercenter_group_contact import add_new_contact
from page_obj.usercenter_group_contact import add_new_group
from page_obj.usercenter_group_contact import delete_all_group
from page_obj.usercenter_group_contact import delete_all_contacts
from page_obj.ticket import goto_ticketlist
from page_obj.ticket import goto_createticket
from screenshot import get_screenshot


class Baiduaccountlogin(myunit.MyTest):


	def test_baidulogin1(self):
		test_user_login(self.driver,self.login_url, username="", password="")
		sleep(1)
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.baiduaccountlogin_error_hint(), u"请您输入手机/邮箱/用户名")
		get_screenshot(self.driver, "test_baidulogin1")

	def test_baidulogin2(self):
		test_user_login(self.driver,self.login_url, username="15900443703", password="")
		sleep(1)
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.baiduaccountlogin_error_hint(), u"请您输入密码")
		get_screenshot(self.driver, "test_baidulogin2")

	def test_baidulogin3(self):
		test_user_login(self.driver,self.login_url, username="1", password="1")
		sleep(1)
		get_screenshot(self.driver, "test_baidulogin3")
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.baiduaccountlogin_error_hint(), u"请输入验证码")

	def test_baidulogin4(self):
		test_user_login(self.driver,self.login_url, username="15900446666", password="123456789")
		sleep(1)
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.baiduaccountlogin_error_hint(), u"用户名或密码有误，请重新输入或找回密码")
		get_screenshot(self.driver, "test_baidulogin4")

	#def tearDown(self):
	#	self.driver.close()



class Cloudaccountlogin(myunit.MyTest):

	def test_uclogin1(self):
		test_cloudaccount_login(self.driver,self.login_url, username="", password="", token="")
		sleep(1)
		get_screenshot(self.driver,"test_uclogin1")
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.uclogin_username_error_hint(), u"用户名不能为空")
		self.assertEqual(login_page.uclogin_password_error_hint(), u"密码不能为空")
		self.assertEqual(login_page.uclogin_token_error_hint(), u"验证码不能为空")

	def test_uclogin2(self):
		test_cloudaccount_login(self.driver,self.login_url, username="15900443703", password="", token="")
		sleep(1)
		get_screenshot(self.driver,"test_uclogin2")
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.uclogin_password_error_hint(), u"密码不能为空")
		self.assertEqual(login_page.uclogin_token_error_hint(), u"验证码不能为空")

	def test_uclogin3(self):
		test_cloudaccount_login(self.driver,self.login_url, username="15900443703", password="123456", token="")
		sleep(1)
		get_screenshot(self.driver,"test_uclogin3")
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.uclogin_token_error_hint(), u"验证码不能为空")

	def test_uclogin4(self):
		test_cloudaccount_login(self.driver,self.login_url, username="15900443703", password="123456", token="1234")
		sleep(1)
		get_screenshot(self.driver,"test_uclogin4")
		login_page=LoginPage(self.driver,u"baidu", u"baidu Cloud")
		self.assertEqual(login_page.uclogin_token_error_hint(), u"验证码错误")


class Casebaiduyun(myunit.MyTest):

	#def setUp(self):
	#	self.driver=webdriver.Chrome()
	#	self.driver.implicitly_wait(20)
	#	self.driver.maximize_window()
		#self.driver.set_window_size(800,800)

	def test_login(self):
		try:
			
			#login_url="https://www.baidu.com"
			test_user_login(self.driver, self.login_url, self.username, self.password)
			sleep(5)
			result=self.driver.find_element_by_class_name("username").is_displayed()
			#print(result)
			self.assertTrue(result, "failed to login")
			#goto_createticket(self.driver)
			#self.driver.get_screenshot_as_file("C:\\Gigi\\baiduyun\\TestScript\\screenshot\\baidu_img.jpg")
			
			#above=self.driver.find_element_by_class_name("username")
			#ActionChains(self.driver).move_to_element(above).perform()
			#above.click()
			
		finally:
			self.driver.close()


	def test_customnavgition(self):
		try:
			test_user_login(self.driver, self.login_url, self.username, self.password)
			sleep(5)
			goto_customnavigition(self.driver)

		finally:
			self.driver.close()

	def test_add_newgroup(self):
		try:
			test_user_login(self.driver, self.login_url, self.username, self.password)
			sleep(5)
			goto_usercenter(self.driver)
			sleep(5)
			delete_all_group(self.driver)
			add_new_group(self.driver, self.newprovidename)

		finally:
			self.driver.close()

	def test_add_newcontact(self):
		try:
			test_user_login(self.driver, self.login_url, self.username, self.password)
			goto_usercenter(self.driver)
			sleep(5)
			#delete_all_contacts(self.driver)

			add_new_contact(self.driver,self.newcontactname, self.newcontactphone, self.newprovidename)
		finally:
			self.driver.close()

	def test_delete_group(self):
		try:
			test_user_login(self.driver, self.login_url, self.username, self.password)
			goto_usercenter(self.driver)
			sleep(5)
			delete_all_group(self.driver)

			#result=self.driver.find_element_by_class_name("ui-table-body-nodata").is_displayed()
			#text=self.driver.find_element_by_class_name("ui-table-body-nodata").text
			#self.assertTrue(result, u"%s is not displayed"%text)
		finally:
			self.driver.close()

	def test_delete_allcontact(self):
		#contactpage_nodata_loc=(By.CLASS_NAME, "ui-table-body-nodata")
		try:
			test_user_login(self.driver, self.login_url, self.username, self.password)
			goto_usercenter(self.driver)
			sleep(5)
			delete_all_contacts(self.driver)
			#result=self.driver.find_element(*self.contactpage_nodata_loc).is_displayed()
			#text=self.driver.find_element(*self.contactpage_nodata_loc).text
			#result=self.driver.find_element_by_class_name("ui-table-body-nodata").is_displayed()
			#text=self.driver.find_element_by_class_name("ui-table-body-nodata").text
			#self.assertTrue(result, u"%s is not displayed"%text)
		finally:
			self.driver.close()


if __name__ == '__main__':
	unittest.main()