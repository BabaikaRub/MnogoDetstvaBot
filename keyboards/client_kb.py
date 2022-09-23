from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import emoji


inline_button_offline = InlineKeyboardButton(text='Занятия оффлайн', callback_data='btn_offline')
inline_button_online = InlineKeyboardButton(text='Занятия онлайн', callback_data='btn_online')
inline_button_site = InlineKeyboardButton(text='Наш сайт', url='http://mnogodetstva.com/')
inline_button_review = InlineKeyboardButton(text='Отзыв', url='http://mnogodetstva.com/otziv')
inline_button_vk = InlineKeyboardButton(text='ВК', url='https://vk.com/roomnogodetstva')
inline_button_contact = InlineKeyboardButton(text='Позвонить и задать вопрос', callback_data='btn_contact')

button_prices = KeyboardButton('Членский и целевой взнос')
button_timetable = KeyboardButton('Расписание')
button_enroll = KeyboardButton('Записаться')
button_back = KeyboardButton('Назад') 

online_button_prices = KeyboardButton('Цена')

# online_button_price = KeyboardButton('Цены')
# online_button_timetable = KeyboardButton('Расписание занятий')
# online_button_enroll = KeyboardButton('Записаться онлайн')

# inline_button_prices = InlineKeyboardButton(text='Список занятий и цены', callback_data='btn_select')
# inline_button_timetable = InlineKeyboardButton(text='Расписание', callback_data='btn_timetable')
# inline_button_enroll = InlineKeyboardButton(text='Записаться', callback_data='btn_enroll')
inline_button_select1 = InlineKeyboardButton(text='1️⃣', callback_data='btn1')
inline_button_select2 = InlineKeyboardButton(text='2️⃣', callback_data='btn2')
inline_button_select3 = InlineKeyboardButton(text='3️⃣', callback_data='btn3')
inline_button_select4 = InlineKeyboardButton(text='4️⃣', callback_data='btn4')

inline_button_tech = InlineKeyboardButton(text='Техническое направление', callback_data='btn_tech')
inline_button_it = InlineKeyboardButton(text='IT-направление', callback_data='btn_it')
inline_button_lang = InlineKeyboardButton(text='Лингвистическое направление', callback_data='btn_leng')
inline_button_oge = InlineKeyboardButton(text='Подготовка к ОГЭ', callback_data='btn_oge')
inline_button_ege = InlineKeyboardButton(text='Подготовка к ЕГЭ', callback_data='btn_ege')
inline_button_early = InlineKeyboardButton(text='Раннее развитие', callback_data='btn_early')

inline_selector_online = InlineKeyboardMarkup(row_width=1)
inline_selector_online.add(inline_button_tech).add(inline_button_it).add(inline_button_lang).add(inline_button_oge).add(inline_button_ege).add(inline_button_early)

inline_selector_offline = InlineKeyboardMarkup(row_width=2)
inline_selector_offline.row(inline_button_select1, inline_button_select2).row(inline_button_select3, inline_button_select4)

inline_menu = InlineKeyboardMarkup(row_width=1)
inline_menu.row(inline_button_offline, inline_button_online).row(inline_button_site, inline_button_review, inline_button_vk).add(inline_button_contact)

offline_center_lst = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
offline_center_lst.add(button_prices).row(button_timetable, button_enroll).add(button_back)

online_center_lst = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
online_center_lst.add(online_button_prices).row(button_timetable, button_enroll).add(button_back)
