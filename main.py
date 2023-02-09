from telebot import types
import Constants
from Constants import *
from Constants import bot
from User import User


@bot.message_handler(commands=['start'])
def welcome(message: types.Message, to_print: bool = True, start: bool = True):
    if start:
        welcome_text_message(message.chat.id)
    if type(checkUser(message.from_user, message.chat.id)) == bool:
        to_print = False
    keyboard = make_menu_keyboard()
    if to_print:
        bot.send_message(message.chat.id, text=MENU_TEXT, reply_markup=keyboard)
    else:
        return keyboard


def welcome_by_chat_id(chat_id: int):
    keyboard = make_menu_keyboard()
    bot.send_message(chat_id, text=MENU_TEXT, reply_markup=keyboard)


def make_menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    callback_button_cul = types.InlineKeyboardButton(text="Архив 📚", callback_data=CULTURE_BTN)
    callback_button_mus = types.InlineKeyboardButton(text="Новогодний плейлист 🎶", callback_data=MUSIC_BTN)
    callback_button_aes = types.InlineKeyboardButton(text="Поздравления от АЭС ✨", callback_data=AEC_BTN)
    callback_button_quiz = types.InlineKeyboardButton(text="Квизы 🤫", callback_data=QUIZ_BTN)
    keyboard.add(callback_button_cul)
    keyboard.add(callback_button_mus)
    keyboard.add(callback_button_aes)
    keyboard.add(callback_button_quiz)
    return keyboard


