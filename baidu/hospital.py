import requests
import json
from baidu.__init__ import *
import pymysql
conn=pymysql.connect(MYSQL_HOST,MYSQL_ROOT,MYSQL_PASSWORD,MYSQL_DATABASE)
cur=conn.cursor()
cur.execute(USE)
cur.execute(DROP3)
cur.execute(CREATE3)
def getjson(loc):
	decodes=[]
	for page_num in range(M_PAGE):
		headers={'User-Agent':"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"}
		pa={'q':'医疗',
			'region':loc,
			'scope':'2',
			'page_size':20,
			'page_num':page_num,
			'output':'json',
			'ak':'这里加上你自己的ak'
		}
		try:
			r=requests.get("http://api.map.baidu.com/place/v2/search",params=pa,headers=headers)
			decodejson = json.loads(r.text)
			decodes.append(decodejson)
		except Exception as e:
			pass
	return decodes
def get_and_save():
	for place in places:
		decodes=getjson(place)
		for decodejson in decodes:
			if decodejson['results']:
				for eachone in decodejson["results"]:
					try:
						name=eachone["name"]
						print(name)
					except:
						name=None
					try:
						province=eachone["province"]
						print(province)
					except:
						province=None
					try:
						city=eachone["city"]
						print(city)
					except:
						city=None
					try:
						area=eachone["area"]
						print(area)
					except:
						area=None
					try:
						address=eachone["address"]
						print(address)
					except:
						address=None
					try:
						telephone=eachone["telephone"]
						print(telephone)
					except:
						telephone=None
					try:
						location_lat=eachone["location"]["lat"]
						print(location_lat)
					except:
						location_lat=None
					try:
						location_lng=eachone["location"]["lng"]
						print(location_lng)
					except:
						location_lng=None
					try:
						tag=eachone["detail_info"]["tag"]
						print(tag)
					except:
						tag=None
					try:
						type=eachone["detail_info"]["type"]
						print(type)
					except:
						type=None
					try:
						price=eachone["detail_info"]["price"]
						print(price)
					except:
						price=None
					try:
						overall_rating=eachone["detail_info"]["overall_rating"]
						print(overall_rating)
					except:
						overall_rating=None
					try:
						comment_num=eachone["detail_info"]["comment_num"]
						print(comment_num)
					except:
						comment_num=None
					try:
						image_num=eachone["detail_info"]["image_num"]
						print(image_num)
					except:
						image_num=None
					try:
						navi_location_lat=eachone["detail_info"]["navi_location"]["lat"]
						print(navi_location_lat)
					except:
						navi_location_lat=None
					try:
						navi_location_lng=eachone["detail_info"]["navi_location"]["lng"]
						print(navi_location_lng)
					except:
						navi_location_lng=None
					print("\n")
					print("\n")
					try:
						cur.execute(SAVEIN3,(name,province,city,area,address,telephone,location_lat,
							location_lng,tag,type,price,overall_rating,comment_num,image_num,
							navi_location_lat,navi_location_lng))
						conn.commit()
					except Exception as err:
						print(err)

if __name__=="__main__":
	# print(getjson("北京"))
	get_and_save()