# Social networks group posting
This script can help to make a post to ***VK group***, ***Facebook group*** and to ***Telegram Channel***.   
To start the scrip you'll have to type in console:  
`$python main.py picture_path text`  
As you can see it takes two arguments: picture_path and text.  
But before that you have to set up all the things as below.



### setting up .env variables:
  You will  have to set your environment variables up with **.env** file where you going to store
  all your relevant infomation as in example below.
  

  You can use [Notepad++](https://notepad-plus-plus.org/downloads/) to create this file for Windows,
or [CotEditor](https://coteditor.com/) for MacOS.   


[About VK Service Token](https://vk.com/dev/access_token?f=3.%20Сервисный%20ключ%20доступа)   
[About telegram](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)   
[About Facebook](https://developers.facebook.com/docs/graph-api/explorer/)   
  
##### This is an example of how it looks like inside of your .env file. 
```
VK_ACCESS_TOKEN=YourAccessToken
VK_LOGIN=Your_login
VK_PASSWORD=YourPassword
VK_GROUP_ID=Vk Group id
VK_USER_ID=Vk_User_ID

FACEBOOK_TOKEN=Your_facebook_token
FB_GROUP_ID=Fb_GroupId

TG_BOT_TOKEN=Telegram_Bot_Token
TG_CHANNEL_NAME=@telegram_chanel_name
```
Variables has to be with CAPITAL letters and without any spaces at all!

## How to install:  

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Project Goal:
To make life easier.