def show_epoches_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    callback_button_1 = types.InlineKeyboardButton(text=Constants.FIRST_NAME,
                                                   url="https://telegra.ph/YAzycheskaya-Rus-12-18")
    callback_button_2 = types.InlineKeyboardButton(text=Constants.SECOND_NAME,
                                                   url="https://telegra.ph/Posle-kreshcheniya-12-18-2")
    callback_button_3 = types.InlineKeyboardButton(text=Constants.THIRD_NAME,
                                                   url="https://telegra.ph/Smutnoe-vremya-12-18")
    callback_button_4 = types.InlineKeyboardButton(text=Constants.FOURTH_NAME,
                                                   url="https://telegra.ph/EHpoha-Petra-I-12-18-2")
    callback_button_5 = types.InlineKeyboardButton(text=Constants.FIFTH_NAME,
                                                   url="https://telegra.ph/Sovetskoe-vremya-12-18")
    callback_button_6 = types.InlineKeyboardButton(text=Constants.SIXTH_NAME,
                                                   url="https://telegra.ph/Nashe-vremya-12-18")
    callback_button_7 = types.InlineKeyboardButton(text="Вернуться к архиву", callback_data=BACK_TO_CULTURE_BTN)
    keyboard.add(callback_button_1, callback_button_2)
    keyboard.add(callback_button_3, callback_button_4)
    keyboard.add(callback_button_5, callback_button_6)
    keyboard.add(callback_button_7)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    user = checkUser(call.from_user)
    if call.message:
        # sendDataToMe(call.data + "\n" + user.toString(), False)
        if call.data == MUSIC_BTN:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            show_music_posts(call.message, user)
        if call.data == NEXT_MUS_BTN:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text,
                                  reply_markup=edit_music_keyboard(MUSIC_DICT[call.message.text].yandex_link))
            user.increase_music_post_cnt()
            show_music_posts(call.message, user)
        if call.data == PREV_MUS_BTN:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text,
                                  reply_markup=edit_music_keyboard(MUSIC_DICT[call.message.text].yandex_link))
            user.decrease_music_post_cnt()
            show_music_posts(call.message, user)
        if call.data == AEC_BTN:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            show_aes_posts(call.message, user)

        if call.data == NEXT_AES_BTN:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open(AES_DICT[call.message.caption].picture, "rb"),
                                                               caption=call.message.caption))
            user.increase_aes_post_cnt()
            show_aes_posts(call.message, user)

        if call.data == PREV_AES_BTN:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open(AES_DICT[call.message.caption].picture, "rb"),
                                                               caption=call.message.caption))
            user.decrease_aes_post_cnt()
            show_aes_posts(call.message, user)

        if call.data == CULTURE_BTN:
            new_text, new_keyboard = show_culture_posts(user)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text,
                                  reply_markup=new_keyboard)
        if call.data == NEXT_CULT_BTN:
            user.increase_culture_post_cnt()
            new_text, new_keyboard = show_culture_posts(user)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text,
                                  reply_markup=new_keyboard)
            show_culture_posts(user)
        if call.data == PREV_CULT_BTN:
            user.decrease_culture_post_cnt()
            new_text, new_keyboard = show_culture_posts(user)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text,
                                  reply_markup=new_keyboard)
        if call.data == MAIN_MENU_BTN:
            if call.message.text in MUSIC_DICT:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=call.message.text,
                                      reply_markup=edit_music_keyboard(MUSIC_DICT[call.message.text].yandex_link))
                welcome(call.message, True, False)
            elif call.message.caption and call.message.caption in AES_DICT:
                bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                       media=types.InputMediaPhoto(open(AES_DICT[call.message.caption].picture, "rb"),
                                                                   caption=call.message.caption))
                welcome(call.message, True, False)
            else:
                new_keyboard = welcome(call.message, False, False)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=MENU_TEXT,
                                      reply_markup=new_keyboard)
        if call.data == "Окунуться в атмосферу":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери интересующую эпоху",
                                  reply_markup=show_epoches_keyboard())
        if call.data == BACK_TO_CULTURE_BTN:
            new_text, new_keyboard = show_culture_posts(user)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text,
                                  reply_markup=new_keyboard)
        if call.data == "day 2":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/days/day_2.png", "rb"),
                                                               caption="До Нового года всего 2 дня!\nА вы написали письмо Деду Морозу? 💌"))
            welcome(call.message, True, False)

        if call.data == "back to menu from info quiz post":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/first_quiz.png", "rb"),
                                                               caption="Новый год наступил, но мы продолжаем поддерживать атмосферу праздника для вас 🎉\n\n<i><b>«Квизы»</b></i> - cамый долгожданный раздел - наконец стал активен!\n\nНа какую же тему мы подготовили первый квиз? 🤫",
                                                               parse_mode="HTML"))
            welcome(call.message, True, False)
    # QUIZ
    if call.data == QUIZ_BTN:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбери квиз",
                              reply_markup=make_keyboard_for_quiz())

    if call.data in NEW_YEAR_Q_QUESTION_CALLBACKS:
        if call.data == NEW_YEAR_Q_BTN:
            user.add_new_year_quiz(call.message.message_id)
        cur_quiz = user.get_new_year_quiz(call.message)
        next_question = NEW_YEAR_Q_QUESTION_CALLBACKS[call.data]
        if call.data in NEW_YEAR_Q_QUESTION_RIGHT:
            cur_quiz.score[next_question - 1] = 1
        if next_question == 13:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(call.message.chat.id, photo=open(get_new_year_quiz_result(sum(cur_quiz.score)), "rb"))

            user.delete_new_year_quiz(call.message.message_id)
            welcome(call.message, True, False)
        else:
            question_text, keyboard = get_quiz_data(next_question, sum(cur_quiz.score))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=question_text, parse_mode="HTML",
                                  reply_markup=keyboard)

    if call.data == CHARACTER_QUIZ_NAME:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=CHARACTER_QUIZ_START_MESSAGE,
                              reply_markup=make_keyboard_for_starting_character_quiz())

    if call.data == START_CHARACTER_QUIZ:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        msg_id = edit_or_send_character_quiz_question(user, call.message, 1)
        user.add_character_quiz(msg_id)

    if call.data in CHARACTER_QUIZ_QUESTION_CALLBACKS:
        try:
            cur_question_num = user.update_character_quiz_score(call.message,
                                                                CHARACTER_QUIZ_QUESTION_CALLBACKS.index(call.data) + 1)
            edit_or_send_character_quiz_question(user, call.message, cur_question_num + 1)
        except FileNotFoundError:
            bot.send_message(call.message.chat.id, "К сожалению, что-то пошло не так с нашей стороны(\nПожалуйста, нажмите на /start и попробуйте снова")

    if call.data in REVERSER_CHARACTER_LIST:
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               media=types.InputMediaPhoto(open(
                                   f"media/CharacterQuizPics/res-{REVERSER_CHARACTER_LIST[call.data][0]}.png", "rb")),
                               reply_markup=make_keyboard_for_ending_character_quiz(REVERSER_CHARACTER_LIST[call.data][1], REVERSER_CHARACTER_LIST[call.data][2]))
        user.delete_character_quiz(call.message.message_id)
        welcome(call.message, True, False)

    if call.data == BACK_TO_MENU_FROM_POST:
        # bot.send_message(MY_ID, call.message.caption)
        if call.message.caption == "До шуток про прошлогодний хлеб всего 6 дней!\n\nКстати уже сегодня добавим поздравления от АЭС 🔥":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/days/day_6.png", "rb"),
                                                               caption="До шуток про прошлогодний хлеб всего 6 дней!\n\nКстати, уже сегодня добавим поздравления от АЭС 🔥"))

        elif call.message.caption.split()[0] == "\"Академик":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/aes_photos/aes_10.jpg", "rb"),
                                                               caption="\"Академик Ломоносов\" — первая и единственная плавучая АЭС. Сейчас находится в городе Певек на Чукотке и является самой северной АЭС мира!",
                                                               parse_mode="HTML"))
        elif call.message.caption.split()[0] == "Остается":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/days/day_5.png", "rb"),
                                                               caption="Остается всего 5 дней до Нового года!\nУже "
                                                                       "придумали, что загадаете? 🎉"))
        elif call.message.caption.split()[0] == "До":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/days/day_4.png", "rb"),
                                                               caption="До Нового года 4 дня! Приготовили подарки родным? 🎁"))
        elif call.message.caption.split()[0] == "Рассказываем":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/bear_and_queen.jpg", "rb"),
                                                               caption="Рассказываем о медвежонке, которому удалось выпить чаю с королевой Великобритании 🐻"))
        elif call.message.caption.split()[0] == "Новый":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/days/day_3.png", "rb"),
                                                               caption="Новый год уже через 3 дня ✨"))
        elif "Ольга Рождественская и ВИА «Добры молодцы» – Песенка о снежинке" in call.message.caption:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/snowflake.jpg", "rb"),
                                                               caption="В новогоднем плейлисте новинка: <i><b>Ольга Рождественская и ВИА «Добры молодцы» – Песенка о снежинке</b></i> из фильма «Чародеи».\n\nПесня могла вовсе не появиться в фильме, о чём рассказываем внизу в мини-статье.\n\nКак всегда, добавили для вас песню в новогодний плейлист ;)",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Рассказываем тут",
                                                                                "https://telegra.ph/Olga-Rozhdestvenskaya-i-VIA-Dobry-molodcy--Pesenka-o-snezhinke-01-04"))
        elif "Танец Феи Драже из балета «Щелкунчик»" in call.message.caption:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/balet.jpg", "rb"),
                                                               caption="В новогоднем плейлисте новинка: <i><b>Пётр Ильич Чайковский — Танец Феи Драже из балета «Щелкунчик»</b></i>\n\nЧайковский использовал для этой композиции довольно необычный инструмент. Какой же? Узнаете в мини-статье!",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Читать мини-статью 📃",
                                                                                "https://telegra.ph/Pyotr-Ilich-CHajkovskij--Tanec-Fei-Drazhe-iz-baleta-SHCHelkunchik-01-07"))
        elif "Queen — Thank God It's Christmas" in call.message.caption:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/queen.jpg", "rb"),
                                                               caption="В новогоднем плейлисте новинка: <i><b>Queen — Thank God It's Christmas</b></i>.\n\nО неизвестной для многих песне рок-группы Queen в мини-статье 🎸",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Про Рождественский сингл",
                                                                                "https://telegra.ph/Queen---Thank-God-Its-Christmas-01-10"))
        elif "В 2022 году исполнилось 130 лет" in call.message.caption:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/big_ballet.jpg", "rb"),
                                                               caption="В 2022 году исполнилось 130 лет, пожалуй, самому новогоднему и известному балету в мире — «Щелкунчику» Петра Ильича Чайковского. В честь юбилея кратко вспоминаем о том, как создавался балет. И предлагаем прикоснуться к классике, впервые или вновь.",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Самый знаменитый балет в мире 🩰",
                                                                                "https://telegra.ph/Baletu-SHCHelkunchik--130-let-01-11"))
        elif "В новогодние праздники мы проводим много времени с семьёй" in call.message.caption:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/family.jpg", "rb"),
                                                               caption="В новогодние праздники мы проводим много времени с семьёй. И чтобы это время проходило с пользой, бизнес-сторителлер Артем Мушин-Македонский поделился с нами вопросами, благодаря которым вы только больше станете гордиться собой и семьёй 👨‍👩‍👧",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Поводы гордиться собой и семьёй",
                                                                                "https://telegra.ph/9-voprosov-dlya-semejnoj-posidelki-01-11"))
        elif call.message.caption.split()[0] == "В":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/prostokvashino.jpg", "rb"),
                                                               caption="В новогоднем плейлисте новинка: <i><b>Валентина Толкунова - Кабы не было зимы</b></i> из мультика Простоквашино.\nА ниже можете почитать, над чем ещё работали авторы песни ❄",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Об авторах песни",
                                                                                "https://telegra.ph/Valentina-Tolkunova---Kaby-ne-bylo-zimy-12-29"))
        elif call.message.caption.split()[0] == "Добавили" and call.message.caption.split()[1] == "новинку":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/TOP.jpg", "rb"),
                                                               caption="Добавили новинку в новогодний плейлист: <i><b>twenty one pilots — Christmas Saves the Year</b></i>\n\nОт лица кого ведётся повествование в песне? Узнаете в мини-статье по кнопке внизу",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("тык",
                                                                                "https://telegra.ph/twenty-one-pilots--Christmas-Saves-the-Year-01-05-2"))

        elif call.message.caption.split()[0] == "Добавили":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/aes_photos/welcome_aes_pic.jpg", "rb"),
                                                               caption=WELCOME_AES_TEXT, parse_mode="HTML"))

        elif call.message.caption.split()[0] == "Новинка":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/wonderful_dreams.jpg", "rb"),
                                                               caption="Новинка в новогоднем плейлисте: <b><i>Melanie Thornton - Wonderful dream (Holidays are coming)</i></b> 🎄\n\nРассказываем об оригинале, с которым вы хорошо знакомы по адаптации песни для российского телевидения!",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("О новогоднем хите",
                                                                                "https://telegra.ph/Melanie-Thornton---Wonderful-dream-Holidays-are-coming-12-29"))
        elif call.message.caption.split()[0] == "Остался":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/days/day_1.png", "rb"),
                                                               caption="Остался всего 1 день до Нового года!"))
        elif call.message.caption.split()[0] == "Не":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/kuranty.png", "rb"),
                                                               caption="Не упусти заветную минуту ❤✨"))
        elif call.message.caption.split()[0] == "Всегда":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/moscow.jpg", "rb"),
                                                               caption="Всегда хотели прогуляться по новогодней Москве, но никак не получалось? Мы подготовили виртуальную прогулку для вас! Правда, с небольшим сюрпризом — прогулка по Москве <b>столетней давности</b>!",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Вперед в прошлое 🚂",
                                                                                "https://telegra.ph/Kak-starinnaya-Moskva-vstrechala-Novyj-god-12-29"))
        elif call.message.caption == "У многих людей есть традиция подводить итоги года. Кто-то вспоминает самые тёплые моменты, кто-то записывает все достижения за год, а кто-то вспоминает всех встреченных за год людей.  Но и у гигантских корпораций тоже есть свой способ подводить итоги года 🗓":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/google.jpg", "rb"),
                                                               caption="У многих людей есть традиция подводить итоги года. Кто-то вспоминает самые тёплые моменты, кто-то записывает все достижения за год, а кто-то вспоминает всех встреченных за год людей.  Но и у гигантских корпораций тоже есть свой способ подводить итоги года 🗓",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Год в поиске",
                                                                                "https://telegra.ph/God-v-poiske-01-06"))
        elif call.message.caption == "Кажется, что Новый год всегда праздновали так, как мы все привыкли видеть. Но что, если мы скажем, что на самом деле вы празднуете Рождество? Ниже можете почитать о том, как Рождество Христово замещали Новым годом\n\nС праздником вас! Теперь вы будете знать, что у вас есть ещё один шанс, если вы пропустили празднование 31 декабря 😉":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/christmas.jpg", "rb"),
                                                               caption="Кажется, что Новый год всегда праздновали так, как мы все привыкли видеть. Но что, если мы скажем, что на самом деле вы празднуете Рождество? Ниже можете почитать о том, как Рождество Христово замещали Новым годом\n\nС праздником вас! Теперь вы будете знать, что у вас есть ещё один шанс, если вы пропустили празднование 31 декабря 😉",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Как отменяли Рождество",
                                                                                "https://telegra.ph/Skaz-o-tom-kak-Rozhdestvo-Novym-godom-zameshchali-01-07"))
        elif call.message.caption.split()[0] == "Надеемся,":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/balls.jpg", "rb"),
                                                               caption="Надеемся, что ваша красавица-ёлка всё ещё с вами и греет сердце в начавшуюся рабочую неделю! Сегодня мы поведаем о том, как и почему на ёлку стали вешать шары 🎄",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Как появились новогодние шары",
                                                                                "https://telegra.ph/Istoriya-novogodnih-sharov-01-09"))

        elif call.message.caption.split()[0] == "Ну":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/new_old_year.jpg", "rb"),
                                                               caption="Ну что, со Старым Новым годом! Кстати, а вы знаете, как Новый год стал «старым»? Тогда читайте небольшую статью на эту тему",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("Как появился второй Новый год?",
                                                                                "https://telegra.ph/Kak-poyavilsya-Staryj-Novyj-god-01-14"))
        elif "У нас для тебя есть" in call.message.caption:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/character_quiz.jpg", "rb"),
                                                               caption="У нас для тебя есть <b>сюрприз</b>\n\nХоть мы и обещали, что работа бота продлится до 14 января, но мы не могли не сделать небольшой сюрприз напоследок! В боте появился <b>новый квиз «Кто ты из персонажей мультфильмов?»</b>. А сам бот будет работать ещё какое-то время, чтобы каждый мог прикоснуться к нему!\n\nСпасибо, что были с нами эти новогодние праздники. Еще не прощаемся, впереди много интересного вместе с Советом юниоров Росатома ❤️\n\n<i><b>Твой новогодний друг</b></i>",
                                                               parse_mode="HTML"))
        elif call.message.caption == "Всем привет! Настала пора прощаться)\n\nОстаются последние сутки работы бота, поэтому не упустите возможность прочитать вышедшие ранее статьи или пройти квизы, если откладывали это на потом ❤":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/attention.jpg", "rb"),
                                                               caption="Всем привет! Настала пора прощаться)\n\nОстаются последние сутки работы бота, поэтому не упустите возможность прочитать вышедшие ранее статьи или пройти квизы, если откладывали это на потом ❤",
                                                               parse_mode="HTML"))
        elif call.message.caption == "А еще у нас есть к вам небольшая просьба)\nЧтобы в следующий раз бот стал ещё круче, оставьте обратную связь в небольшой формочке!\nНам правда важно ваше мнение 🎅🏻❤":
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/back_form.jpg", "rb"),
                                                               caption="А еще у нас есть к вам небольшая просьба)\nЧтобы в следующий раз бот стал ещё круче, оставьте обратную связь в небольшой формочке!\nНам правда важно ваше мнение 🎅🏻❤",
                                                               parse_mode="HTML"),
                                   reply_markup=make_new_keyboard_for_sent_post("тык для формочки",
                                                                                "https://forms.yandex.ru/cloud/63d6475f43f74f9671216351/"))
        else:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(open("media/posts_pics/last_christmas_pic.jpg", "rb"),
                                                               caption=POST_MSG, parse_mode="HTML"))

        welcome(call.message, True, False)


