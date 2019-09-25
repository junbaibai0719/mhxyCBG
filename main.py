from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re
import json
import time

from login import login, write_cookies
from formatdata import fm
from mysql import CbgSql

urllogin = 'https://xyq.cbg.163.com/cgi-bin/show_login.py?act=show_login&server_id=149&server_name=%E5%86%8D%E7%BB%AD%E5%89%8D%E7%BC%98'
url = 'https://xyq.cbg.163.com/cgi-bin/query.py?act=recommend_search&recommend_type=1'
urlquery = 'https://xyq.cbg.163.com/cgi-bin/query.py?act=query'
urlgongshi = 'https://xyq.cbg.163.com/cgi-bin/query.py?act=fair_show_query'

username = 'lbj_no2@163.com'
passwd = 'll980413'

prefs = {"profile.managed_default_content_settings.images": 2}


def get(browser, url, cookies):
	browser.get(url)
	for ck in cookies:
		if ck['domain'] == 'xyq.cbg.163.com' and ck['httpOnly'] == True:
			browser.add_cookie(cookie_dict=ck)
	browser.get(url)
	WebDriverWait(browser, 3).until(lambda b: b.find_element_by_id('top_mycbg_menu_a'))


def getprice(browser, ):
	pass


def get_server_list(browser):
	url = 'https://xyq.cbg.163.com/'
	browser.get(url)
	area_list = browser.find_elements_by_xpath("//a[starts-with(@id,'area')]")
	s = set()
	c = 0
	for i in area_list:
		i.click()
		server_list = browser.find_elements_by_xpath("//a[starts-with(@id,'server')]")
		for sl in server_list:
			s.add(sl.get_attribute('data_serverid'))
			print(sl.get_attribute('data_serverid'))
			# print(sl.get_attribute('data_server_name'))
			# print(sl.get_attribute('data_area_name'))
			# print(sl.get_attribute('data_areaid'))
			print(sl.text)
			c += 1
			print(s.__len__(), c)


def get_goods_info(browser):
	# 进入我的收藏查看收藏商品
	browser.find_element_by_id('top_mycbg_menu_a').click()
	browser.find_element_by_id('menu_collect').click()
	browser.find_element_by_class_name('soldImg').click()

	WebDriverWait(browser, 10).until(lambda b: b.find_element_by_class_name('names'))
	# 获取编号,卖家姓名，卖家id，上架状态，是否接受还价，剩余时间
	num = browser.find_element_by_xpath("//strong[text()='编号：']/parent::li").text.split('：')
	sailname = browser.find_element_by_xpath("//strong[text()='卖家：']/parent::li").text.split('：')
	sailid = browser.find_element_by_xpath("//strong[text()='卖家ID：']/parent::li").text.split('：')
	is_shelf = browser.find_element_by_xpath("//strong[text()='是否上架：']/parent::li").text.split('：')
	is_counter_offer = browser.find_element_by_xpath("//strong[text()='是否接受还价：']/parent::li").text.split('：')
	remaining_time = browser.find_element_by_xpath("//strong[text()='出售剩余时间：']/parent::li").text.split('：')

	current_time = time.time()
	# price处理
	price = browser.find_element_by_xpath("//span[@class='price fB']/span").text
	res = re.findall('([1-9]\d*\.?\d*)|(0\.\d*)', price)
	price = float(''.join(res[0]))
	url = browser.current_url
	firstshelftime = ''.join(re.findall('eid=([0-9]{8})', url))
	firstshelftime = firstshelftime[0:4] + '-' + firstshelftime[4:6] + '-' + firstshelftime[6:8]
	eid = ''.join(re.findall('eid=(.{32})', url))
	t = remaining_time[1].rstrip('时').split('天')
	t = int(t[0]) * 86400 + int(t[1]) * 3600
	timeArray = time.localtime(t)
	shelftime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	timeArray = time.localtime(current_time)
	current_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	sailinfo = {
		num[0]: num[1]
		, sailname[0]: sailname[1]
		, '价格': price
		, sailid[0]: sailid[1]
		, is_shelf[0]: is_shelf[1]
		, is_counter_offer[0]: is_counter_offer[1]
		, remaining_time[0]: remaining_time[1]
		, '当前时间': current_time
		, 'url': url
		, '是否已出售': False
		, '公示时间': firstshelftime
		, '上架时间': shelftime
		, 'eid': eid
	}
	print(sailinfo)
	info = fm(
		browser.find_element_by_class_name('role_basic_attr_table').get_attribute("innerHTML"))
	print(info)

