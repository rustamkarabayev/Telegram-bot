from sqlite3 import connect
import sqlite3
import requests
import telebot
from telebot import types
from telebot.types import *
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

bot = telebot.TeleBot('5777208709:AAGdFmSxGqiPVdHzAPvF6vy50XNak-v0P0M')

conn = connect("database.db", check_same_thread=False)
cursor = conn.cursor()

exit = KeyboardButton(text="⬅️Назад")

categoryKB = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
smartphoneBtn = KeyboardButton(text="📱 Smartphone")
tabBtn = KeyboardButton(text="🖥Tab")
watchBtn = KeyboardButton(text="⌚️Watch")
headphoneBtn = KeyboardButton(text="🎧 Headphone")
macbookBtn = KeyboardButton(text="💻Macbook")
currencyBtn = KeyboardButton(text="💰 Курс валют")
phoneBtn = KeyboardButton(text="📞Отправить номер телефона", request_contact=True)
site = types.InlineKeyboardButton("Наш официальный сайт🌐", url='https://www.apple.com/')
categoryKB.add(smartphoneBtn, tabBtn, watchBtn, headphoneBtn, macbookBtn, currencyBtn, phoneBtn, site)

smartphoneKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
iphone12 = KeyboardButton(text="Iphone 12")
iphone13 = KeyboardButton(text="Iphone 13")
iphone14 = KeyboardButton(text="Iphone 14")
smartphoneKB.add(iphone12, iphone13, iphone14, exit)

tabKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
ipadair = KeyboardButton(text="Ipad air")
ipadpro = KeyboardButton(text="Ipad pro")
ipad10 = KeyboardButton(text="Ipad 10th generation")
tabKB.add(ipadair, ipadpro, ipad10, exit)

watchKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
watchse = KeyboardButton(text="Watch SE")
watchseries8 = KeyboardButton(text="Watch series 8")
watchultra = KeyboardButton(text="Watch Ultra")
watchKB.add(watchse, watchseries8, watchultra, exit)

headphoneKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
airpodsmax = KeyboardButton(text="Airpods Max")
airpodspro = KeyboardButton(text="Airpods pro 2")
airpods3 = KeyboardButton(text="Airpods 3")
headphoneKB.add(airpodsmax, airpodspro, airpods3, exit)

macbookKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
macbookair = KeyboardButton(text="Macbook air")
macbookm1 = KeyboardButton(text="Macbook M1")
macbookm2 = KeyboardButton(text="Macbook M2")
macbookKB.add(macbookair, macbookm1, macbookm2, exit)

colorphoneKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
purple = KeyboardButton(text="🟣Purple")
white = KeyboardButton(text="⚪️White")
black = KeyboardButton(text="⚫️Black")
colorphoneKB.add(purple, white, black, exit)

colortabKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
yellow = KeyboardButton(text="🟡Yellow")
blue = KeyboardButton(text="🔵Blue")
pink = KeyboardButton(text="🟣Pink")
colorphoneKB.add(yellow, blue, pink, exit)

colorwatchKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
red = KeyboardButton(text="🟥Red")
grey = KeyboardButton(text="⬛️Grey")
colorphoneKB.add(red, grey, exit)

colorheadphoneKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
green = KeyboardButton(text="🟢Green")
blackwhite = KeyboardButton(text="⬛️Black-white")
bluewhite = KeyboardButton(text="💠Blue-white")
colorphoneKB.add(green, blackwhite, bluewhite, exit)

colormacbookKB = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
silver = KeyboardButton(text="Silver")
mint = KeyboardButton(text="Mint")
colormacbookKB.add(silver, mint, exit)

memoryphoneKB = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
one128 = KeyboardButton(text="128 gb")
two256 = KeyboardButton(text="256 gb")
three512 = KeyboardButton(text="512 gb")
four1tb = KeyboardButton(text="1 TB")
memoryphoneKB.add(one128, two256, three512, four1tb, exit)

memorytabKB = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
one64 = KeyboardButton(text="64 gb")
two130 = KeyboardButton(text="130 gb")
memoryphoneKB.add(one64, two130, exit)

memorymacbookKB = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
one2tb = KeyboardButton(text="2 TB")
two4tb = KeyboardButton(text="4 TB")
memorymacbookKB.add(one2tb, two4tb, exit)


@bot.message_handler(commands=["start"])
def start(message):
    text = "🤖 Здравствуйте! Я бот поддержки интернет-магазина iStore.\nВыберите то что вы хотите приобрести но сначала хотите ли вы чтоб вас сохранили?"
    bot.send_message(message.chat.id, text, reply_markup=categoryKB)

