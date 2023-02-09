import telebot

from CharacterQuizQuestion import CharacterQuizQuestion
from QuizQuestion import NewYearQuizQuestion
from CulturePost import CulturePost
from MusicPost import MusicPost

from aes_post import AesPost

TOKEN = ""
bot = telebot.TeleBot(TOKEN)
MY_ID = -848974389
BOT_ID = 5675207455
MY_PERSONAL_ID = 506954303

CULTURE_BTN = "culture_btn"
MUSIC_BTN = "music_btn"
AEC_BTN = "aes_btn"
QUIZ_BTN = "quiz_btn"
NEXT_CULT_BTN = "next_cult_btn"
NEXT_MUS_BTN = "next_mus_btn"
PREV_CULT_BTN = "prev_cult_btn"
PREV_MUS_BTN = "prev_mus_btn"
MAIN_MENU_BTN = "back to menu"
LISTEN_ON_YANDEX_BTN = "listen on yandex"
BACK_TO_CULTURE_BTN = "back to culture"
MENU_TEXT = "Выбери раздел"
YANDEX_LINK_TEXT = "Слушать на Яндекс.Музыке"
BACK_TEXT = "Назад"
NEXT_TEXT = "Далее"
BACK_TO_MENU_TEXT = "Вернуться в меню 💫"
SOON_CAPTION = "Скоро добавим 👀"
BACK_TO_MENU_FROM_POST = "back to menu from post"

USER = {}

START_MESSAGE = "Привет! Я – бот, помощник Деда Мороза 🎅 Меня создал <b>Совет юниоров Росатома</b>.\n\nЕсли ты в поисках новогоднего настроения или просто хочешь окунуться в праздичную атмосферу, то я помогу ✨\n\nКаждый день здесь будут появляться новые истории и музыкальные хиты, а у меня – новые функции! Если вдруг что-то пропустил, то не забудь нажать кнопку <i>«Архив»</i>, там уже много интересного.\n\nДелись мной с родными, коллегами, друзьями. Будет повод растопить лёд (если он есть) и поговорить ❄"

POST_MSG = """🎶 <b>Wham! — Last Christmas</b>\n\nОдна из самых популярных песен, связанных с Рождеством, записанная дуэтом ещё а 1984 году.\n\nУзнайте, кто записывал каверы на эту песню, какие игры появлись благодаря ей и посмотрите клип! 🎬\nВсе это можно сделать, нажав на кнопку "Узнать подробнее" или в разделе "Архив"!\n\nТакже мы добавили композицию с пластникой в наш новогодний плейлист, приятного прослушивания! ❤🎧"""

FIRST_NAME = "Языческая Русь"
SECOND_NAME = "После крещения"
THIRD_NAME = "Смутное время"
FOURTH_NAME = "Эпоха Петра I"
FIFTH_NAME = "Советское время"
SIXTH_NAME = "Наше время"

INTRO = "Какой был Новый год сто лет назад? Что изменилось с тех пор?\n\nПочувствуй себя потомственным дворянином на балу в новогоднюю ночь, боярином во время праздничного пира, окунись в атмосферу целой эпохи! ✨"
INTRO_FILM = "Декабрь – время для марафона Новогоднего кино! 🎬"
INTRO_COKE = "Как Coca-Cola стала символом Нового года? 🥤"
INTRO_WHAM = "Про одну из самых популярных Рождественских песен 🎧"
INTRO_BEAR = "Рождественская история медвежонка, ставшего символом праздника для миллионов 🐻"
INTRO_MOSCOW = "Виртуальная прогулка по новогодней старинной Москве"
INTRO_GOOGLE = "Как подводит итоги года Google"
INTRO_CHRISTMAS = "Про Рождество Христово ... Или всё же Новый год? 🤔"
INTRO_BALLS = "Надеемся, что ваша красавица-ёлка всё ещё с вами и греет сердце в начавшуюся рабочую неделю! Сегодня мы поведаем о том, как и почему на ёлку стали вешать шары 🎄"
INTRO_BALLET = "Предлагаем вспомнить о великом произведении, написанном Чайковским ещё в XIX веке."
INTRO_FAMILY = "Как с пользой провести время вместе с семьёй 👨‍👩‍👧"
INTRO_NEW_OLD_YEAR = "О том, как мы стали праздновать два Новых года"