def show_culture_posts(user):
    cur_post, num = user.get_cur_culture_post()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if cur_post.additional_btn is not None:
        if cur_post.url:
            callback_button_additional = types.InlineKeyboardButton(text=cur_post.additional_btn, url=cur_post.url)
        else:
            callback_button_additional = types.InlineKeyboardButton(text=cur_post.additional_btn,
                                                                    callback_data=cur_post.additional_btn)
        keyboard.add(callback_button_additional)
    if num == 0:
        callback_button_back = types.InlineKeyboardButton(text=BACK_TEXT, callback_data=PREV_CULT_BTN)
        callback_button_next = types.InlineKeyboardButton(text=NEXT_TEXT, callback_data=NEXT_CULT_BTN)
        keyboard.add(callback_button_back, callback_button_next)
    if num == -1:
        callback_button_next = types.InlineKeyboardButton(text=NEXT_TEXT, callback_data=NEXT_CULT_BTN)
        keyboard.add(callback_button_next)
    if num == 1:
        callback_button_back = types.InlineKeyboardButton(text=BACK_TEXT, callback_data=PREV_CULT_BTN)
        keyboard.add(callback_button_back)
    callback_button_back_to_menu = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=MAIN_MENU_BTN)
    keyboard.add(callback_button_back_to_menu)
    return cur_post.text, keyboard


