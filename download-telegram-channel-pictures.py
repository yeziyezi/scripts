from telethon import TelegramClient, sync
import socks # 如果你需要使用代理（vpn），来连接Telegram。你需要导入它。
from telethon.tl.types import InputMessagesFilterPhotos


# =======================================
'''Telegram 频道 图片 下载 工具
你可以从 https://my.telegram.org/apps 获得你的 api_id 和 api_hash 
在你第一次运行这个脚本的时候,
你需要提供你的手机号码去登录你的Telegram账号。
(这需要使用 Telethon)
'''

''' 
api_id = 你获得的 api_id 					（数字）
api_hash = 你获得的 api_hash 				（hash字符串）
channel_link = 你想下载图片的频道链接		（网址字符串）
'''
# 例子 使用时 需根据 自己所拥有的信息进行更改
api_id = 123456
api_hash = "af042a39824c6"
channel_link = "https://t.me/xx"

# SSR 可以用此配置
proxy = (socks.SOCKS5, '127.0.0.1', 1080) 
# 如果你不需要代理就能连接Telegram，请注释上一行 放开下一行
#proxy = None  


# 图片的存储路径 默认为 当前目录下的Pic
picture_storage_path = "Pic"
# ==========================================

# 获取一个 Telegram 客户端？
client = TelegramClient('my_session',
                        api_id=api_id,
                        api_hash=api_hash,
                        proxy=proxy
                        ).start()



# 获取你所打开的频道的数组
#dialogs = client.get_dialogs()

# 检查你所输入的 channel_name 是否正确
#for dialog in dialogs:
#    if dialog.name == channel_name:
#        channel = dialog
#        break

#if channel is None:
#    print("[Error]The channel ", channel_name, " is not subscribed!")
#    exit(1)

# 获取该频道的图片数组
photos = client.get_messages(channel, None, filter=InputMessagesFilterPhotos)
total = len(photos)
index = 0
# 循环下载
for photo in photos:
    filename = picture_storage_path + "/" +str(photo.id) + ".jpg"
    index = index + 1
    print("downloading:", index, "/", total, " : ", filename)
    client.download_media(photo, filename)
	
# 在你操作完成的时候关闭链接
client.disconnect()

print("Done.")