CULTURE_POSTS = [
    CulturePost(INTRO_NEW_OLD_YEAR, "Ещё один праздник", "https://telegra.ph/Kak-poyavilsya-Staryj-Novyj-god-01-14"),
    CulturePost(INTRO_FAMILY, "Поводы гордиться собой и семьёй",
                "https://telegra.ph/9-voprosov-dlya-semejnoj-posidelki-01-11"),
    CulturePost(INTRO_BALLET, "Самый знаменитый балет в мире 🩰",
                "https://telegra.ph/Baletu-SHCHelkunchik--130-let-01-11"),
    CulturePost(INTRO_BALLS, "Как появились новогодние шары?", "https://telegra.ph/Istoriya-novogodnih-sharov-01-09"),
    CulturePost(INTRO_CHRISTMAS, "Как отменяли Рождество",
                "https://telegra.ph/Skaz-o-tom-kak-Rozhdestvo-Novym-godom-zameshchali-01-07"),
    CulturePost(INTRO_GOOGLE, "Год в Поиске 🔎", "https://telegra.ph/God-v-poiske-01-06"),
    CulturePost(INTRO_MOSCOW, "Вперед в прошлое 🚂",
                "https://telegra.ph/Kak-starinnaya-Moskva-vstrechala-Novyj-god-12-29"),
    CulturePost(INTRO_BEAR, "Медвежонок Паддингтон", "https://telegra.ph/Medvezhonok-Paddington-12-27"),
    CulturePost(INTRO_WHAM, "Wham! - Last Christmas", "https://telegra.ph/Wham---Last-Christmas-12-25-2"),
    CulturePost(INTRO_COKE, "Coca-Cola и Новый год", "https://telegra.ph/Koka-Kola-i-Novyj-god-12-19"),
    CulturePost(INTRO, "Окунуться в атмосферу"),
    CulturePost(INTRO_FILM, "Новогоднее кино!", "https://telegra.ph/Novogodnee-kino-12-18")
]

# MUSIC

MUS_NAME_1 = "Perry Como - Magic Moments"
MUS_NAME_2 = "Stevie Wonder - What Christmas Means To Me"
MUS_NAME_3 = "Michael Bublé - White Christmas"
MUS_NAME_4 = "Людмила Гурченко - Пять минут"
MUS_NAME_5 = "Brenda Lee - Rockin' Around The Christmas Tree"
MUS_NAME_6 = "Wham! - Last Christmas"
MUS_NAME_7 = "Валентина Толкунова - Кабы не было зимы"
MUS_NAME_8 = "Melanie Thornton - Wonderful dream (Holidays are coming)"
MUS_NAME_9 = "twenty one pilots - Christmas Saves The Year"
MUS_NAME_10 = "Ольга Рождественская и ВИА Добры молодцы - Песенка о снежинке"
MUS_NAME_11 = "Пётр Ильич Чайковскй - Музыка из балета Щелкунчик"
MUS_NAME_12 = "Queen - Thank God It's Christmas"

MusPost1 = MusicPost(MUS_NAME_1, "media/music_disks/magic_moments.mp4", "https://music.yandex.ru/album/572022/track/5649466")
MusPost2 = MusicPost(MUS_NAME_2, "media/music_disks/what_christmas_means.mp4",
                     "https://music.yandex.ru/album/6350343/track/68286")
MusPost3 = MusicPost(MUS_NAME_3, "media/music_disks/white_christmas.mp4",
                     "https://music.yandex.ru/album/9092253/track/59364946")
MusPost4 = MusicPost(MUS_NAME_4, "media/music_disks/five_minutes.mp4",
                     "https://music.yandex.ru/album/12347882/track/53775253")
MusPost5 = MusicPost(MUS_NAME_5, "media/music_disks/rocking_around.mp4", "https://music.yandex.ru/album/9032855/track/68282")
MusPost6 = MusicPost(MUS_NAME_6, "media/music_disks/Wham! - Last Christmas.mp4",
                     "https://music.yandex.ru/album/18731878/track/631110")
