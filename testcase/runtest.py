from HTMLTestRunner import HTMLTestRunner
import time
import unittest, sys
sys.path.append("./email_report")
from email_report.send_mail_latest_report import new_report
from email_report.send_mail_latest_report import send_mail

'''
def addcookies(driver):
	driver.add_cookie({'name':'BAIDUID', 'value':'405A85F15C1B5C542971B7F88DDB14F4:FG=1'})
	driver.add_cookie({'name':'BDUSS', 'value':'XdRMTZibFgxdmJ3WTNKc2liWmd5ZHktemg2WXF3dURZcjZ3emlPOGplLUhnTWxhQUFBQUFBJCQAAAAAAAAAAAEAAADzaBdzv8mwrrXER2lnMTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIfzoVqH86Fae'})
	#sleep(10)
	driver.refresh()
'''


if __name__ == '__main__':
	#unittest.main()
	'''
	testunit=unittest.TestSuite()
	testunit.addTest(Casebaiduyun("test_login"))
	
	testunit.addTest(Casebaiduyun("test_add_newgroup"))
	
	testunit.addTest(Casebaiduyun("test_add_newcontact"))
	testunit.addTest(Casebaiduyun("test_delete_group"))
	testunit.addTest(Casebaiduyun("test_delete_allcontact"))
	testunit.addTest(Casebaiduyun("test_customnavgition"))	
	testunit.addTest(Baiduaccountlogin("test_baidulogin1"))
	testunit.addTest(Baiduaccountlogin("test_baidulogin2"))
	testunit.addTest(Baiduaccountlogin("test_baidulogin3"))
	testunit.addTest(Baiduaccountlogin("test_baidulogin4"))
	testunit.addTest(Cloudaccountlogin("test_uclogin1"))
	testunit.addTest(Cloudaccountlogin("test_uclogin2"))
	testunit.addTest(Cloudaccountlogin("test_uclogin3"))
	testunit.addTest(Cloudaccountlogin("test_uclogin4"))
	'''

	now=time.strftime("%Y-%m-%d %H_%M_%S")
	TestResult_dir='./TestReport/'
	filename=TestResult_dir+now+'_result.html'
	fp=open(filename,'wb')
	runner=HTMLTestRunner(stream=fp, title='测试报告',description='用例执行情况：')
	discover=unittest.defaultTestLoader.discover('./', pattern='test_*.py')
	runner.run(discover)
	fp.close()
	new_report=new_report(TestResult_dir)
	send_mail(new_report)
