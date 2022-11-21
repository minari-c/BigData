import urllib.request
import datetime
import json


client_id = 'EjbHjpgKv0gwN1C05qn6'
client_secret = 'FDtN2OazP7'


def getRequestUrl(url):
	req = urllib.request.Request(url)
	req.add_header("X-Naver-Client-Id", client_id)
	req.add_header("X-Naver-Client-Secret", client_secret)
	
	try:
		response = urllib.request.urlopen(req)
		if response.getcode() == 200:
			print("[%s] Url Request Success" % datetime.datetime.now())
			return response.read().decode('utf-8')
	except Exception as e:
		print(e)
		print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
		return None


def getNaverSearch(node, srcText, start, display):
	base = "https://openapi.naver.com/v1/search"
	node = "/%s.json" % node
	parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)
	
	url = base + node + parameters
	responseDecode = getRequestUrl(url)  # [CODE 1]
	
	if responseDecode is None:
		return None
	else:
		return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):
	title = post['title']
	description = post['description']
	org_link = post['originallink']
	link = post['link']
	
	pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
	pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
	
	jsonResult.append({'cnt': cnt, 'title': title, 'description': description, 'org_link': org_link, 'link': org_link,
	                   'pDate': pDate})
	return

	