def try_otp(browser):
	try:
		WebDriverWait(browser, 1).until(
			lambda b: b.find_element_by_xpath("//h3[text()='请输入将军令的动态密码']"))
		# 等待输入将军令，直到进入
		otp = input('输入将军令:')
		browser.find_element_by_id('otp').send_keys(otp)
		browser.find_element_by_class_name('btn1').click()
	except Exception as e:
		print(e, '没有找到将军令输入界面')
		print('不需要输入将军令')

def get_equip_url(browser, url):
	browser.get(url)
	#获取类型列表
	kindlist = browser.find_elements_by_xpath("//a[starts-with(@id,'kind')]")
	kl = []
	for i in kindlist:
		if i.get_attribute('id') == 'kind_a_1'\
			or i.get_attribute('id') == 'kind_a_56' \
			or i.get_attribute('id') == 'kind_a_56' \
			or i.get_attribute('id') == 'kind_a_56' \
			or i.get_attribute('id') == 'kind_a_0' \
			or i.get_attribute('id') == 'kind_a_2' \
			or i.get_attribute('id') == 'kind_a_23' \
			or i.get_attribute('id') == 'kind_a_56':
			continue
		kl.append(int(i.get_attribute('id').lstrip('kind_a_')))
	with open('kindid.txt','w') as f:
		f.write(json.dumps(kl))
	cbgsql = CbgSql()
	cbgsql.connect()
	kl = list(reversed(kl))
	for kid in kl:
		browser.get(urlgongshi + '&page=%d' % 1 + '&kindid=%d' % kid)
		try:
			pagenum = browser.find_element_by_xpath("//div[@id='pager']/div[@class='pages']").text
			pagenum = int(''.join(re.findall('共(.*?)页', pagenum)))
		except Exception as e:
			print(e)
			try_otp(browser)
			pagenum = 1
		for page in range(1, pagenum + 1):
			browser.get(urlgongshi + '&page=%d' % page +'&kindid=%d'%kid)
			try:
				li= browser.find_elements_by_xpath("//a[@class='soldImg']")
				for i in li:
					url = i.get_attribute('href')
					# print(url)
					eid = ''.join(re.findall('eid=(.{32})', url))
					cbgsql.insertEquip(eid=eid, url=url)
			except Exception as e:
				print(e,'没有找到soldImg')
				try_otp(browser)


if __name__ == '__main__':
	chrome_options = webdriver.ChromeOptions()
	# chrome_options.add_experimental_option("prefs",prefs)
	# # 使用headless无界面浏览器模式
	# chrome_options.add_argument('--headless') #增加无界面选项
	# chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题

	# 启动浏览器，获取网页源代码
	browser = webdriver.Chrome(chrome_options=chrome_options)
	# 登录，cookie操作
	try:
		with open('cookie.py', 'r') as f:
			cookies = f.read()
			cookies = json.loads(cookies)
	except Exception as e:
		print(e)
	try:
		get(browser, url, cookies)
	except Exception as e:
		print(e)
		try:
			WebDriverWait(browser, 3).until(
				lambda b: b.find_element_by_xpath("//div[@class='blockTitle']/h3[text()='选择服务器']"))
			cookies, url = login(urllogin, username, passwd)
			for ck in cookies:
				if ck['domain'] == 'xyq.cbg.163.com' and ck['httpOnly'] == True:
					browser.add_cookie(cookie_dict=ck)
			browser.get(url)
		except Exception as e:
			print(e,'不是登录界面')
			try_otp(browser)
	get_equip_url(browser, urlgongshi)

# get_goods_info(browser)

# while True:
#
# 	break
# if price < 4300.00:
# 	print('降价了',price)
# elif price == 4300.00:
# 	print('无变化',price)
# else:
# 	break
# browser.refresh()
# mainUrl = 'https://xyq.cbg.163.com/equip?s=149&eid=201908271600113-149-JB3VFEQIPVQD&equip_refer=29'
# browser.get(mainUrl)
#
# print(browser.find_element_by_id('role_info_box').text)
# browser.find_element_by_id('role_equips').click()
# print(browser.find_element_by_id('role_info_box').text)
# browser.quit()