MusPost7 = MusicPost(MUS_NAME_7, "media/music_disks/Валентина Толкунова - Кабы не было зимы.mp4",
                     "https://music.yandex.ru/album/4644677/track/36812772")
MusPost8 = MusicPost(MUS_NAME_8, "media/music_disks/Melanie Thornton - Wonderful Dream (Holidays Are Coming).mp4",
                     "https://music.yandex.ru/album/3396288/track/649993")
MusPost9 = MusicPost(MUS_NAME_9, "media/music_disks/christmas_saves_the_year.mp4",
                     "https://music.yandex.ru/album/13079020/track/74701685")
MusPost10 = MusicPost(MUS_NAME_10, "media/music_disks/О снежинке.mp4",
                      "https://music.yandex.ru/album/12869511/track/18049100"),
MusPost11 = MusicPost(MUS_NAME_11, "media/music_disks/балет.mp4", "https://music.yandex.ru/album/9503675/track/40190715")
MusPost12 = MusicPost(MUS_NAME_12, "media/music_disks/Thank God It's Christmas.mp4",
                      "https://music.yandex.ru/album/2486907/track/2295008")

MUSIC_DICT = {MUS_NAME_1: MusPost1,
              MUS_NAME_2: MusPost2,
              MUS_NAME_3: MusPost3,
              MUS_NAME_4: MusPost4,
              MUS_NAME_5: MusPost5,
              MUS_NAME_6: MusPost6,
              MUS_NAME_7: MusPost7,
              MUS_NAME_8: MusPost8,
              MUS_NAME_9: MusPost9,
              MUS_NAME_10: MusPost10,
              MUS_NAME_11: MusPost11,
              MUS_NAME_12: MusPost12, }

MUSIC_POSTS = [
    MusPost12, MusPost11, MusPost10, MusPost9, MusPost8, MusPost7, MusPost6, MusPost1, MusPost2, MusPost3, MusPost4,
    MusPost5
]

# AES

WELCOME_AES_TEXT = "Добавили долгожданный раздел с поздравлениями от АЭС 🔥\n\n💡У каждой атомной электростанции есть свое сердце, которое называется ядерным реактором.\n\nТак вот, представь себе, что все 12 российских АЭС подготовили для тебя поздравления c новогодними каламбурами от всего <s>сердца</s> реактора❤"

PREV_AES_BTN = "prev aes btn"
NEXT_AES_BTN = "next aes btn"

AES_0_NAME = "Ростовская АЭС"
AES_1_NAME = "Белоярская АЭС"
AES_2_NAME = "Нововоронежская АЭС"
AES_3_NAME = "Ленинградская АЭС"
AES_4_NAME = "Смоленская АЭС"
AES_5_NAME = "Кольская АЭС"
AES_6_NAME = "Балаковская АЭС"
AES_7_NAME = "Курская АЭС"
AES_8_NAME = "Билибинская АЭС"
AES_9_NAME = "Калининская АЭС"
AES_10_NAME = "Плавучая АЭС"
AES_11_NAME = "Запорожская АЭС"

