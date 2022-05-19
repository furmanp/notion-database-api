import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


def GetMemeberCount(channel_name):
    configure()
    url = f"https://api.telegram.org/{os.getenv('TELEGRAM_SECRET')}/getChatMemberCount?chat_id=@{channel_name}"
    try:
        response = requests.request('GET', url=url)
        return response.json()['result']
    except:
        return 'N/A'
