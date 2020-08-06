# Social networks group posting
This script can help to make a post to ***VK group***, ***Facebook group*** and to ***Telegram Channel***  
In the ***main*** file you will have to fill up all the relevant infomation:
```
vk_group_id = 'GroupID'
vk_user_id = 'Your_User_ID'  
  
fb_group_id = 'Your_facebook_group_id'  
  
tg_chat_id = '@telegram_chanel_name'  
  
picture_path = 'picture_path'
text = 'any text'
```

[About VK Service Token](https://vk.com/dev/access_token?f=3.%20Сервисный%20ключ%20доступа)  
[About telegram](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)  
[About Facebook](https://developers.facebook.com/docs/graph-api/explorer/)

### setting up .env variables   
  You will  have to set your environment variables up with **.env** file where you going to store
  your **ALL YOUR TOKENS + VK LOGIN AND PASSWORD**.  
  

  You can use [Notepad++](https://notepad-plus-plus.org/downloads/) to create this file for Windows,
or [CotEditor](https://coteditor.com/) for MacOS.
  
##### This is an example of how it looks like inside of your .env file. 
(You can choose your own variable names if you want)  
```
VK_ACCESS_TOKEN=YourAccessToken
VK_LOGIN=Your_login
VK_PASSWORD=YourPassword
TG_BOT_TOKEN=Telegram_Bot_Token
FACEBOOK_TOKEN=Your_facebook_token
```
Variables has to be with CAPITAL letters and without any spaces at all!



## How to install  

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Project Goals  
To make life easier
