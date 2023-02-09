from telebot import types
import time
from Constants import *


class SendMessageClass:

    def __get_users(self):
        file = open("metadata/user_info.txt", "r")
        cur_users = set()
        for line in file:
            cur_users.add(int(line.strip().split(',')[0]))
        file.close()
        return cur_users

    def __make_keyboard_with_back_to_menu_btn(self):
        keyboard = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=BACK_TO_MENU_FROM_POST)
        keyboard.add(btn_1)
        return keyboard

    def __make_keyboard_with_url_and_back_to_menu_btn(self, btn_text: str, url: str):
        keyboard = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text=btn_text, url=url)
        btn_2 = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=BACK_TO_MENU_FROM_POST)
        keyboard.add(btn_1)
        keyboard.add(btn_2)
        return keyboard

    def sendCultureMessage(self, picture: str, pic_caption: str, btn_text: str, url: str, onlyToMe: bool = False):
        cur_users = self.__get_users()
        for i in cur_users:
            if i != BOT_ID:
                if onlyToMe and i != MY_PERSONAL_ID:
                    continue
                time.sleep(1)
                try:
                    bot.send_photo(i, photo=open(picture, "rb"),
                                   caption=pic_caption,
                                   reply_markup=self.__make_keyboard_with_url_and_back_to_menu_btn(btn_text, url),
                                   parse_mode="HTML")
                except:
                    print("User blocked bot, id: ", i)

    def sendPostMessage(self, picture: str, pic_caption: str, onlyToMe: bool = False):
        cur_users = self.__get_users()
        for i in cur_users:
            if i != BOT_ID:
                if onlyToMe and i != MY_PERSONAL_ID:
                    continue
                time.sleep(1)
                try:
                    bot.send_photo(i, photo=open(picture, "rb"),
                                   caption=pic_caption,
                                   reply_markup=self.__make_keyboard_with_back_to_menu_btn(),
                                   parse_mode="HTML")
                except:
                    print("User blocked bot, id: ", i)
