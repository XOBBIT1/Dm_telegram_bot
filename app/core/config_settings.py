import os

import dotenv
from pathlib import Path

from aiogram import Dispatcher, Router, Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

token = os.environ['TOKEN']

# bd_settings
host = os.environ['HOST']
user = os.environ['USER']
password = os.environ['PASSWORD']
db_name = os.environ['DB_NAME']
port = os.environ["PORT"]
db_url = os.environ["DB_URL"]

dp = Dispatcher()
router = Router()
bot_engine = Bot(token)
scheduler = AsyncIOScheduler()

waiting_for_reply = set()
user_messages = dict()
