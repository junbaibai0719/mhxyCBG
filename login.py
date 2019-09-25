from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import json

def write_cookies(cookies):
	with open('cookie.py','w') as f:
		f.writelines(json.dumps(cookies))


def login(loginurl,username,passwd):
	b = webdriver.Chrome()
	b.get(loginurl)

	#定位到frame
	iframe = b.find_elements_by_tag_name("iframe")[0]
	b.switch_to_frame(iframe)
	#输入账户密码登录
	b.find_element_by_name('email').send_keys(username)
	b.find_element_by_name('password').send_keys(passwd)
	b.find_element_by_id('dologin').click()
	# WebDriverWait(b, 10).until(lambda b: b.find_element_by_id('login_btn'))
	try:
		WebDriverWait(b, 20).until(lambda b: b.find_element_by_id('login_btn'))
	except Exception as e:
		print(e)
		#等待输入将军令，直到进入
		otp = input('输入将军令:')
		b.find_element_by_id('otp').send_keys(otp)
		b.find_element_by_class_name('btn1').click()

	#进入
	b.find_element_by_id('login_btn').click()
	cookies = b.get_cookies()
	url =b.current_url
	b.quit()
	write_cookies(cookies)
	return cookies,url



