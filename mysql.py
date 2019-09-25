import pymysql
import time
class CbgSql():

	def connect(self):
		self.connection = pymysql.connect(
				host='localhost'
				, port=3306
				, user='root'
				, password=""
				, db="mydb"
				, charset="utf8"
		)
		self.connection.autocommit(True)

	def close(self):
		try:
			self.connection.close()
		except Exception as e:
			print(e)

	def insertEquip(self,
			eid = ''
			,num = ''
			,sailname =''
			,price='0'
			,sailid=''
			,is_shelf=True
			,is_counter_offer=False
			,remaining_time=''
			,current_time=None
			,url=''
			,is_onsale=False
			,firstshelftime=None
			,shelftime=None
			,kindid = ''
			):
		if current_time is None:
			timeArray = time.localtime(time.time())
			current_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		if firstshelftime is None:
			firstshelftime = current_time
		if shelftime is None:
			shelftime=current_time
		cu =self.connection.cursor()
		statment = """insert into `Equip`(
		`eid`
		,`num`
		,`sailname`
		,`price`
		,`sailid`
		,`is_shelf`
		,`is_counter_offer`
		,`remaining_time`
		,`current_time`
		,`url`
		,`is_onsale`
		,`firstshelftime`
		,`shelftime`
		,`kindid`
		)values ({},{},{},{},{},{},{}
				,{},{},{},{},{},{},{})""".format(
			 "'%s'" %eid
			,"'%s'" % num
			,"'%s'" % sailname
			,"'%s'" % price
			,"'%s'" % sailid
			,is_shelf
			,is_counter_offer
			,"'%s'" % remaining_time
			,"'%s'" % current_time
			,"'%s'" % url
			,is_onsale
			,"'%s'" % firstshelftime
			,"'%s'" % shelftime
			,"'%s'" % kindid)
		# print(statment)
		try:
			cu.execute(statment)
		except Exception as e:
			print(e)

	def read_column(self,tabelname = '',columnname = '',key='',value=''):
		cu = self.connection.cursor()
		if  key=='' or value =='':
			cu.execute("""select `{}` from `{}`""".format(columnname,tabelname))
		else:
			cu.execute("""select `{}` from `{}` where `{}` = '{}'""".format(columnname,tabelname,key,value))
		result = cu.fetchall()
		return result


cbg = CbgSql()
cbg.connect()
urllist = cbg.read_column(tabelname='Equip',columnname='url')
cbg.close()
for i in urllist:
	print(i)