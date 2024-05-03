# YoBot

A bot that lets the boys vote on whether they are getting on Discord.

## Env

The following is required in a `.env` file:

```ts
TOKEN="the bot's secret token"
TZ_IDENTIFIER="timezone identifier string. Ex: America/New_York"
SCHEDULE_HOUR="the hour the message will be sent at"
SCHEDULE_MINUTE="the minute the message will be sent at"
CHANNEL_ID="the id of the channel where the message will be sent"
YO_EMOJI="the 'yo' emoji using Discord's format. Ex: <:yo:689957806891204660>"
NO_EMOJI="the 'no' emoji using Discord's format. Ex: <:no:483957824851202621>"
```

## Usage

`python3 -m pip install -U discord.py`

`python3 main.py`