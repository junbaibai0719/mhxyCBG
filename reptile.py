import requests

area_name = "追忆"
server_name = "再续前缘"
cbg_url = "https://xyq.cbg.163.com/equip?s=149&eid=201810222300113-149-6ZYX3XQYU6SO&equip_refer=27"
url = """https://xyq.cbg.163.com/cgi-bin/show_login.py?act=show_login&area_id={}
                                                                    &area_name={}
                                                                    &server_id={}
                                                                    &server_name={}""".format(45,
																							  area_name,
																							  149,
																							  server_name)
cookie = '_ntes_nnid=f2f308ccab7a0b1476fb1adbc4c9b2e4,1546945013348; _ntes_nuid=f2f308ccab7a0b1476fb1adbc4c9b2e4; UM_distinctid=169a877a68b39e-0b852f771ab0ca-9333061-100200-169a877a68c6b6; vinfo_n_f_l_n3=e99a39b778780822.1.0.1553309605291.0.1553309641037; mail_psc_fingerprint=43dc72791aab3a4118afef45da6d404d; usertrack=CrH5y11nqSo2oxMTAwZ8Ag==; __f_=1567074604980; fingerprint=y5elxqev4jcr30eu; __session__=1; cbg_qrcode=qx0aT5xoCY1tuP5PXwkisso93sLMfMGBsHGavJ0R; NTES_SESS=e0N5FicOs67JMg2sZbOxblgqj8TlaUXE8IQqlOAepQ2_8ptA.y5u3P2EDk_5KJSnjW_TaJo1UDV7S6hmthSJ0XTJevO30rDCxmpa8PZ6o51PeXG1lo0COqkFI6x2RcIZxeU9osEZrilKPUfJmbfcFkIZIKvslSsW.4wwDLjByh4x_.R1wTeViQDccsfVTufR_; sid=wL4LClD-TKcm1AewTXTlJfBScZajPgrRAHduQOUJ; cur_servername=%25E5%2586%258D%25E7%25BB%25AD%25E5%2589%258D%25E7%25BC%2598; last_login_roleid=16096500; login_user_nickname=%25E2%2596%25B3%25E8%258F%2585%25E8%258A%25B7%25E8%2595%258A%25E2%2584%2596; is_user_login=1; login_user_icon=2; login_user_roleid=16096500; login_user_level=0; login_user_urs=lbj_no2@163.com; login_user_school=None; new_msg_num=1; offsale_num=0; unpaid_order_num=0; unpaid_order_price_total=0.00; last_login_role_serverid=149; recommend_typeids=1,2,3,4; recommend_url=https://xyq.cbg.163.com/cgi-bin/query.py?act=recommend_search&recommend_type=1; last_login_serverid=149; wallet_data=%7B%22is_locked%22%3A%20false%2C%20%22checking_balance%22%3A%200%2C%20%22balance%22%3A%200%2C%20%22free_balance%22%3A%200%7D; remind_offsale=1; alert_msg_flag=1; overall_sid=_7BSruTW20YcaLIh88hoPxtMtatKmrEyGUwwi9ps'

header = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept - Encoding": "gzip, deflate, br",
	"Accept - Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
	"Cache-Control": "max-age=0",
	"Connection": "Keep-Alive",
	'Cookie': cookie,
	# 'return_url=; NTES_SESS=DEmm1mnamlqhiEQk32xdJRpSisksWXxvugQra9uNBsk6AmJgg_rsNCnNtiw29dHIHMDWZr24onf7WsHfSMmXQV.MG6lZo6O9r59RiI8ydmBnaSXcEsYiwOQImyXNMxYxffu77b9Grs5iP.MH09GHDuAxuDWlH4yWbX1Tw986UaxflAXiwI8EXJQLJP_ZxR5Vw9XNQlKluEA8c; S_INFO=1540385699|0|3&100##|yowl_no1; P_INFO=yowl_no1@163.com|1540385699|0|cbg|00&99|bej&1540385640&cbg#bej&null#10#0#0|188361&0|g37_client_check&g37_client&cbg|yowl_no1@163.com; _ntes_nnid=c518da51cc564a427c65dbf8ff22d4c7,1540385685146; _ntes_nuid=c518da51cc564a427c65dbf8ff22d4c7; __session__=1; sid=8LY8Fs65FqBeEiF3ZctijNWWBUbdqY1egX0UPEfg; wallet_data=%7B%22is_locked%22%3A%20false%2C%20%22checking_balance%22%3A%200%2C%20%22balance%22%3A%200%2C%20%22free_balance%22%3A%200%7D; login_user_nickname=%25E7%25BB%2595%25E6%258C%2587%25E6%259F%2594%25E4%25B8%25B6%25E5%2590%259B%25E5%25BF%2583; is_user_login=1; login_user_icon=8; login_user_roleid=14983812; login_user_level=58; login_user_urs=yowl_no1@163.com; login_user_school=12; new_msg_num=0; offsale_num=0; unpaid_order_num=0; unpaid_order_price_total=0.00; last_login_roleid=14983812; last_login_role_serverid=149; area_id=45; recommend_url=https://xyq.cbg.163.com/cgi-bin/query.py?act=recommend_search&recommend_type=1; fingerprint=1513062741; fingerprint=1513062741; remind_offsale=1; last_login_serverid=149; recommend_typeids=1,2,3,4',
	"Host": "xyq.cbg.163.com",
	"Referer": "https://xyq.cbg.163.com/equip?s=149&eid=201810200100113-149-CEGEICFWYBCL&equip_refer=26&view_loc=reco_left",
	'Upgrade - Insecure - Requests': '1',
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
login_url = "https://dl.reg.163.com/dl/l"
post_data = {"un": "yowl_no1@163.com",
			 "pw": "dvBDuV63E099Kk9mjvrAkaMzRaKDXIDddRJQ3EVy5JuRYTAK+bXCf3YNDljCbV4pt68HjGUMmLxmCFSShSafhDwaxAHSNwzeAibvOjGAMuf1Sad8ULqFv22HTSJTyqXh+l1CAhRFYzPDFB9iuSI/f1qGwvUhFQ/DTYLsEKy5tvc=",
			 "pd": "cbg", "l": 0, "d": 10, "t": 1540364067101, "pkid": "aqpOBwV", "domains": "",
			 "tk": "f9b7ee66e27915ce3906984aa92e7ee2", "pwdKeyUp": 1,
			 "topURL": "https://xyq.cbg.163.com/cgi-bin/show_login.py?act=show_login&area_id=45&area_name=%E8%BF%BD%E5%BF%86&server_id=149&server_name=%E5%86%8D%E7%BB%AD%E5%89%8D%E7%BC%98",
			 "rtid": "AJn8D7wmVnMsGZwRLbTBTJXOvajBsMCd"}
post_data1 = {"un": "yowl_no1@163.com",
			  "pw": "OobjZz25gw8ZRZQ6BL1fr3FEicsm3gf5gEmglNSb5IP7U50+bniDITVHYXDLZyxdGng4rhEXRWa3s5iIZnghylDCEjaBMrfS5daScVeKcNIa+CQ1t9y+aNQu7twV+26OLlV1gnnOaD7hJ6ysoIsENqm+s/c6nXp8PMXnBUxtbBo=",
			  "pd": "cbg", "l": 0, "d": 10, "t": 1540365929634, "pkid": "aqpOBwV", "domains": "",
			  "tk": "e7448d5044ea3fea94f4d2e75502ec94", "pwdKeyUp": 1,
			  "topURL": "https://xyq.cbg.163.com/cgi-bin/show_login.py?act=show_login&area_id=45&area_name=%E8%BF%BD%E5%BF%86&server_id=149&server_name=%E5%86%8D%E7%BB%AD%E5%89%8D%E7%BC%98",
			  "rtid": "2t4UQr9ribnN9MKPVd7UEL10P0dh293s"}