def show_music_posts(message, user):
    cur_post, num = user.get_cur_music_post()

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if num == 0:
        callback_button_back = types.InlineKeyboardButton(text=BACK_TEXT, callback_data=PREV_MUS_BTN)
        callback_button_next = types.InlineKeyboardButton(text=NEXT_TEXT, callback_data=NEXT_MUS_BTN)
        keyboard.add(callback_button_back, callback_button_next)
    if num == -1:
        callback_button_next = types.InlineKeyboardButton(text=NEXT_TEXT, callback_data=NEXT_MUS_BTN)
        keyboard.add(callback_button_next)
    if num == 1:
        callback_button_back = types.InlineKeyboardButton(text=BACK_TEXT, callback_data=PREV_MUS_BTN)
        keyboard.add(callback_button_back)

    callback_button_go_to_yandex = types.InlineKeyboardButton(text=YANDEX_LINK_TEXT, url=cur_post.yandex_link,
                                                              callback_data=LISTEN_ON_YANDEX_BTN)
    callback_button_back_to_menu = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=MAIN_MENU_BTN)
    keyboard.add(callback_button_go_to_yandex)
    keyboard.add(callback_button_back_to_menu)

    bot.send_video_note(message.chat.id, thumb=True, data=open(cur_post.video, "rb"))
    bot.send_message(message.chat.id, cur_post.description, reply_markup=keyboard)


