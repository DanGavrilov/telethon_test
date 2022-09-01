import schedule
from telethon.sync import TelegramClient

api_id = 1
api_hash = 'api_hash'

file = open('chat_list.txt', 'r')
chats_ = [chat.split() for chat in file]
chats = sum(chats_, [])

with TelegramClient('name', api_id, api_hash) as client:
    def send_messages():
        for number in range(len(chats)):
            client.send_message(client.get_entity(chats[number]), "Python is cool")

    schedule.every(1).hour.do(send_messages)

    while True:
        schedule.run_pending()

