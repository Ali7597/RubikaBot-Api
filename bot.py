from rubika import Bot
import requests
import time

target=input("target: ")
while True:
	
	time.sleep(35)
	#بر حسب ثانیه هست تایمر
	
	url=requests.get("https://api.codebazan.ir/jok/")
	#message=input("text: ")
	mtn= url.text
	bot = Bot("Auth-Account")
	bot.sendMessage(target, mtn)
	
	#بچه ها guid رو نمیخواد اینجا بزنید وقتی ران کنید بهتون میگه واردش کنید و به پی وی ، کانال و گروه وصل میشه