def show_aes_posts(message, user):
    cur_post, num = user.get_cur_aes_post()

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if num == 0:
        callback_button_back = types.InlineKeyboardButton(text=BACK_TEXT, callback_data=PREV_AES_BTN)
        callback_button_next = types.InlineKeyboardButton(text=NEXT_TEXT, callback_data=NEXT_AES_BTN)
        keyboard.add(callback_button_back, callback_button_next)
    if num == -1:
        callback_button_next = types.InlineKeyboardButton(text=NEXT_TEXT, callback_data=NEXT_AES_BTN)
        keyboard.add(callback_button_next)
    if num == 1:
        callback_button_back = types.InlineKeyboardButton(text=BACK_TEXT, callback_data=PREV_AES_BTN)
        keyboard.add(callback_button_back)

    callback_button_back_to_menu = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=MAIN_MENU_BTN)
    keyboard.add(callback_button_back_to_menu)

    bot.send_photo(message.chat.id, open(cur_post.picture, "rb"), caption=cur_post.caption, reply_markup=keyboard)


def checkUser(from_user: types.User, chat_id: int = 0):
    if int(chat_id) < 0:
        bot.send_message(chat_id, "Пока что я плохо работаю в групповых чатах(\nПишите мне лично!")
        return False
    if from_user.id not in Constants.USER:
        user = User(from_user.id, from_user.first_name, from_user.last_name, from_user.username)
        Constants.USER[from_user.id] = user
    else:
        user = Constants.USER[from_user.id]
    return user