post_data2 = {"un": "yowl_no1@163.com",
			  "pw": "nLMkS+NmF3VUf8QinCONBkokVf0+qQYjrTSs0+RM5x/PxjrE/b2M3OoB1dhxBlUa5hVwNbN+sKQx47tXjhKgumRXLyw0J+qXcFW0E47VZCdZb63Zx7TQj5FJTDrSbIcPcXFKULO8bntd7ijHVRvHD7v4aa0/z6R4/U7hsKZnPuA=",
			  "pd": "cbg", "l": 0, "d": 10, "t": 1540366074708, "pkid": "aqpOBwV", "domains": "",
			  "tk": "f545cb3ddb9f0815374f21797c87d3ce", "pwdKeyUp": 1,
			  "topURL": "https://xyq.cbg.163.com/cgi-bin/show_login.py?act=show_login&area_id=45&area_name=%E8%BF%BD%E5%BF%86&server_id=149&server_name=%E5%86%8D%E7%BB%AD%E5%89%8D%E7%BC%98",
			  "rtid": "pbw1UsuLbRFkRSVTR7OFghPzfCBRZ4Zw"}
response = requests.post(
	'https://xyq.cbg.163.com/equip?s=149&eid=201908271600113-149-JB3VFEQIPVQD&equip_refer=34&view_loc=search_key',
	headers=header)
response.encoding = 'gbk'
print(response.text)

