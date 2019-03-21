from telethon import TelegramClient
#import socks # if you need connect telegram through proxy,import this.
from telethon.tl.types import InputMessagesFilterPhotos

# =======================================
'''Telegram Channel Pictures Download Tool
You can get your api_id and api_hash at https://my.telegram.org/apps
At the first time you run the script,you should provide your phone number 
to login in your telegram account(needed by Telethon).
'''
api_id = 12345
api_hash = "1234sdef"
channel_name = "AChannel"
proxy = None  # if need,replace "None" by "(socks.SOCKS5, 'host', port)".
picture_storage_path = "/path/to/picture/storage"
# ==========================================

client = TelegramClient('my_session',
                        api_id=api_id,
                        api_hash=api_hash,
                        proxy=proxy
                        ).start()

dialogs = client.get_dialogs()
channel = None
for dialog in dialogs:
    if dialog.name == channel_name:
        channel = dialog
        break

if channel is None:
    print("[Error]The channel ", channel_name, " is not subscribed!")
    exit(1)

photos = client.get_messages(channel, None, filter=InputMessagesFilterPhotos)
total = len(photos)
index = 0
for photo in photos:
    filename = picture_storage_path + str(photo.id) + ".jpg"
    print("downloading:", ++index, "/", total, " : ", filename)
    client.download_media(photo, filename)
print("Done.")
