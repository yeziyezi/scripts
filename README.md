
# 脚本
一些实用小脚本的集合，不定期更新～
## 下载Telegram频道中的图片

2019年5月21日：更新了断点续传功能，再也不用担心电脑断网、断电了。

### 依赖
`Python3.x`  
`Telethon`  
`PySocks`  

## 使用方法

需要依次安装 
`[Python3.x]`(https://www.python.org/) 
`[Telethon]`(https://github.com/LonamiWebs/Telethon) 
`[PySocks]`(https://github.com/Anorov/PySocks)
<br/>
1. 打开 `download-telegram-channel-pictures.py` 修改以下代码  
``` Python
api_id = 123456 #api_id
api_hash = "af042a39824c6" #api_hash
channel_link = "https://t.me/xx" #你所想下载的频道链接 https://t.me/ 开头
```

``` bash
你可以从 https://my.telegram.org/apps 获得你的 api_id 和 api_hash 
在你第一次运行这个脚本的时候,
你需要提供你的手机号码（+86 15512348888）去登录你的Telegram账号。(因为这需要使用 Telethon)
```

2. 根据需要选择修改 以下代码  如果你在国内使用SSR 选择第一个 如果你在国外则选择第二个 
``` Python
proxy = (socks.SOCKS5, '127.0.0.1', 1080)
#proxy = None
```

3. 找个位置开启命令行
`git clone https://github.com/Jxh98/scripts`
`python ./download-telegram-channel-pictures.py`

4. 输入手机号码  例子 `+86 15512348888`
输入Telegram中的验证码  例子 `12345`

`喝杯咖啡等待一下吧！`

## 其他说明：
[关于Telethon的文档在这里](https://telethon.readthedocs.io/en/latest/index.html)