import os

API_ID = int(os.environ.get("API_ID", 26352575))
API_HASH = os.environ.get("API_HASH", 398efeced6b006e357b339b14ffa182a)
BOT_TOKEN = os.environ.get("BOT_TOKEN", 6506519905:AAHj99efEH_QL-WB0WIjph0tq8Mu4lK-sNg)
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", -1002038756270)
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID",7138268353))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'https://inote.pro/notes/DR0W5P')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