def sendDataToMe(user, new_user: bool):
    if new_user:
        add_user_data(user)
        bot.send_message(Constants.MY_ID, "new user:\n" + user.toString())
    else:
        bot.send_message(Constants.MY_ID, "action:\n" + user)


def edit_music_keyboard(link):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    callback_button_go_to_yandex = types.InlineKeyboardButton(text=YANDEX_LINK_TEXT, url=link,
                                                              callback_data=LISTEN_ON_YANDEX_BTN)
    keyboard.add(callback_button_go_to_yandex)
    return keyboard


def add_user_data(user: types.User):
    file = open("metadata/user_info.txt", "a")
    data = str(user.id) + "," + str(user.first_name) + "," + str(user.last_name) + "," + str(user.username) + "\n"
    file.write(data)
    file.close()


def upload_users():
    file = open("metadata/user_info.txt", "r")
    for line in file:
        user_data = line.split(',')
        user = User(int(user_data[0]), get_str_or_None(user_data[1]),
                    get_str_or_None(user_data[2]), get_str_or_None(user_data[3]))
        if user.id not in Constants.USER:
            Constants.USER[user.id] = user
    file.close()


def get_str_or_None(str: str):
    if str == "None":
        return None
    return str


def welcome_text_message(chat_id):
    bot.send_message(chat_id, Constants.START_MESSAGE, parse_mode='HTML')
    bot.send_photo(chat_id, photo=open("media/posts_pics/welcome_pic.jpeg", "rb"))


