import os

from dotenv import load_dotenv

load_dotenv()

ADMIN_ID = os.getenv("ADMIN")
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
URl= os.getenv("URL")