AES_CAPTION_0 = "Ростовская АЭС\n\nОбогащение — процесс повышения концентрации того или иного элемента в добытом сырье. У нас, атомщиков, это превращение природного урана в ядерное топливо."
AES_CAPTION_1 = "Белоярская АЭС\n\nМОКС-топливо создают с добавлением отработавшего ядерного топлива, что позволяет уменьшить потребление урана. Кстати, в сентябре 2022 года один из реакторов Белоярской АЭС полностью перешёл на МОКС-топливо — вот уж кому удалось отМОКСнуть!"
AES_CAPTION_2 = "Нововоронежская АЭС\n\nВ процессе деления урана в реакторе накапливаются иод и ксенон, которые после выключения реактора первые сутки не дают ему начать снова работать на полной мощности — это состояние и называют иодной ямой."
AES_CAPTION_3 = "Ленинградская АЭС\n\nЦентрифуги позволяют обогащать уран — превращать простой природный уран в ядерное топливо."
AES_CAPTION_4 = "Смоленская АЭС\n\nУран, конечно, не буквально выгорает, но так называют его расход во время работы ядерного реактора."
AES_CAPTION_5 = "Кольская АЭС\n\nЭто первая АЭС, построенная за полярным кругом."
AES_CAPTION_6 = "Балаковская АЭС\n\nОколо 20% электричества в России приходится именно на атомную энергетику!"
AES_CAPTION_7 = "Курская АЭС\n\nРЕМИКС-топливо для ядерных реакторов «готовится» из уже отработавшего ядерного топлива — это позволяет уменьшить потребность и в добыче урана, и в его захоронении!"
AES_CAPTION_8 = "Билибинская АЭС\n\nДо прибытия в порт Певека «Академика Ломоносова» была самой северной АЭС мира — на Чукотке прохладно!"
AES_CAPTION_9 = "Калининская АЭС\n\nДелаем отсылку на счëтчик Гейгера и желаем светиться от счастья ;)"
AES_CAPTION_10 = "Плавучая АЭС\n\n\"Академик Ломоносов\" — первая и единственная плавучая АЭС. Сейчас находится в городе Певек на Чукотке и является самой северной АЭС мира!"
AES_CAPTION_11 = "Запорожская АЭС\n\nСамая крупная электростанция Европы."

aesPost0 = AesPost("media/aes_photos/aes_0.jpg", AES_CAPTION_0, AES_0_NAME)
aesPost1 = AesPost("media/aes_photos/aes_1.jpg", AES_CAPTION_1, AES_1_NAME)
aesPost2 = AesPost("media/aes_photos/aes_2.jpg", AES_CAPTION_2, AES_2_NAME)
aesPost3 = AesPost("media/aes_photos/aes_3.jpg", AES_CAPTION_3, AES_3_NAME)
aesPost4 = AesPost("media/aes_photos/aes_4.jpg", AES_CAPTION_4, AES_4_NAME)
aesPost5 = AesPost("media/aes_photos/aes_5.jpg", AES_CAPTION_5, AES_5_NAME)
aesPost6 = AesPost("media/aes_photos/aes_6.jpg", AES_CAPTION_6, AES_6_NAME)
aesPost7 = AesPost("media/aes_photos/aes_7.jpg", AES_CAPTION_7, AES_7_NAME)
aesPost8 = AesPost("media/aes_photos/aes_8.jpg", AES_CAPTION_8, AES_8_NAME)
aesPost9 = AesPost("media/aes_photos/aes_9.jpg", AES_CAPTION_9, AES_9_NAME)
aesPost10 = AesPost("media/aes_photos/aes_10.jpg", AES_CAPTION_10, AES_10_NAME)
aesPost11 = AesPost("media/aes_photos/aes_11.jpg", AES_CAPTION_11, AES_11_NAME)

AES_DICT = {
    AES_CAPTION_0: aesPost0,
    AES_CAPTION_1: aesPost1,
    AES_CAPTION_2: aesPost2,
    AES_CAPTION_3: aesPost3,
    AES_CAPTION_4: aesPost4,
    AES_CAPTION_5: aesPost5,
    AES_CAPTION_6: aesPost6,
    AES_CAPTION_7: aesPost7,
    AES_CAPTION_8: aesPost8,
    AES_CAPTION_9: aesPost9,
    AES_CAPTION_10: aesPost10,
    AES_CAPTION_11: aesPost11
}

AES_POSTS = [aesPost0, aesPost1, aesPost2, aesPost3, aesPost4, aesPost5, aesPost6,
             aesPost7, aesPost8, aesPost9, aesPost10, aesPost11]

# NEW YEAR QUIZ