# @bot.message_handler(func=lambda a: True)
# def handler(message):
#     if message.text == "Да":
#         bot.send_message(message.chat.id, "Вы сохранены!")
#
#         cursor.execute('INSERT INTO iStore(user_id, name, surname, username) VALUES(?, ?, ?, ?)',
#                        (message.from_user.id,
#                         message.from_user.first_name,
#                         message.from_user.last_name,
#                         message.from_user.username))
#         conn.commit()
#     elif message.text == "all":
#         cursor.execute("SELECT * FROM iStore")
#         res = cursor.fetchall()
#
#         # for user in res:
#         #     bot.send_message(user[1], "Hello")
#         print(res)
#
#     elif message.text == "spam":
#         cursor.execute("SELECT * FROM iStore")
#         res = cursor.fetchall()
#
#         for user in res:
#             bot.send_message(user[1], "Spam!!!")


@bot.message_handler(commands=['calendar'])
def start(message):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(message.chat.id,
                     f"Выберите (год) {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def call(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Выберите (месяц) {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"Вы выбрали: {result}",
                              c.message.chat.id,
                              c.message.message_id)


@bot.message_handler(commands=['products'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="📱 Smartphone", callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text="🖥Tab", callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text="🎧 Headphone", callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text="⌚️Watch", callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text="💻Macbook", callback_data=5))
    bot.send_message(message.chat.id, text="Выберите то что хотите приобрести и узнайте чем он полезен:",
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="О боте🤖", callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text="Наш официальный сайт🌐", callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text="Вспомогательные команды запросов🔀", callback_data=8))
    bot.send_message(message.chat.id, text="Выберите из кнопок если хотите узнать больше о нас", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо то что выбрали нас!')
    answer = ''
    if call.data == '1':
        answer = 'Используется каждый день и без него никак📅'
    elif call.data == '2':
        answer = 'Он удобен для просмотра различных видео и передач▶️'
    elif call.data == '3':
        answer = 'Вы можете насладиться музыкой в изолированно от ежедневной рутины🔊'
    elif call.data == '4':
        answer = 'Они будут вам как неотъемлемая часть жизни только на руке🕐'
    elif call.data == '5':
        answer = 'С помощью него вы можете выполнять сложные задачи и также выполнять свои работы не только в офисе но и дома🏦'
    elif call.data == '6':
        answer = 'Этот бот является помощником для покупки любой техники Apple от магазина iStore🍏, владельцем которого является Карабаев Рустам.\n Вы можете заказать и оплачивать не выходя из дома, также вы можете посмотреть информацию в шапке профиля бота и перед запуском ботаℹ️'
    elif call.data == '7':
        answer = 'https://www.apple.com/'
    elif call.data == '8':
        answer = '/start - Начало работы с ботом\n/products - Список продукций и их применение\n/calendar - Календарь для планирования своих действий\n/help - Помощь и дополнительная информация для пользователей'
    bot.send_message(call.message.chat.id, answer)


@bot.message_handler(func=lambda message: True)
def main_handler(message):
    if message.text == "📱 Smartphone":
        p = open("smartphone(images)/images(main)/download.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Раздел о смартфонах", reply_markup=smartphoneKB)

    elif message.text == "Iphone 12":
        p = open("smartphone(images)/images/iphone12.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Iphone 12 выбран\nЦена:750$", reply_markup=colorphoneKB)

    elif message.text == "Iphone 13":
        p = open("smartphone(images)/images/iphone13.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Iphone 13 выбран\nЦена:1100$", reply_markup=colorphoneKB)

    elif message.text == "Iphone 14":
        p = open("smartphone(images)/images/iphone14.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Iphone 14 выбран\nЦена:1450$", reply_markup=colorphoneKB)

    elif message.text == "🟣Purple":
        p = open("smartphone(images)/images/iphone14.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Фиолетовый цвет выбран", reply_markup=memoryphoneKB)

    elif message.text == "⚪️White":
        p = open("smartphone(images)/colours/whiteiphone14.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Белый цвет выбран", reply_markup=memoryphoneKB)

    elif message.text == "⚫️Black":
        p = open("smartphone(images)/colours/blackiphone14.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Черный цвет выбран", reply_markup=memoryphoneKB)

    elif message.text == "128 gb":
        bot.send_message(message.chat.id, "128 gb выбран", reply_markup=smartphoneKB)
    elif message.text == "256 gb":
        bot.send_message(message.chat.id, "256 gb выбран", reply_markup=smartphoneKB)
    elif message.text == "512 gb":
        bot.send_message(message.chat.id, "512 gb выбран", reply_markup=smartphoneKB)
    elif message.text == "1 TB":
        bot.send_message(message.chat.id, "1 TB выбран", reply_markup=smartphoneKB)


    elif message.text == "🖥Tab":
        p = open("tab(images)/images(main)/download.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Раздел о планшетах", reply_markup=tabKB)

    if message.text == "Ipad air":
        p = open("tab(images)/images/ipadair.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Ipad air выбран\nЦена:750$", reply_markup=colortabKB)

    elif message.text == "Ipad pro":
        p = open("tab(images)/images/ipadpro.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Ipad pro выбран\nЦена:1300$", reply_markup=colortabKB)

    elif message.text == "Ipad 10th generation":
        p = open("tab(images)/images/ipad10.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Ipad 10th generation выбран\nЦена:900$", reply_markup=colortabKB)
    if message.text == "🟡Yellow":
        p = open("tab(images)/colours/yellow.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Желтый цвет выбран", reply_markup=memorytabKB)

    elif message.text == "🟣Pink":
        p = open("tab(images)/colours/pink.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Розовый цвет выбран", reply_markup=memorytabKB)

    elif message.text == "🔵Blue":
        p = open("tab(images)/colours/blue.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Синний цвет выбран", reply_markup=memorytabKB)

    if message.text == "64 gb":
        bot.send_message(message.chat.id, "64 gb выбран", reply_markup=tabKB)
    elif message.text == "130 gb":
        bot.send_message(message.chat.id, "130 gb выбран", reply_markup=tabKB)


    elif message.text == "⌚️Watch":
        p = open("watch(images)/images(main)/download.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Раздел о часах", reply_markup=watchKB)

    if message.text == "Watch SE":
        p = open("watch(images)/images/watchse.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Watch SE выбран\nЦена:250$", reply_markup=colorwatchKB)

    elif message.text == "Watch series 8":
        p = open("watch(images)/images/watchseries8.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Watch series 8 выбраны\nЦена:480$", reply_markup=colorwatchKB)

    elif message.text == "Watch series Ultra":
        p = open("watch(images)/images/watchultr.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Watch Ultra выбран\nЦена:1000$", reply_markup=colorwatchKB)

    if message.text == "🟥Red":
        p = open("watch(images)/images/watchultra.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Красный цвет выбран", reply_markup=watchKB)

    elif message.text == "⬛️Grey":
        p = open("watch(images)/colours/watchgrey.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Серый цвет выбран", reply_markup=watchKB)



    elif message.text == "🎧 Headphone":
        p = open("headphones(images)/images(main)/images.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Раздел о наушниках", reply_markup=headphoneKB)

    if message.text == "Airpods Max":
        p = open("headphones(images)/images/airpodsmax.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Airpods Max выбраны\nЦена:800$", reply_markup=colorheadphoneKB)

    elif message.text == "Airpods pro 2":
        p = open("headphones(images)/images/airpodspro2.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Airpods pro 2 выбраны\nЦена:300$", reply_markup=colorheadphoneKB)

    elif message.text == "Airpods 3":
        p = open("headphones(images)/images/airpods3.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Airpods 3 выбраны\nЦена:220$", reply_markup=colorheadphoneKB)

    if message.text == "🟢Green":
        p = open("headphones(images)/colours/airpodsgreen.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Зеленые выбраны", reply_markup=categoryKB)

    elif message.text == "⬛️Black-white":
        p = open("headphones(images)/colours/airpodsblackwhite.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Черно-белые выбраны", reply_markup=categoryKB)

    elif message.text == "💠Blue-white":
        p = open("headphones(images)/colours/airpodsbluewhite.png", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Сине-белый выбраны", reply_markup=categoryKB)


    elif message.text == "💻Macbook":
        p = open("macbook(images)/images(main)/download.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Раздел о ноутбуках", reply_markup=macbookKB)

    if message.text == "Macbook air":
        p = open("macbook(images)/images/macbookair.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Macbook air выбран\nЦена:1200$", reply_markup=colormacbookKB)

    elif message.text == "Macbook M1":
        p = open("macbook(images)/colours/macbookgrey.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Macbook M1 выбран\nЦена:2250$", reply_markup=colormacbookKB)

    elif message.text == "Macbook M2":
        p = open("macbook(images)/images/macbookm2.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Macbook M2 выбран\nЦена:3850$", reply_markup=colormacbookKB)

    if message.text == "Silver":
        p = open("macbook(images)/colours/macbookgrey.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Silver цвет выбран", reply_markup=memorymacbookKB)

    elif message.text == "Mint":
        p = open("macbook(images)/colours/macbookmint.webp", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, "Mint цвет выбран", reply_markup=memorymacbookKB)

    if message.text == "2 TB":
        bot.send_message(message.chat.id, "2 TB выбран", reply_markup=macbookKB)
    elif message.text == "4 TB":
        bot.send_message(message.chat.id, "4 TB выбран", reply_markup=macbookKB)
    elif message.text == "⬅️Назад":
        bot.send_message(message.chat.id, "⬅️Меню", reply_markup=categoryKB)

    elif message.text == "Наш официальный сайт🌐":
        bot.send_message(message.chat.id, "https://www.apple.com/", reply_markup=categoryKB)

    elif message.text == "💰 Курс валют":
        data = requests.get('https://nbu.uz/uz/exchange-rates/json/').json()
        bot.send_message(message.chat.id, f'Покупка: {data[len(data) - 1]["nbu_buy_price"]}\n================\n' f'Продажа: {data[len(data) - 1]["nbu_cell_price"]}')


bot.infinity_polling()
