import requests
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from googletrans import Translator

# Keep your existing API key and bot token
TOKEN = "7934434941:AAGUF7-FH0JXPQ0HkH95_MPQvTVbA-bD_uU"
API_KEY = "sk-fqOxk83Pj95U2AZxLsehy88qWjItr1G9"

# Initialize translator
translator = Translator()

# Function to get AI response from Forefront API
def get_gpt_response(prompt, lang):
    url = "https://api.forefront.ai/v1/chat/completions"
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "model": "alpindale/Mistral-7B-v0.2-hf",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 128,
        "temperature": 0.5,
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        if response.status_code == 200:
            reply = response.json().get('choices', [{}])[0].get('message', {}).get('content', "I don't understand.")
        else:
            reply = "Sorry, something went wrong."
    except requests.exceptions.RequestException:
        reply = "No internet connection. Please try again later."

    # Translate response if user language is not English
    if lang != "en":
        reply = translator.translate(reply, dest=lang).text
    return reply

# Function to handle user messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    user_lang = update.message.from_user.language_code  # Detect user's language

    # Check if user asks about the creator
    if "creator" in user_message.lower() or "who made you" in user_message.lower():
        response = "My creator is Bruk Getachew @Nameofbless."
    else:
        response = get_gpt_response(user_message, user_lang)

    update.message.reply_text(response)

# Main function to run the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