NEW_YEAR_Q_BTN = "new year quiz"
NEW_YEAR_Q_FIRST_QUESTION_RIGHT = "1.1.1"
NEW_YEAR_Q_FIRST_QUESTION_WRONG = "1.1.0"
NEW_YEAR_Q_SECOND_QUESTION_RIGHT = "1.2.1"
NEW_YEAR_Q_SECOND_QUESTION_WRONG = "1.2.0"
NEW_YEAR_Q_THIRD_QUESTION_RIGHT = "1.3.1"
NEW_YEAR_Q_THIRD_QUESTION_WRONG = "1.3.0"
NEW_YEAR_Q_FOURTH_QUESTION_RIGHT = "1.4.1"
NEW_YEAR_Q_FOURTH_QUESTION_WRONG = "1.4.0"
NEW_YEAR_Q_FIFTH_QUESTION_RIGHT = "1.5.1"
NEW_YEAR_Q_FIFTH_QUESTION_WRONG = "1.5.0"
NEW_YEAR_Q_SIXTH_QUESTION_RIGHT = "1.6.1"
NEW_YEAR_Q_SIXTH_QUESTION_WRONG = "1.6.0"
NEW_YEAR_Q_SEVENTH_QUESTION_RIGHT = "1.7.1"
NEW_YEAR_Q_SEVENTH_QUESTION_WRONG = "1.7.0"
NEW_YEAR_Q_EIGHTH_QUESTION_RIGHT = "1.8.1"
NEW_YEAR_Q_EIGHTH_QUESTION_WRONG = "1.8.0"
NEW_YEAR_Q_NINTH_QUESTION_RIGHT = "1.9.1"
NEW_YEAR_Q_NINTH_QUESTION_WRONG = "1.9.0"
NEW_YEAR_Q_TENTH_QUESTION_RIGHT = "1.10.1"
NEW_YEAR_Q_TENTH_QUESTION_WRONG = "1.10.0"
NEW_YEAR_Q_ELEVENTH_QUESTION_RIGHT = "1.11.1"
NEW_YEAR_Q_ELEVENTH_QUESTION_WRONG = "1.11.0"
NEW_YEAR_Q_TWELFTH_QUESTION_RIGHT = "1.12.1"
NEW_YEAR_Q_TWELFTH_QUESTION_WRONG = "1.12.0"

NEW_YEAR_Q_QUESTION_CALLBACKS = {
    NEW_YEAR_Q_BTN: 1,
    NEW_YEAR_Q_FIRST_QUESTION_RIGHT: 2, NEW_YEAR_Q_FIRST_QUESTION_WRONG: 2, NEW_YEAR_Q_SECOND_QUESTION_RIGHT: 3,
    NEW_YEAR_Q_SECOND_QUESTION_WRONG: 3, NEW_YEAR_Q_THIRD_QUESTION_RIGHT: 4, NEW_YEAR_Q_THIRD_QUESTION_WRONG: 4,
    NEW_YEAR_Q_FOURTH_QUESTION_RIGHT: 5, NEW_YEAR_Q_FOURTH_QUESTION_WRONG: 5, NEW_YEAR_Q_FIFTH_QUESTION_RIGHT: 6,
    NEW_YEAR_Q_FIFTH_QUESTION_WRONG: 6, NEW_YEAR_Q_SIXTH_QUESTION_RIGHT: 7, NEW_YEAR_Q_SIXTH_QUESTION_WRONG: 7,
    NEW_YEAR_Q_SEVENTH_QUESTION_RIGHT: 8, NEW_YEAR_Q_SEVENTH_QUESTION_WRONG: 8, NEW_YEAR_Q_EIGHTH_QUESTION_RIGHT: 9,
    NEW_YEAR_Q_EIGHTH_QUESTION_WRONG: 9, NEW_YEAR_Q_NINTH_QUESTION_RIGHT: 10, NEW_YEAR_Q_NINTH_QUESTION_WRONG: 10,
    NEW_YEAR_Q_TENTH_QUESTION_RIGHT: 11, NEW_YEAR_Q_TENTH_QUESTION_WRONG: 11, NEW_YEAR_Q_ELEVENTH_QUESTION_RIGHT: 12,
    NEW_YEAR_Q_ELEVENTH_QUESTION_WRONG: 12, NEW_YEAR_Q_TWELFTH_QUESTION_RIGHT: 13, NEW_YEAR_Q_TWELFTH_QUESTION_WRONG: 13
}

