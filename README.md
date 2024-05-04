# YoBot

A bot that lets the boys vote on whether they are getting on Discord.

## Env

The following is required in a `.env` file:

- `TOKEN`: the bot's secret token.
- `TZ_IDENTIFIER`: timezone identifier string. Ex: `America/New_York`.
- `SCHEDULE_HOUR`: the hour at which the message will be sent.
- `SCHEDULE_MINUTE`: the minute at which the message will be sent.
- `CHANNEL_ID`: the id of the channel where the message will be sent
- `YO_EMOJI`: the "yo" emoji using Discord's format. Ex: `<:yo:689957806891204660>`
- `NO_EMOJI`: the "no" emoji using Discord's format. Ex: `<:no:483957824851202621>`

## Build

`docker build -t yobot .`

## Run

`docker run --rm -d yobot`

