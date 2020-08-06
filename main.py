import os
import vk_api
from dotenv import load_dotenv
import telegram
import requests


def post_to_vk(picture_path, text):
    vk_session = vk_api.VkApi(vk_login,
                              vk_password,
                              token=vk_access_token)
    vk_session.auth()
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(picture_path,
                              group_id=vk_group_id,
                              caption=text)
    picture_id = photo[0]['id']
    vk = vk_session.get_api()
    attachments = f'photo{vk_user_id}_{picture_id}'
    vk.wall.post(message=text,
                 owner_id=-vk_group_id,
                 attachments=attachments)


def post_to_fb(picture_path, text):
    url = f"https://graph.facebook.com/v2.11/{fb_group_id}/photos"
    files = {'upload_files': open(picture_path, 'rb')}
    data = {'caption': text,
            'access_token': fb_token,
            }
    response = requests.post(url, files=files, data=data)
    print('Facebook response: ' + response.text)
    response.raise_for_status()


def post_to_telegram(picture_path, text):
    bot = telegram.Bot(token=tg_bot_token)
    bot.send_photo(chat_id=tg_chat_id,
                   photo=open(picture_path, 'rb'))
    bot.send_message(chat_id=tg_chat_id, text=text)



if __name__ == '__main__':
    load_dotenv()
    vk_login = os.getenv('VK_LOGIN')
    vk_password = os.getenv('VK_PASSWORD')
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = 'GroupID'
    vk_user_id = 'Your_User_ID'

    fb_token = os.getenv('FACEBOOK_TOKEN')
    fb_group_id = 'Your_facebook_group_id'

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = '@telegram_chanel_name'

    picture_path = 'picture_path'
    text = 'any text'

    post_to_vk(picture_path, text)
    post_to_fb(picture_path, text)
    post_to_telegram(picture_path, text)