NEW_YEAR_Q_QUESTION_RIGHT = {NEW_YEAR_Q_FIRST_QUESTION_RIGHT, NEW_YEAR_Q_SECOND_QUESTION_RIGHT,
                             NEW_YEAR_Q_THIRD_QUESTION_RIGHT, NEW_YEAR_Q_FOURTH_QUESTION_RIGHT,
                             NEW_YEAR_Q_FIFTH_QUESTION_RIGHT, NEW_YEAR_Q_SIXTH_QUESTION_RIGHT,
                             NEW_YEAR_Q_SEVENTH_QUESTION_RIGHT, NEW_YEAR_Q_EIGHTH_QUESTION_RIGHT,
                             NEW_YEAR_Q_NINTH_QUESTION_RIGHT, NEW_YEAR_Q_TENTH_QUESTION_RIGHT,
                             NEW_YEAR_Q_ELEVENTH_QUESTION_RIGHT, NEW_YEAR_Q_TWELFTH_QUESTION_RIGHT}

NEW_YEAR_Q_FIRST_QUESTION = NewYearQuizQuestion(
    "Всем известно, что внучкой деда Мороза является Снегурочка. А вот какой город считается родиной снежной красавицы?",
    ["Великий Устюг", "Кострома", "Тюмень", "Великий Новгород"], 1,
    [NEW_YEAR_Q_FIRST_QUESTION_RIGHT, NEW_YEAR_Q_FIRST_QUESTION_WRONG])

NEW_YEAR_Q_SECOND_QUESTION = NewYearQuizQuestion(
    "Из какого фильма эта фраза: <b><i>«Мне десять лет. Телевизор — это моя жизнь»</i></b>?",
    ["«Рождественские хроники»", "«Операция «Ы» и другие приключения Шурика»", "«Один дома»",
     "«Гринч-похититель рождества»"], 2, [NEW_YEAR_Q_SECOND_QUESTION_RIGHT, NEW_YEAR_Q_SECOND_QUESTION_WRONG])

NEW_YEAR_Q_THIRD_QUESTION = NewYearQuizQuestion(
    "2021 год — год науки и технологий; 2022 год — год культурного наследия. А годом чего объявлен 2023 год?",
    ["Театра", "Добровольца и волонтера", "Педагога и наставника", "Памяти и славы"], 2,
    [NEW_YEAR_Q_THIRD_QUESTION_RIGHT, NEW_YEAR_Q_THIRD_QUESTION_WRONG])

NEW_YEAR_Q_FOURTH_QUESTION = NewYearQuizQuestion(
    "В новогоднем фильме «Чародеи» герои занимались созданием волшебной палочки. А как назывался институт, в котором велась разработка?",
    ["Не может быть", "Ну и ну", "Удивительные явления", "Фантастические изобретения"], 1,
    [NEW_YEAR_Q_FOURTH_QUESTION_RIGHT, NEW_YEAR_Q_FOURTH_QUESTION_WRONG])

NEW_YEAR_Q_FIFTH_QUESTION = NewYearQuizQuestion(
    "Первый раз зрители увидели эту телепередачу в 1962 году. С тех пор каждый год россияне включают эту концертную программу в Новый год. О какой передаче идёт речь?",
    ["«Угадай мелодию»", "«Поле чудес»", "«Голубой огонёк»", "«КВН»"], 2,
    [NEW_YEAR_Q_FIFTH_QUESTION_RIGHT, NEW_YEAR_Q_FIFTH_QUESTION_WRONG])

NEW_YEAR_Q_SIXTH_QUESTION = NewYearQuizQuestion(
    "А откуда эта фраза: <i><b>«Бабу-ягу со стороны брать не будем, воспитаем в своем коллективе!»</b></i>?",
    ["«Карнавальная ночь»", "«Чародеи»", "«Красавица и чудовище: Чудесное Рождество»", "«Ёлки»"], 0,
    [NEW_YEAR_Q_SIXTH_QUESTION_RIGHT, NEW_YEAR_Q_SIXTH_QUESTION_WRONG])

NEW_YEAR_Q_SEVENTH_QUESTION = NewYearQuizQuestion(
    "В России 11 часовых поясов, поэтому Новый год можно отметить несколько раз. А какой регион из перечисленных встречает этот праздник первым?",
    ["Камчатский край", "Калининградская область", "Хабаровский край", "Новосибирская область"], 0,
    [NEW_YEAR_Q_SEVENTH_QUESTION_RIGHT, NEW_YEAR_Q_SEVENTH_QUESTION_WRONG])