def make_new_keyboard_for_sent_post(button_text: str, link: str):
    keyboard = types.InlineKeyboardMarkup()
    callback_button_back_to_menu = types.InlineKeyboardButton(text=button_text, url=link)
    keyboard.add(callback_button_back_to_menu)
    return keyboard


def make_keyboard_for_quiz():
    keyboard = types.InlineKeyboardMarkup()
    first_quiz_btn = types.InlineKeyboardButton(text="Обо всём новогоднем", callback_data=NEW_YEAR_Q_BTN)
    second_quiz_btn = types.InlineKeyboardButton(text="Кто ты из персонажей мультфильмов",
                                                 callback_data=CHARACTER_QUIZ_NAME)
    callback_button_back_to_menu = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=MAIN_MENU_BTN)
    keyboard.add(first_quiz_btn)
    keyboard.add(second_quiz_btn)
    keyboard.add(callback_button_back_to_menu)
    return keyboard


def get_quiz_data(question_num: int, score: int):
    info_text = f"❓ Вопрос {question_num} из {len(Constants.NEW_YEAR_Q_QUESTIONS)}\n✅ Верно {score} из {question_num - 1}\n\n"

    cur_question = NEW_YEAR_Q_QUESTIONS[question_num]
    keyboard = types.InlineKeyboardMarkup()
    if cur_question.answer_num == 0:
        first_btn = types.InlineKeyboardButton(text=cur_question.options[0],
                                               callback_data=cur_question.options_callbacks[0])
    else:
        first_btn = types.InlineKeyboardButton(text=cur_question.options[0],
                                               callback_data=cur_question.options_callbacks[1])
    if cur_question.answer_num == 1:
        second_btn = types.InlineKeyboardButton(text=cur_question.options[1],
                                                callback_data=cur_question.options_callbacks[0])
    else:
        second_btn = types.InlineKeyboardButton(text=cur_question.options[1],
                                                callback_data=cur_question.options_callbacks[1])
    if cur_question.answer_num == 2:
        third_btn = types.InlineKeyboardButton(text=cur_question.options[2],
                                               callback_data=cur_question.options_callbacks[0])
    else:
        third_btn = types.InlineKeyboardButton(text=cur_question.options[2],
                                               callback_data=cur_question.options_callbacks[1])
    if cur_question.answer_num == 3:
        fourth_btn = types.InlineKeyboardButton(text=cur_question.options[3],
                                                callback_data=cur_question.options_callbacks[0])
    else:
        fourth_btn = types.InlineKeyboardButton(text=cur_question.options[3],
                                                callback_data=cur_question.options_callbacks[1])
    back_to_main_menu_btn = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=MAIN_MENU_BTN)
    keyboard.add(first_btn)
    keyboard.add(second_btn)
    keyboard.add(third_btn)
    keyboard.add(fourth_btn)
    keyboard.add(back_to_main_menu_btn)
    return info_text + cur_question.question, keyboard


