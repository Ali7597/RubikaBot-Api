	elif msg["text"].startswith("!font"):
						response = get(f"https://api.codebazan.ir/font/?text={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:10])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "متأسفانه نتیجه‌ای در بر نداشت ☹️", message_id=msg["message_id"])
