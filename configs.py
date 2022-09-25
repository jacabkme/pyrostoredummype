# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "19890227"))
	API_HASH = os.environ.get("API_HASH", "ad2685e918be5a89c31e991448262e63")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5211965803:AAErvvVKh3XWfzhVEHqCashhS9B5I0piR9A") 
	BOT_USERNAME = os.environ.get("BOT_USERNAME", " filemini")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001787207236"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1540312271"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://random:random@cluster0.tb63h.mongodb.net/cluster0?retryWrites=true&w=majority") 
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001583792995")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Jasuran123

👥 **Support Group:** [DeepSea](https://t.me/dummypr)

📢 **Updates Channel:** [DeepSea](https://t.me/dummypr)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @JAsuran123

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
