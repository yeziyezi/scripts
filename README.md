# Scripts
一些实用小脚本的集合，不定期更新～
### 下载telegram频道中的图片
- 链接：[download-telegram-channel-pictures.py](./download-telegram-channel-pictures.py)

- 环境: python3
- 依赖: Telethon
  - 如果需要通过代理连接到telegram的话: aiohttp_socks (Python version>=3.6), PySocks (<=3.5)
- 使用方法: 
1. 在[my.telegram.org/apps](https://my.telegram.org/apps)拿到你的api-id以及api-hash
2.  将一些变量替换成你需要的值
3.  运行
- 注意事项：首次运行脚本需要输入tg所绑定的手机号和验证码，然后telethon才能以你的身份登录去下载图片
- 其他说明：[关于Telethon的文档在这里](https://telethon.readthedocs.io/en/latest/index.html)

### 删除指定文件夹下的重复文件
- 链接：[delete-duplicate-files.rb](./delete-duplicate-files.rb)
- 环境：ruby2.6.2
- 使用方法：将文件中“指定文件夹”替换为需要的值，然后```ruby delete-duplicate-files.rb```运行。

### 待更新……