NEW_YEAR_Q_EIGHTH_QUESTION = NewYearQuizQuestion(
    "Прямиком из детства, вспомните, откуда фраза: <i><b>«Тепло ли тебе, девица, тепло ли тебе, красная»</b></i>?",
    ["«Простоквашино»", "«Морозко»", "«Холодное сердце»", "«Секретная служба Санта-Клауса»"], 1,
    [NEW_YEAR_Q_EIGHTH_QUESTION_RIGHT, NEW_YEAR_Q_EIGHTH_QUESTION_WRONG])

NEW_YEAR_Q_NINTH_QUESTION = NewYearQuizQuestion("В каком году первое января было объявлено праздничным днём?",
                                                ["1939 г.", "1947 г.", "1953 г.", "1856 г."], 1,
                                                [NEW_YEAR_Q_NINTH_QUESTION_RIGHT, NEW_YEAR_Q_NINTH_QUESTION_WRONG])

NEW_YEAR_Q_TENTH_QUESTION = NewYearQuizQuestion(
    "Просмотр фильма «Ирония судьбы, или С лёгким паром!» стал ежегодной традицией россиян. Главная героиня кинокартины — Надя. А представителем какой профессии она является?",
    ["Бухгалтер", "Водитель троллейбуса", "Парикмахер", "Учитель"], 3,
    [NEW_YEAR_Q_TENTH_QUESTION_RIGHT, NEW_YEAR_Q_TENTH_QUESTION_WRONG])

NEW_YEAR_Q_ELEVENTH_QUESTION = NewYearQuizQuestion("В каком году новогодняя ёлка стала символом праздника?",
                                                   ["1710 г.", "1698 г.", "1705 г.", "1700 г."], 3,
                                                   [NEW_YEAR_Q_ELEVENTH_QUESTION_RIGHT,
                                                    NEW_YEAR_Q_ELEVENTH_QUESTION_WRONG])

NEW_YEAR_Q_TWELFTH_QUESTION = NewYearQuizQuestion(
    "Ну и в конце не можем не упомянуть эту песню! Откуда строчка: <i><b>«Остыли реки, и земля остыла»</b></i>?",
    ["«Три белых коня»", "«Новогодняя»", "«Кабы не было зимы»", "«Снежинка»"], 0,
    [NEW_YEAR_Q_TWELFTH_QUESTION_RIGHT, NEW_YEAR_Q_TWELFTH_QUESTION_WRONG])

NEW_YEAR_Q_QUESTIONS = {1: NEW_YEAR_Q_FIRST_QUESTION, 2: NEW_YEAR_Q_SECOND_QUESTION, 3: NEW_YEAR_Q_THIRD_QUESTION,
                        4: NEW_YEAR_Q_FOURTH_QUESTION, 5: NEW_YEAR_Q_FIFTH_QUESTION, 6: NEW_YEAR_Q_SIXTH_QUESTION,
                        7: NEW_YEAR_Q_SEVENTH_QUESTION, 8: NEW_YEAR_Q_EIGHTH_QUESTION, 9: NEW_YEAR_Q_NINTH_QUESTION,
                        10: NEW_YEAR_Q_TENTH_QUESTION, 11: NEW_YEAR_Q_ELEVENTH_QUESTION,
                        12: NEW_YEAR_Q_TWELFTH_QUESTION}

# CHARACTER QUIZ

CHARACTER_QUIZ_NAME = "character_quiz"
START_CHARACTER_QUIZ = "start_character_quiz"
CHARACTER_QUIZ_LENGTH = 18

CHARACTER_QUIZ_START_MESSAGE = "Тебя ждёт тестик на 18 вопросов, по результатам которого мы сможем определить, с каким персонажем мультсериалов (и не только 🤫) ты схож! Помни: правильных ответов нет ❤"

