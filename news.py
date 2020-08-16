import requests 
import xml.etree.ElementTree as ET 


def request_xml():
	resp=requests.get('https://www.thehindu.com/news/feeder/default.rss')
	with open('./file.xml','wb') as f:
		f.write(resp.content)


def add(f):
	tree=ET.parse(f)
	root=tree.getroot()
	feed=[]
	for item in root.findall('./channel/item'):
		news={}
		for child in item:
			if child.text is not None:
				news[child.tag]=child.text.encode('UTF-8')
		feed.append(news)
	return feed

def stories():
	request_xml()
	newsitems=add('file.xml')
	return newsitems


