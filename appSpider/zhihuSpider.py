import requests
import json
import time
headers = {"Cache-Control":"no-cache",
"Accept-Encoding":"gzip",
"Authorization":"Bearer gt2.0AAAAAAo9WjALQpW2sQJQAAAAAAxNVQJgAgBsEHHAlsgeJFlHb3CvOysxGHkpIg==",
"Cookie":"tgw_l7_route=156dfd931a77f9586c0da07030f2df36; z_c0=2|1:0|10:1539833726|4:z_c0|92:Z3QyLjBBQUFBQUFvOVdqQUxRcFcyc1FKUUFBQUFBQXhOVlFKZ0FnQnNFSEhBbHNnZUpGbEhiM0N2T3lzeEdIa3BJZz09|e412d5bafb6db0a73eabae1c5c35a37ac3b3aaf5fe9d9a931e123ee9935e6900; _xsrf=k5nAXjY6bL1mUKqkvaiVsFLfuouVNuwg",
"User-Agent":"Futureve/4.53.2 Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 Google-HTTP-Java-Client/1.22.0 (gzip)",
"x-api-version":"3.0.60",
"x-app-version":"4.53.2",
"x-app-za":"OS=Android&Release=6.0&Model=EVA-AL10&VersionName=4.53.2&VersionCode=501&Width=1080&Height=1812&Installer=%E5%8D%8E%E4%B8%BA%E5%BA%94%E7%94%A8%E5%B8%82%E5%9C%BA&WebView=55.0.2883.91",
"x-app-build":"release",
"x-network-type":"WiFi",
"x-suger":"SU1FST04NjM0NDUwMzE3MDIyMTM=",
"x-udid":"AFACsbaVQgtLBWnrOzJwdmc0vi7fsxldyw0=",
"Host":"api.zhihu.com",
"Connection":"Keep-Alive",}
url = "https://api.zhihu.com/topstory?action=down&action_feed=True&limit=7&after_id={}&session_token=858c0ca5584e6a95e64d619ebcf8f62b"
for i in range(6,49,7):
	url = url.format(i)
	time.sleep(3)
	response = requests.get(url,headers=headers,verify=False)
	content = response.content.decode()
	text = json.loads(content,encoding="utf-8")
	print(text)