def keyboard_with_back_to_main_menu_btn():
    keyboard = types.InlineKeyboardMarkup()
    callback_button_back_to_menu = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT,
                                                              callback_data=BACK_TO_MENU_FROM_POST)
    keyboard.add(callback_button_back_to_menu)
    return keyboard


def get_new_year_quiz_result(score: int):
    return f"media/new_year_quiz_pics/{score}.png"


def edit_or_send_character_quiz_question(user: User, message: types.Message, question_num):
    if question_num == 19:
        end_character_quiz(user, message)
        return
    question = CHARACTER_QUIZ_QUESTIONS[question_num]
    keyboard = make_keyboard_for_character_quiz(question.options_list)
    if question_num == 1:
        msg_id = bot.send_photo(message.chat.id, photo=open("media/CharacterQuizPics/1.png", "rb"),
                                reply_markup=keyboard)
        return msg_id.message_id
    bot.edit_message_media(media=types.InputMediaPhoto(open(question.picture, "rb")),
                           chat_id=message.chat.id, message_id=message.message_id, reply_markup=keyboard)


def end_character_quiz(user: User, message: types.Message):
    cur_quiz = user.get_character_quiz(message)
    res = get_character_quiz_result(cur_quiz.score)
    picture = f"media/CharacterQuizPics/res-{res - 1}.png"
    bot.edit_message_media(media=types.InputMediaPhoto(open(picture, "rb"), caption="Поздравляем! Вы прошли квиз 🎉"),
                           chat_id=message.chat.id, message_id=message.message_id,
                           reply_markup=make_back_to_menu_btn_for_ending_character_quiz(res))


def get_character_quiz_result(score: list):
    max_score = -1
    res = -1
    for i in range(1, 7):
        cur_score = score.count(i)
        if cur_score > max_score:
            max_score = cur_score
            res = i
    return res


def make_keyboard_for_character_quiz(options: list):
    keyboard = types.InlineKeyboardMarkup()
    first_btn = types.InlineKeyboardButton(text="1", callback_data=CHARACTER_QUIZ_QUESTION_CALLBACKS[options[0] - 1])
    second_btn = types.InlineKeyboardButton(text="2", callback_data=CHARACTER_QUIZ_QUESTION_CALLBACKS[options[1] - 1])
    third_btn = types.InlineKeyboardButton(text="3", callback_data=CHARACTER_QUIZ_QUESTION_CALLBACKS[options[2] - 1])
    fourth_btn = types.InlineKeyboardButton(text="4", callback_data=CHARACTER_QUIZ_QUESTION_CALLBACKS[options[3] - 1])
    fifth_btn = types.InlineKeyboardButton(text="5", callback_data=CHARACTER_QUIZ_QUESTION_CALLBACKS[options[4] - 1])
    sixth_btn = types.InlineKeyboardButton(text="6", callback_data=CHARACTER_QUIZ_QUESTION_CALLBACKS[options[5] - 1])
    keyboard.add(first_btn, second_btn)
    keyboard.add(third_btn, fourth_btn)
    keyboard.add(fifth_btn, sixth_btn)
    return keyboard


def make_keyboard_for_starting_character_quiz():
    keyboard = types.InlineKeyboardMarkup()
    first_btn = types.InlineKeyboardButton(text="Начать квиз", callback_data=START_CHARACTER_QUIZ)
    second_btn = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=MAIN_MENU_BTN)
    keyboard.add(first_btn)
    keyboard.add(second_btn)
    return keyboard


def make_back_to_menu_btn_for_ending_character_quiz(res: int):
    character_callback = CHARACTERS_LIST[res - 1]
    keyboard = make_keyboard_for_ending_character_quiz(REVERSER_CHARACTER_LIST[character_callback][1],
                                                       REVERSER_CHARACTER_LIST[character_callback][2])
    first_btn = types.InlineKeyboardButton(text=BACK_TO_MENU_TEXT, callback_data=character_callback)
    keyboard.add(first_btn)
    return keyboard


def make_keyboard_for_ending_character_quiz(btn_name: str, link: str):
    keyboard = types.InlineKeyboardMarkup()
    first_btn = types.InlineKeyboardButton(text=btn_name, url=link)
    keyboard.add(first_btn)
    return keyboard


if __name__ == '__main__':
    upload_users()
    bot.polling(none_stop=True)
