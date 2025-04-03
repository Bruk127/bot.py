# Telegram Bot (bot.py)

This is a Telegram bot built using Python and the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library. It integrates with the Forefront AI API to generate responses and supports multi-language interactions using [Googletrans](https://pypi.org/project/googletrans/4.0.0-rc1/) and [Langdetect](https://pypi.org/project/langdetect/).

## Features

- **AI-Powered Responses:** The bot uses the Forefront AI API to generate dynamic responses.
- **Multi-Language Support:** It detects the user's language and translates the response accordingly.
- **Creator Information:** When asked about its creator, it responds with "My creator is Bruk Getachew @Nameofbless."
- **Image Sending:** Supports sending images via the `/image` command if a file named `sample.jpg` is available.
- **Offline Handling:** Provides a fallback message if there’s no internet connection
