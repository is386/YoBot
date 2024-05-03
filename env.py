import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
SCHEDULE_HOUR = int(os.getenv('SCHEDULE_HOUR'))
SCHEDULE_MINUTE = int(os.getenv('SCHEDULE_MINUTE'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
TZ_IDENTIFIER = os.getenv('TZ_IDENTIFIER')
YO_EMOJI = os.getenv('YO_EMOJI')
NO_EMOJI = os.getenv('NO_EMOJI')