
# 脚本
一些实用小脚本的集合，不定期更新～
## 下载Telegram频道中的图片

### 依赖
`Python3.x`  
`Telethon`  
`PySocks`  

## 使用方法

依次安装 
`[Python3.x]`(https://www.python.org/) 
`[Telethon]`(https://github.com/LonamiWebs/Telethon) 
`[PySocks]`(https://github.com/Anorov/PySocks)
<br/>
1. 打开 `download-telegram-channel-pictures.py` 修改以下代码  
```Python
api_id = 123456
api_hash = "af042a39824c6"
channel_link = "https://t.me/xx"
```

2. 根据需要选择修改 以下代码  
```Python
proxy = (socks.SOCKS5, '127.0.0.1', 1080)
#proxy = None
```  

3. 找个位置开启命令行
`git clone https://github.com/Jxh98/scripts`
`python ./download-telegram-channel-pictures.py`

4. 输入手机号码  `例子 +86 13012341234`
输入Telegram中的验证码  `例子 12345`

`喝杯咖啡等待一下吧！`

5. 提示 `Done.` 即为下载完成。

## 其他说明：
[关于Telethon的文档在这里](https://telethon.readthedocs.io/en/latest/index.html)
