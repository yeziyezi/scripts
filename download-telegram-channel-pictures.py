from telethon import TelegramClient, sync
from telethon.tl.types import InputMessagesFilterPhotos
import socks  # 如果你需要使用代理（vpn），来连接Telegram。你需要导入它。
import os  # 用于读取文件，实现断点续传的功能。

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
channel_link = 你想下载图片的频道链接		 （网址字符串）
'''
# 例子 使用时 需根据 自己所拥有的信息进行更改
api_id = 123456
api_hash = "af042a39824"
channel_link = "https://t.me/???"

if channel_link[13:] == "???":
    print("请修改频道链接（channel_link）!")
    exit(1)

if api_id == 123456:
    print("请修改api_id 为自己的（api_id）!")
    exit(1)

if api_hash == "af042a39824":
    print("请修改api_hash 为自己的（api_hash）!")
    exit(1)

# SSR 可以用此配置
proxy = (socks.SOCKS5, '127.0.0.1', 1080)
# 如果你不需要代理就能连接Telegram，请注释上一行 放开下一行
#proxy = None


# 图片的存储路径 默认为 当前目录下的频道名称
picture_storage_path = channel_link[13:]
# ==========================================


# 获取一个 Telegram 客户端？
client = TelegramClient('my_session',
                        api_id=api_id,
                        api_hash=api_hash,
                        proxy=proxy
                        ).start()
print("初始化Telethon成功！")

# 获取你所打开的频道的数组
#dialogs = client.get_dialogs()

# 检查你所输入的 channel_name 是否正确
# for dialog in dialogs:
#    if dialog.name == channel_name:
#        channel = dialog
#        break

# if channel is None:
#    print("[Error]The channel ", channel_name, " is not subscribed!")
#    exit(1)

# 获取该频道的图片数组
photos = client.get_messages(
    channel_link, None, filter=InputMessagesFilterPhotos)
total = len(photos)
print("获取该频道的图片数组成功！")

F = []
# 判断本地是否有此文件夹
if os.path.exists(picture_storage_path):
    # 获取本地以拥有的图片名称数组
    L = os.listdir(picture_storage_path)
    for str1 in L:
        F.append(str1[0:-4])
    print("获取本地以拥有的图片名称数组成功！")

# 循环下载 支持 断点续传
sum = 0
index = 0
for photo in photos:
    if str(photo.id) in F:
        # print(str(photo.id) + ".jpg"+" 已下载！")
        sum += 1
    else:
        filename = picture_storage_path + "/" + str(photo.id) + ".jpg"
        index = index + 1
        print("正在下载:", index, "/", total, " : ", filename)
        client.download_media(photo, filename)
        sum += 1

# 无脑循环下载

# for photo in photos:
#     filename = picture_storage_path + "/" +str(photo.id) + ".jpg"
#     index = index + 1
#     print("downloading:", index, "/", total, " : ", filename)
#     client.download_media(photo, filename)

if sum == total:
    print("全部下载成功！")
else:
    print("部分下载成功，请在此运行程序，下载缺失部分！")

# 在你操作完成的时候关闭链接
client.disconnect()

print("关闭成功！")
