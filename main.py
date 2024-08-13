from telethon import TelegramClient, events
from telethon.sessions import StringSession
from datetime import datetime
from keep_alive import keep_alive

api_id = 25221873
api_hash = '6b9b455b58e19a006eb8ed906c84b370'
string_session = '1BJWap1sBu1PqxFmF1EbJTotmHbnUAGrMkcy2iaWGAvgF99kiur9xgg667ANyKT8tDYjFeHYzFESOPVa38DJ8oGZ9ajdciiBYaPMG9TylqgmgOzADN3s8rYttje359Niz5ND7tyPZXzDDuaRFY4-6yGkf-WkADduvKw0xQheNi7Qz7aox3j8Yy8KYgIgfvfl5CnaxbQU7qZLPBx76UTN9BRl3i8h_lYaYpIbuBQaMxaVDtV2eJ7kLoO1I7k-JyTyOrr5NdC1KfcJsB9sq9iUrEWsxmDhHhycxRQKCUdoRk9DSqTi_1n_XJvX7aZUihK7o0G8UJDFMnkLwH-bs8jJsrpV_B6VnCto='

client = TelegramClient(StringSession(string_session), api_id, api_hash)

greeted_users = {}

banned_words = ['kot', 'mol', 'garang', 'tom', 'kalanga', 'kt', 'axmoq', 'jinni', 'fuck', 'it', 'eshak', 'ahmoq']

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private or event.is_channel:
        user_id = f"{event.sender.first_name or ''} {event.sender.last_name or ''}".strip() or "User"

        current_date = datetime.now().date()

        last_greeted = greeted_users.get(user_id)
        if last_greeted is None or last_greeted < current_date:
            if event.sender.language_code == 'en':
                await event.respond(f'👋 Hello, {user_id}! 😊')
            elif event.sender.language_code == 'uzb':
                await event.respond(f'👋 Assalomu alaykum, {user_id}! 😊')
            elif event.sender.language_code == 'ru':
                await event.respond(f'👋 Здравствуйте, {user_id}! 😊')
            else:
                await event.respond(f'👋 Assalomu alaykum, {user_id}! 😊')
            greeted_users[user_id] = current_date


        message_text = event.message.message.lower()
        if any(banned_word in message_text for banned_word in banned_words):
            if event.sender.language_code == 'en':
                await event.respond('🚫 Please do not using inappropriate language. 🛑')
            elif event.sender.language_code == 'ru':
                await event.respond('🚫 Пожалуйста, избегайте ненормативной лексики. 🛑')
            else:
                await event.respond('🚫 So\'kinme gaplashaylik. 🛑')
                

        if event.message.text.lower().startswith('/yomon_soz_qoshish '):
            new_word = event.message.text[len('/yomon_soz_qoshish '):].strip().lower()
            if new_word and new_word not in banned_words:
                banned_words.append(new_word)
                await event.respond(f'✅ The word "{new_word}" has been successfully added to the banned words list. 👍')
            elif new_word in banned_words:
                await event.respond(f'⚠️ The word "{new_word}" is already in the banned words list. ❗')
            else:
                await event.respond('❌ No word provided to add. 🚫')

with client:
    keep_alive()
    print("Client is running... 🚀")
    client.run_until_disconnected()