CHARACTER_VALLI_CALLBACK = "character_valli_callback"
CHARACTER_VALLI_CALLBACK_RESULT = "character_valli_callback_result"
CHARACTER_DASHA_CALLBACK = "character_dasha_callback"
CHARACTER_DASHA_CALLBACK_RESULT = "character_dasha_callback_result"
CHARACTER_FITNESS_CALLBACK = "character_fitness_callback"
CHARACTER_FITNESS_CALLBACK_RESULT = "character_fitness_callback_result"
CHARACTER_KOTIK_CALLBACK = "character_kotik_callback"
CHARACTER_KOTIK_CALLBACK_RESULT = "character_kotik_callback_result"
CHARACTER_YMKA_CALLBACK = "character_ymka_callback"
CHARACTER_YMKA_CALLBACK_RESULT = "character_ymka_callback_result"
CHARACTER_SHORT_CALLBACK = "character_short_callback"
CHARACTER_SHORT_CALLBACK_RESULT = "character_short_callback_result"

CHARACTER_QUIZ_QUESTION_CALLBACKS = [CHARACTER_VALLI_CALLBACK, CHARACTER_DASHA_CALLBACK,
                                     CHARACTER_FITNESS_CALLBACK, CHARACTER_KOTIK_CALLBACK,
                                     CHARACTER_YMKA_CALLBACK, CHARACTER_SHORT_CALLBACK]

CHARACTERS_LIST = {
    0: CHARACTER_VALLI_CALLBACK_RESULT,
    1: CHARACTER_DASHA_CALLBACK_RESULT,
    2: CHARACTER_FITNESS_CALLBACK_RESULT,
    3: CHARACTER_KOTIK_CALLBACK_RESULT,
    4: CHARACTER_YMKA_CALLBACK_RESULT,
    5: CHARACTER_SHORT_CALLBACK_RESULT
}

REVERSER_CHARACTER_LIST = {
    CHARACTER_VALLI_CALLBACK_RESULT: (0, "Зеленый офис в Росатоме", "https://vk.com/wall-189209997_5570"),
    CHARACTER_DASHA_CALLBACK_RESULT: (1, "Edu в Атом", "https://juniorrosatom.team/eduvatom"),
    CHARACTER_FITNESS_CALLBACK_RESULT: (2, "РешАтом", "https://juniorrosatom.team/page32139546.html"),
    CHARACTER_KOTIK_CALLBACK_RESULT: (3, "Наша группа", "https://vk.com/juniorrosatom"),
    CHARACTER_YMKA_CALLBACK_RESULT: (4, "АтомСтори", "https://vk.com/atomstory"),
    CHARACTER_SHORT_CALLBACK_RESULT: (5, "Наша группа", "https://vk.com/juniorrosatom")
}

CHARACTER_QUIZ_QUESTIONS = {
    1: CharacterQuizQuestion(1, [3, 2, 5, 6, 1, 4]),
    2: CharacterQuizQuestion(2, [3, 2, 4, 5, 6, 1]),
    3: CharacterQuizQuestion(3, [6, 3, 2, 5, 1, 4]),
    4: CharacterQuizQuestion(4, [5, 3, 6, 4, 1, 2]),
    5: CharacterQuizQuestion(5, [6, 3, 2, 1, 5, 4]),
    6: CharacterQuizQuestion(6, [2, 1, 5, 6, 3, 4]),
    7: CharacterQuizQuestion(7, [5, 2, 3, 4, 6, 1]),
    8: CharacterQuizQuestion(8, [5, 6, 4, 3, 2, 1]),
    9: CharacterQuizQuestion(9, [1, 3, 4, 2, 6, 5]),
    10: CharacterQuizQuestion(10, [3, 5, 4, 1, 6, 2]),
    11: CharacterQuizQuestion(11, [5, 1, 6, 3, 2, 4]),
    12: CharacterQuizQuestion(12, [4, 2, 3, 5, 1, 6]),
    13: CharacterQuizQuestion(13, [1, 2, 6, 4, 5, 3]),
    14: CharacterQuizQuestion(14, [2, 3, 5, 1, 4, 6]),
    15: CharacterQuizQuestion(15, [1, 3, 5, 6, 4, 2]),
    16: CharacterQuizQuestion(16, [6, 1, 4, 2, 5, 3]),
    17: CharacterQuizQuestion(17, [6, 5, 4, 3, 2, 1]),
    18: CharacterQuizQuestion(18, [1, 2, 6, 4, 5, 3])
}
