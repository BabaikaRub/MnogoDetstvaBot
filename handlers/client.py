from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import emoji

from create_bot import dp, bot
from keyboards import inline_menu, offline_center_lst, inline_selector_offline, inline_selector_online, online_center_lst
from handlers.messages import greeting, show_menu_message, offline_centers, offline_files, contribution


offline_btns = ['btn1', 'btn2', 'btn3', 'btn4']
online_btns_extra = ['btn_tech', 'btn_it', 'btn_leng', 'btn_early']

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, greeting, reply_markup=ReplyKeyboardRemove())


async def show_menu(message: types.Message):
    await bot.send_message(message.from_user.id, show_menu_message, reply_markup=inline_menu)


@dp.callback_query_handler(text='btn_offline')
async def offline_list(callback: types.CallbackQuery):
    try:
        global status
        status = callback.data
    except AttributeError:
        pass

    centers = list(offline_centers.values())
    await bot.send_message(callback.from_user.id, 'Выберите центр, в котором хотите посещать занятия' + emoji.emojize(':backhand_index_pointing_down:'))
    await bot.send_message(callback.from_user.id, f'1️⃣ {centers[0]}\n\n2️⃣ {centers[1]}\n\n3️⃣ {centers[2]}\n\n4️⃣ {centers[3]}', reply_markup=inline_selector_offline)
    await callback.answer()


@dp.callback_query_handler(text='btn_online')
async def online_list(callback: types.CallbackQuery):
    try:
        global status
        status = callback.data
    except AttributeError:
        pass

    await bot.send_message(callback.from_user.id, 'Выберите тип онлайн занятий, которые хотите посещать ⬇️', reply_markup=inline_selector_online)
    await callback.answer()


@dp.callback_query_handler(text='btn_contact')
async def get_contact(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Номер телефона для связи: +7 (985) 916-16-67')
    await callback.answer()


@dp.callback_query_handler(text='btn1')
@dp.callback_query_handler(text='btn2')
@dp.callback_query_handler(text='btn3')
@dp.callback_query_handler(text='btn4')
async def select_center(callback: types.CallbackQuery):
    global direction
    direction = callback.data
    await bot.send_message(callback.from_user.id, f'🏢 Выбран центр: {offline_centers[callback.data]}')
    await bot.send_message(callback.from_user.id, 'Выберите действие:', reply_markup=offline_center_lst)

    await callback.answer()


@dp.callback_query_handler(text='btn_tech')
@dp.callback_query_handler(text='btn_it')
@dp.callback_query_handler(text='btn_leng')
@dp.callback_query_handler(text='btn_oge')
@dp.callback_query_handler(text='btn_ege')
@dp.callback_query_handler(text='btn_early')
async def select_direction(callback: types.CallbackQuery):
    global direction
    direction = callback.data
    await bot.send_message(callback.from_user.id, 'Выберите действие:', reply_markup=online_center_lst)
    
    await callback.answer()


@dp.message_handler(Text(equals='Расписание'))
async def get_timetable(message: types.Message):
    
    if direction in offline_btns:
        file = open(f'centers\offline_centers\{offline_files[direction]}.pdf', 'rb')
        await bot.send_document(message.chat.id, file)

    elif direction in online_btns_extra:
        file = open('centers\online_centers\Raspisainie_Online.pdf', 'rb')
        await bot.send_document(message.chat.id, file)
    
    elif direction == 'btn_oge':
        file = open('centers\online_centers\Raspisanie_OGE.pdf', 'rb')
        await bot.send_document(message.chat.id, file)

    elif direction == 'btn_ege':
        file = open('centers\online_centers\Raspisanie_EGE.pdf', 'rb')
        await bot.send_document(message.chat.id, file)


@dp.message_handler(Text(equals='Записаться'))
async def get_record(message: types.Message):
    
    if direction in offline_btns:
        await bot.send_message(message.from_user.id, 'Для записи перейдите по ссылке: https://forms.yandex.ru/cloud/631329e6e4cec35d01168a87/')

    elif direction in online_btns_extra:
        await bot.send_message(message.from_user.id, 'Для записи перейдите по ссылке: https://forms.yandex.ru/u/62fb6ce5d5b8427c7aed7b80/')

    elif direction == 'btn_oge' or direction == 'btn_ege':
        await bot.send_message(message.from_user.id, 'Для записи перейдите по ссылке: https://forms.yandex.ru/u/62fb6ce5d5b8427c7aed7b80/')


@dp.message_handler(Text(equals='Членский и целевой взнос'))
async def contribution_msg(message: types.Message):
    await bot.send_message(message.from_user.id, contribution)


@dp.message_handler(Text(equals='Цена'))
async def show_price(message: types.Message):
    await bot.send_message(message.from_user.id, 'Список цен на онлайн курсы: https://docs.google.com/document/d/1s0UUZX0Vs0BD94wU6FoVNCiHO1LB_0oUwj9ZeVlV5J8/edit?usp=sharing')


@dp.message_handler(Text(equals='Назад'))
async def back_menu(callback: types.CallbackQuery):
    try:
        await bot.send_message(callback.from_user.id, emoji.emojize(':red_exclamation_mark:') + 'Вы вернулись на прошлый шаг', reply_markup=ReplyKeyboardRemove())
        
        if status == 'btn_offline':
            await offline_list(callback)
        elif status == 'btn_online':
            await online_list(callback)

    except TypeError:
        pass


def registration_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(show_menu, commands=['menu'])