# a =  {
#     "1": [["上海1区", "5_3", "4", "shanghai1qu", 1, "shyq"], [[159, "珍宝阁", "1_1", "zhenbaoge", "zbg"], [819, "东海之滨", "2_1", "donghaizhibin", "dhzb"], [163, "晚芳亭", "3_1", "wanfangting", "wft"], [811, "繁花似锦", "4_1", "fanhuasijin", "fhsj"], [841, "灿若星河", "5_1", "canruoxinghe", "crxh"], [847, "**", "6_1", "haikuotiankong", "hktk"], [861, "倾城之恋", "7_1", "qingchengzhilian", "qczl"]]],
#     "2": [["广东3区", "4_7", "40", "guangdong3qu", 2, "gdsq"], [[2, "罗浮山", "1_1", "luofushan", "lfs"], [677, "广州湾", "2_1", "guangzhouwan", "gzw"], [805, "风华绝代", "3_1", "fenghuajuedai", "fhjd"]]],
#     "3": [["北京1区", "5_1", "3", "beijing1qu", 3, "bjyq"], [[3, "国子监", "1_1", "guozijian", "gzj"], [155, "太和殿", "2_1", "taihedian", "thd"], [9, "紫禁城", "3_1", "zijincheng", "zjc"], [459, "2008", "4_1", "2008", "ellb"], [527, "生日快乐", "5_1", "shengrikuaile", "srkl"], [699, "喜大普奔", "6_1", "xidapuben", "xdpb"], [769, "景泰蓝", "7_1", "jingtailan", "jtl"], [769, "恭王府", "1_2", "gongwangfu", "gwf"], [776, "天坛公园", "2_2", "tiantangongyuan", "ttgy"], [786, "五道口", "3_2", "wudaokou", "wdk"], [786, "十里霓虹", "4_2", "shilinihong", "slnh"], [838, "黄金台", "5_2", "huangjintai", "hjt"], [846, "豪情壮志", "6_2", "haoqingzhuangzhi", "hqzz"], [851, "江山如画", "7_2", "jiangshanruhua", "jsrh"]]],
#     "4": [["广东4区", "4_8", "48", "guangdong4qu", 4, "gdsq"], [[358, "流花湖", "1_1", "liuhuahu", "lhh"], [85, "白云山", "2_1", "baiyunshan", "bys"], [82, "状元坊", "3_1", "zhuangyuanfang", "zyf"], [84, "流溪河", "4_1", "liuxihe", "lxh"]]],
#     "5": [["浙江3区", "4_3", "43", "zhejiang3qu", 5, "zjsq"], [[139, "普陀山", "1_1", "putuoshan", "pts"], [138, "钱塘江", "2_1", "qiantangjiang", "qtj"], [804, "功成名就", "3_1", "gongchengmingjiu", "gcmj"], [834, "水阁乌镇", "4_1", "shuigewuzhen", "sgwz"]]],
#     "6": [["广西2区", "1_9", "55", "guangxi2qu", 6, "gxeq"], [[297, "叠彩山", "1_1", "diecaishan", "dcs"], [6, "黄姚古镇", "2_1", "huangyaoguzhen", "hygz"]]],
#     "7": [["河南2区", "2_5", "39", "henan2qu", 7, "hneq"], [[192, "牡丹亭", "1_1", "mudanting", "mdt"], [193, "少室山", "2_1", "shaoshishan", "sss"], [337, "王屋山", "3_1", "wangwushan", "wws"], [859, "逍遥游", "4_1", "xiaoyaoyou", "xyy"]]],
#     "8": [["山东2区", "6_6", "13", "shandong2qu", 8, "sdeq"], [[212, "水泊梁山", "1_1", "shuipoliangshan", "spls"], [828, "太阳城", "2_1", "taiyangcheng", "tyc"], [835, "泱泱大风", "3_1", "yangyangdafeng", "yydf"], [852, "齐鲁大地", "4_1", "qiludadi", "qldd"], [863, "藏龙涧", "5_1", "canglongjian", "clj"]]],
#     "9": [["北京2区", "5_2", "44", "beijing2qu", 9, "bjeq"], [[299, "阳光城", "1_1", "yangguangcheng", "ygc"], [689, "**长城", "2_1", "wanlichangcheng", "wlcc"], [732, "长安街", "3_1", "changanjie", "caj"], [799, "东方巨龙", "4_1", "dongfangjulong", "dfjl"], [786, "青春如诗", "5_1", "qingchunrushi", "qcrs"], [810, "天之骄子", "6_1", "tianzhijiaozi", "tzjz"], [816, "龙争虎斗", "7_1", "longzhenghudou", "lzhd"], [821, "顺天府", "1_2", "shuntianfu", "stf"], [826, "叱咤风云", "2_2", "chizhafengyun", "czfy"], [799, "逐梦青春", "3_2", "zhumengqingchun", "zmqc"], [810, "乘风破浪", "4_2", "chengfengpolang", "cfpl"], [816, "高山流水", "5_2", "gaoshanliushui", "gsls"], [816, "上海滩", "6_2", "shanghaitan", "sht"], [821, "丝绸之府", "7_2", "sichouzhifu", "sczf"]]],
#     "10": [["福建2区", "3_7", "45", "fujian2qu", 10, "fjeq"], [[304, "日光岩", "1_1", "riguangyan", "rgy"], [234, "鼓浪屿", "2_1", "gulangyu", "gly"], [11, "百花村", "3_1", "baihuacun", "bhc"], [326, "齐云楼", "4_1", "qiyunlou", "qyl"]]],
#     "11": [["广西1区", "1_8", "20", "guangxi1qu", 11, "gxyq"], [[12, "明秀园", "1_1", "mingxiuyuan", "mxy"], [249, "青秀山", "2_1", "qingxiushan", "qxs"], [86, "云天宫", "3_1", "yuntiangong", "ytg"]]],
#     "12": [["河北1区", "2_1", "14", "hebei1qu", 12, "hbyq"], [[60, "缘聚唐城", "1_1", "yuanjutangcheng", "yjtc"], [402, "渤海明珠", "2_1", "bohaimingzhu", "bhmz"]]],
#     "13": [["河北3区", "2_3", "49", "hebei3qu", 13, "hbsq"], [[15, "避暑山庄", "1_1", "bishushanzhuang", "bssz"]]],
#     "14": [["黑龙江区", "6_1", "35", "heilongjiangqu", 14, "hljq"], [[221, "雪域天龙", "1_1", "xueyutianlong", "xytl"]]],
#     "15": [["湖北1区", "2_7", "16", "hubei1qu", 15, "hbyq"], [[94, "武当山", "1_1", "wudangshan", "wds"], [420, "昭君台", "2_1", "zhaojuntai", "zjt"]]],
#     "16": [["湖北2区", "2_8", "42", "hubei2qu", 16, "hbeq"], [[95, "神农架", "1_1", "shennongjia", "snj"], [223, "黄鹤楼", "2_1", "huanghelou", "hhl"]]],
#     "17": [["湖南区", "2_9", "26", "hunanqu", 17, "hnq"], [[275, "橘子洲", "1_1", "juzizhou", "jzz"], [96, "洞庭湖", "2_1", "dongtinghu", "dth"]]],
#     "19": [["天津区", "7_1", "60", "tianjinqu", 19, "tjq"], [[55, "精武门", "1_1", "jingwumen", "jwm"]]],
#     "20": [["吉林区", "6_2", "36", "jilinqu", 20, "jlq"], [[307, "佟佳江", "1_1", "tongjiajiang", "tjj"]]],
#     "21": [["江苏1区", "3_1", "9", "jiangsu1qu", 21, "jsyq"], [[101, "文昌阁", "1_1", "wenchangge", "wcg"], [104, "雨花台", "2_1", "yuhuatai", "yht"], [676, "凤凰台", "3_1", "fenghuangtai", "fht"], [816, "高山流水", "4_1", "gaoshanliushui", "gsls"], [831, "齐天大圣", "5_1", "qitiandasheng", "qtds"], [837, "风起云扬", "6_1", "fengqiyunyang", "fqyy"], [865, "天下文枢", "7_1", "tianxiawenshu", "txws"]]],
#     "22": [["江苏2区", "3_2", "38", "jiangsu2qu", 22, "jseq"], [[105, "夫子庙", "1_1", "fuzimiao", "fzm"], [352, "姑苏城", "2_1", "gusucheng", "gsc"], [831, "虎踞龙盘", "3_1", "hujulongpan", "hjlp"], [849, "金风玉露", "4_1", "jinfengyulu", "jfyl"], [860, "枫桥夜泊", "5_1", "fengqiaoyepo", "fqyp"]]],
#     "23": [["江苏3区", "3_3", "51", "jiangsu3qu", 23, "jssq"], [[26, "花果山", "1_1", "huaguoshan", "hgs"], [462, "镇淮楼", "2_1", "zhenhuailou", "zhl"], [831, "燕子矶", "3_1", "yanziji", "yzj"], [854, "春风十里", "4_1", "chunfengshili", "cfsl"]]],
#     "24": [["江西区", "3_5", "25", "jiangxiqu", 24, "jxq"], [[270, "庐山胜境", "1_1", "lushanshengjing", "lssj"]]],
#     "25": [["辽宁1区", "6_3", "15", "liaoning1qu", 25, "lnyq"], [[367, "星海湾", "1_1", "xinghaiwan", "xhw"]]],
#     "26": [["山东1区", "6_5", "33", "shandong1qu", 26, "sdyq"], [[211, "东岳泰山", "1_1", "dongyuetaishan", "dyts"], [360, "南天门", "2_1", "nantianmen", "ntm"], [669, "青岛栈桥", "3_1", "qingdaozhanqiao", "qdzq"], [681, "东海崂山", "4_1", "donghailaoshan", "dhls"], [779, "孙子兵法", "5_1", "sunzibingfa", "szbf"], [810, "乘风破浪", "6_1", "chengfengpolang", "cfpl"], [830, "千帆竞发", "7_1", "qianfanjingfa", "qfjf"], [843, "百战不殆", "1_2", "baizhanbudai", "bzbd"]]],
#     "27": [["山东3区", "6_7", "37", "shandong3qu", 27, "sdsq"], [[33, "蓬莱岛", "1_1", "penglaidao", "pld"], [857, "壮气凌云", "2_1", "zhuangqilingyun", "zqly"], [867, "黄海明珠", "3_1", "huanghaimingzhu", "hhmz"]]],
#     "28": [["山东4区", "6_8", "47", "shandong4qu", 28, "sdsq"], [[207, "大明湖", "1_1", "daminghu", "dmh"], [443, "沂水雪山", "2_1", "yishuixueshan", "ysxs"], [830, "青州古城", "3_1", "qingzhougucheng", "qzgc"]]],
#     "29": [["山东5区", "6_9", "54", "shandong5qu", 29, "sdwq"], [[34, "玉皇顶", "1_1", "yuhuangding", "yhd"], [407, "曲阜孔庙", "2_1", "qufukongmiao", "qfkm"], [657, "威海卫", "3_1", "weihaiwei", "whw"]]],
#     "30": [["山西区", "1_2", "19", "shanxiqu", 30, "sxq"], [[421, "雁门关", "1_1", "yanmenguan", "ymg"]]],
#     "31": [["陕西区", "1_3", "12", "shanxiqu", 31, "sxq"], [[200, "大雁塔", "1_1", "dayanta", "dyt"], [203, "西岳华山", "2_1", "xiyuehuashan", "xyhs"]]],
#     "32": [["上海2区", "5_4", "22", "shanghai2qu", 32, "sheq"], [[38, "东方明珠", "1_1", "dongfangmingzhu", "dfmz"], [622, "徐家汇", "2_1", "xujiahui", "xjh"], [799, "逐梦青春", "3_1", "zhumengqingchun", "zmqc"], [816, "上海滩", "4_1", "shanghaitan", "sht"], [855, "四海升平", "5_1", "sihaishengping", "shsp"]]],
#     "33": [["深圳2区", "3_9", "52", "shenzhen2qu", 33, "szeq"], [[412, "梧桐山", "1_1", "wutongshan", "wts"], [344, "小梅沙", "2_1", "xiaomeisha", "xms"], [39, "世界之窗", "3_1", "shijiezhichuang", "sjzc"]]],
#     "34": [["四川1区", "1_4", "23", "sichuan1qu", 34, "scyq"], [[263, "嘉陵江", "1_1", "jialingjiang", "jlj"], [40, "成都府", "2_1", "chengdufu", "cdf"]]],
#     "35": [["浙江4区", "4_4", "50", "zhejiang4qu", 35, "zjsq"], [[377, "绍兴兰亭", "1_1", "shaoxinglanting", "sxlt"], [416, "绍兴鉴湖", "2_1", "shaoxingjianhu", "sxjh"], [750, "烟雨江南", "3_1", "yanyujiangnan", "yyjn"], [821, "丝绸之府", "4_1", "sichouzhifu", "sczf"], [850, "琴心剑胆", "5_1", "qinxinjiandan", "qxjd"]]],
#     "36": [["贵州区", "1_7", "57", "guizhouqu", 36, "gzq"], [[285, "红枫湖", "1_1", "hongfenghu", "hfh"]]],
#     "37": [["深圳1区", "3_8", "21", "shenzhen1qu", 37, "szyq"], [[116, "大观园", "1_1", "daguanyuan", "dgy"]]],
#     "38": [["时光", "7_6", "32", "shiguang", 38, "sg"], [[45, "花样年华", "1_1", "huayangnianhua", "hynh"]]],
#     "39": [["华南区", "7_2", "6", "huananqu", 39, "hnq"], [[173, "逍遥城", "1_1", "xiaoyaocheng", "xyc"], [625, "钓鱼岛", "2_1", "diaoyudao", "dyd"], [173, "侠客岛", "3_1", "xiakedao", "xkd"]]],
#     "40": [["内蒙区", "1_1", "17", "neimengqu", 40, "nmq"], [[229, "雄鹰岭", "1_1", "xiongyingling", "xyl"]]],
#     "41": [["福建1区", "3_6", "18", "fujian1qu", 41, "fjyq"], [[305, "朱紫坊", "1_1", "zhuzifang", "zzf"], [305, "凌云殿", "2_1", "lingyundian", "lyd"]]],
#     "42": [["安徽1区", "3_4", "24", "anhui1qu", 42, "ahyq"], [[417, "紫蓬山", "1_1", "zipengshan", "zps"], [266, "慈光阁", "2_1", "ciguangge", "cgg"]]],
#     "43": [["广东2区", "4_6", "8", "guangdong2qu", 43, "gdeq"], [[79, "如意岛", "1_1", "ruyidao", "ryd"], [77, "进贤门", "2_1", "jinxianmen", "jxm"], [78, "万绿湖", "3_1", "wanluhu", "wlh"], [79, "七星岩", "4_1", "qixingyan", "qxy"]]],
#     "44": [["云南区", "1_6", "29", "yunnanqu", 44, "ynq"], [[127, "彩云之南", "1_1", "caiyunzhinan", "cyzn"], [130, "蝴蝶泉", "2_1", "hudiequan", "hdq"]]],
#     "45": [["追忆", "7_5", "2", "zhuiyi", 45, "zy"], [[149, "再续前缘", "1_1", "zaixuqianyuan", "zxqy"], [150, "梦回望月", "2_1", "menghuiwangyue", "mhwy"]]],
#     "47": [["广东1区", "4_5", "34", "guangdong1qu", 47, "gdyq"], [[72, "湖光岩", "1_1", "huguangyan", "hgy"]]],
#     "48": [["河北2区", "2_2", "41", "hebei2qu", 48, "hbeq"], [[334, "燕塞湖", "1_1", "yansehu", "ysh"], [215, "燕赵风云", "2_1", "yanzhaofengyun", "yzfy"]]],
#     "49": [["河南1区", "2_4", "11", "henan1qu", 49, "hnyq"], [[413, "少林寺", "1_1", "shaolinsi", "sls"], [197, "中岳嵩山", "2_1", "zhongyuesongshan", "zyss"], [199, "汴梁城", "3_1", "bianliangcheng", "blc"], [825, "龙图腾", "4_1", "longtuteng", "ltt"], [825, "开天辟地", "5_1", "kaitianpidi", "ktpd"], [839, "武麒麟", "6_1", "wuqilin", "wql"], [845, "九州鼎", "7_1", "jiuzhouding", "jzd"], [853, "紫气东来", "8_1", "ziqidonglai", "zqdl"]]],
#     "50": [["河南3区", "2_6", "58", "henan3qu", 50, "hnsq"], [[414, "南阳府", "1_1", "nanyangfu", "nyf"]]],
#     "51": [["辽宁2区", "6_4", "46", "liaoning2qu", 51, "lneq"], [[367, "医巫闾山", "1_1", "yiwulvshan", "ywls"]]],
#     "52": [["四川2区", "1_5", "5", "sichuan2qu", 52, "sceq"], [[167, "文殊院", "1_1", "wenshuyuan", "wsy"], [123, "德阳文庙", "2_1", "deyangwenmiao", "dywm"]]],
#     "54": [["浙江1区", "4_1", "28", "zhejiang1qu", 54, "zjyq"], [[133, "台州湾", "1_1", "taizhouwan", "tzw"], [132, "西栅老街", "2_1", "xishanlaojie", "xslj"], [712, "文澜阁", "3_1", "wenlange", "wlg"], [804, "黄龙吐翠", "4_1", "huanglongtucui", "hltc"], [804, "古灵精怪", "5_1", "gulingjingguai", "gljg"], [840, "三吴都会", "6_1", "sanwuduhui", "swdh"], [858, "龙泉山", "7_1", "longquanshan", "lqs"]]],
#     "55": [["浙江2区", "4_2", "10", "zhejiang2qu", 55, "zjeq"], [[137, "苏堤春晓", "1_1", "sudichunxiao", "sdcx"], [378, "灵隐寺", "2_1", "lingyinsi", "lys"], [661, "碧海潮生", "3_1", "bihaichaosheng", "bhcs"], [758, "西湖龙井", "4_1", "xihulongjing", "xhlj"], [758, "人间天堂", "5_1", "renjiantiantang", "rjtt"], [864, "彩凤鸣岐", "6_1", "caifengmingqi", "cfmq"]]],
#     "56": [["重庆区", "5_5", "31", "chongqingqu", 56, "cqq"], [[146, "解放碑", "1_1", "jiefangbei", "jfb"], [482, "茶山竹海", "2_1", "chashanzhuhai", "cszh"]]],
#     "57": [["海外专区", "7_4", "30", "haiwaizhuanqu", 57, "hwzq"], [[173, "侠客岛", "1_1", "xiakedao", "xkd"]]],
#     "58": [["无与伦比", "7_3", "61", "wuyulunbi", 58, "wylb"], [[554, "兰亭序", "1_1", "lantingxu", "ltx"], [558, "青花瓷", "2_1", "qinghuaci", "qhc"], [559, "本草纲目", "3_1", "bencaogangmu", "bcgm"], [558, "菊花台", "4_1", "juhuatai", "jht"], [579, "千里之外", "5_1", "qianlizhiwai", "qlzw"], [583, "龙拳", "6_1", "longquan", "lq"], [584, "将军", "7_1", "jiangjun", "jj"], [705, "龙马精神", "1_2", "longmajingshen", "lmjs"]]],
#     "60": [["天下无双", "5_6", "67", "tianxiawushuang", 60, "txws"], [[723, "群星璀璨", "1_1", "qunxingcuican", "qxcc"], [730, "金戈铁马", "2_1", "jingetiema", "jgtm"], [762, "群雄逐鹿", "3_1", "qunxiongzhulu", "qxzl"], [805, "聚圣三界", "4_1", "jushengsanjie", "jssj"], [783, "梦回长安", "5_1", "menghuichangan", "mhca"], [785, "逍遥三界", "6_1", "xiaoyaosanjie", "xysj"], [791, "诗情画意", "7_1", "shiqinghuayi", "sqhy"], [795, "超凡入圣", "1_2", "chaofanrusheng", "cfrs"], [805, "风华绝代", "2_2", "fenghuajuedai", "fhjd"], [866, "纵横驰骋", "3_2", "zonghengchicheng", "zhcc"]]],
#     "61": [["笑傲三界", "5_7", "70", "xiaoaosanjie", 61, "xasj"], [[807, "花好月圆", "1_1", "huahaoyueyuan", "hhyy"], [811, "华山论剑", "2_1", "huashanlunjian", "hslj"], [819, "上古神器", "3_1", "shanggushenqi", "sgsq"], [828, "群雄争霸", "4_1", "qunxiongzhengba", "qxzb"], [832, "纵横天下", "5_1", "zonghengtianxia", "zhtx"], [836, "机巧乾坤", "6_1", "jiqiaoqiankun", "jqqk"], [842, "腾云驾雾", "7_1", "tengyunjiawu", "tyjw"], [811, "繁花似锦", "1_2", "fanhuasijin", "fhsj"], [844, "皓月千里", "2_2", "haoyueqianli", "hyql"], [848, "龙吟九天", "3_2", "longyinjiutian", "lyjt"], [856, "绝代天骄", "4_2", "juedaitianjiao", "jdtj"], [828, "太阳城", "5_2", "taiyangcheng", "tyc"], [819, "东海之滨", "6_2", "donghaizhibin", "dhzb"], [862, "龙飞凤舞", "7_2", "longfeifengwu", "lffw"]]],
#     "62": [["名扬三界", "5_8", "71", "mingyangsanjie", 62, "mysj"], [[868, "文韬武略", "1_1", "wentaowulue", "wtwl"]]]
# }
#
# import json
#
# print(json.dumps(a,ensure_ascii=False, indent=4))
