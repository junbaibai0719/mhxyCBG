import re

def fm(text):
	com = re.compile("<strong>(.*?)：?</strong>(.*?)\n? *?<",re.S)
	resule = re.findall(com,text)
	json1 = {i:j for i,j in resule}
	return json1