from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot, bot_address
from keyboards import kb_client
from school_database import sqlite_db

"""Хендлеры для взаимодействия с клиентом
"""


#@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    bot_home = bot_address  # можно указать адрес бота в телеграм строкой 't.me/bot'
    try:
        await bot.send_message(message.from_user.id,
                               f'Привет! Я фитнесс бот от компании Мегаспорт. Наша программа подходит для всех, независимо от вашего уровня подготовки.\
            Используйте клавиатуру, чтобы узнать больше о наших тренировках и услугах.', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(f'Пожалуйста напишите боту в ЛС: {bot_home}')


#@dp.message_handler(Text(equals='Контакты', ignore_case=True))
async def get_contacts(message: types.Message):
    address = "ул. Муслимская, 00/00"
    phones = '+7 (000) 000-00-00'
    email = 'info@muslimfitnessclub.com'
    website = 'www.muslimfitnessclub.com'
    social_media = {
        'Instagram': '@muslimfitnessclub',
        'Facebook': 'facebook.com/muslimfitnessclub'
    }
    working_hours = 'пн-вс 06.30–22.30'
    transport = 'Ближайшее метро: Муслимская'

    await bot.send_message(message.from_user.id,
                           f'Адрес нашего фитнес-клуба: {address}\n'
                           f'Контактные номера: {phones}\n'
                           f'Электронная почта: {email}\n'
                           f'Наш веб-сайт: {website}\n'
                           f'Наши социальные сети:\n'
                           f'Instagram: {social_media["Instagram"]}\n'
                           f'Facebook: {social_media["Facebook"]}\n'
                           f'Часы работы: {working_hours}\n'
                           f'Ориентир: {transport}\n'
                           f'Ждём вас на тренировках, Муслим!')




#@dp.message_handler(Text(equals='Режим работы', ignore_case=True))
async def get_work_hours(message: types.Message):
    work_hours = (
        "Понедельник: 06:30–22:30\n"
        "Вторник: 06:30–22:30\n"
        "Среда: 06:30–22:30\n"
        "Четверг: 06:30–22:30\n"
        "Пятница: 06:30–22:30\n"
        "Суббота: 06:30–22:30\n"
        "Воскресенье: 06:30–22:30"
    )
    await bot.send_message(message.from_user.id, f'Время работы:\n{work_hours}')



#@dp.message_handler(Text(equals='Тренировки', ignore_case=True))
async def get_training_courses(message: types.Message):
    await sqlite_db.sql_read_from_courses(message)


#@dp.message_handler(Text(equals='Преподаватели', ignore_case=True))
async def get_trainers_info(message: types.Message):
    await sqlite_db.sql_read_from_teachers(message)


# Обработчик для кнопки "Главное меню"
@dp.message_handler(Text(equals='Главное меню', ignore_case=True))
async def go_to_main_menu(message: types.Message):
    await message.reply("Вы в главном меню", reply_markup=kb_client)


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(get_contacts, Text(equals='Контакты', ignore_case=True))
    dp.register_message_handler(get_work_hours, Text(equals='Режим работы', ignore_case=True))
    dp.register_message_handler(get_training_courses, Text(equals='Тренировки', ignore_case=True))
    dp.register_message_handler(get_trainers_info, Text(equals='Преподаватели', ignore_case=True))
    dp.register_message_handler(go_to_main_menu, Text(equals='Главное меню', ignore_case=True))
