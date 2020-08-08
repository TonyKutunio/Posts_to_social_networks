import os
import vk_api
from dotenv import load_dotenv
import telegram
import requests
import argparse
import logging


logger = logging.getLogger("Facebook Requests Response")


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
                 owner_id= -vk_group_id,
                 attachments=attachments)


def post_to_fb(picture_path, text):
    url = f"https://graph.facebook.com/v2.11/{fb_group_id}/photos"

    data = {'caption': text,
            'access_token': fb_token,
            }
    with open(picture_path, 'rb') as file:
        files = {'upload_files': file}
        response = requests.post(url, files=files, data=data)
        logger.debug(response.text)
        response.raise_for_status()


def post_to_telegram(picture_path, text):
    bot = telegram.Bot(token=tg_bot_token)
    bot.send_photo(chat_id=tg_chanel_name,
                   photo=open(picture_path, 'rb'))
    bot.send_message(chat_id=tg_chanel_name, text=text)


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description='Takes two arguments.'
                    '1. Text'
                    '2. File Path')

    parser.add_argument('file_path',
                        type=str,
                        help='File path of picture to be posted')

    parser.add_argument('text',
                        type=str,
                        help='Text to be posted')
    return parser


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    logger.setLevel(logging.DEBUG)
    load_dotenv()
    vk_login = os.getenv('VK_LOGIN')
    vk_password = os.getenv('VK_PASSWORD')
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = int(os.getenv('VK_GROUP_ID'))
    vk_user_id = os.getenv('VK_USER_ID')

    fb_token = os.getenv('FACEBOOK_TOKEN')
    fb_group_id = int(os.getenv('FB_GROUP_ID'))

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chanel_name = os.getenv('TG_CHANNEL_NAME')


    parser = get_argument_parser()
    args = parser.parse_args()
    picture_path = args.file_path
    text = args.text

    post_to_vk(picture_path, text)
    post_to_fb(picture_path, text)
    post_to_telegram(picture_path, text)



