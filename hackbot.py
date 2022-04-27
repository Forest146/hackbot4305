import telebot
from telebot import types, TeleBot
import time
bot: TeleBot = telebot.TeleBot("5181699381:AAFyXOIShOkwkIJQi82rwM1DPnbKYzPli8A")


@bot.message_handler(commands=["start"])
def start(message):
    ph = open('завантаження.png', 'rb')
    bot.send_photo(message.chat.id, ph, "Привет! Этот бот поможет тебе получить доступ к любой странице  в ВК или Инстаграм.")
    btn1 = types.KeyboardButton("Начать Взлом")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, "Чтобы приступить, нажми кнопку!", reply_markup=markup, )


@bot.message_handler(content_types=["text"])
def text(message):
    text_user = message.text
    if text_user.startswith('http'):
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Поиск аккаунта по взломаных базах данных....', reply_markup=a)
        time.sleep(4.3)
        bot.send_message(message.chat.id, 'Проверка аккаунта....')
        time.sleep(3.1)
        bot.send_message(message.chat.id, 'Взлом начался....')
        time.sleep(5.5)
        inline_markup = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton("Получить логин и пароль🔓", callback_data='pasw')
        inline_markup.add(btn_1)
        bot.send_message(message.chat.id, "Готово\nЛогин: a**ap2*4*9\nПароль: ro*5*k**5*8*6\nчтобы получить логин и пароль нажми на кнопку ", reply_markup=inline_markup)

    else:
        bot.send_message(message.chat.id, 'Вставь сюда ссылку на Инстаграм  или ВК')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'pasw':
                time.sleep(2)
                inlin_markup = types.InlineKeyboardMarkup()
                btn_2 = types.InlineKeyboardButton('Готово!', callback_data='ready')
                inlin_markup.add(btn_2)
                bot.send_message(call.message.chat.id,'Чтобы получить логин и пароль необходимо подписаться на канал:\nhttps://t.me/+Af_0JxvlKctiY2My\n Если отпишешься, то мы не сможем отправить тебе логин и  пароль😊 ', reply_markup=inlin_markup)
            if call.data == 'ready':
                time.sleep(2)
                inl_markup = types.InlineKeyboardMarkup()
                btn_3 = types.InlineKeyboardButton('Узнать статус логина и пароля', callback_data='wait')
                inl_markup.add(btn_3)
                bot.send_message(call.message.chat.id,"Отлично, ожидайте логин и пароль.", reply_markup=inl_markup)
            if call.data == 'wait':
                time.sleep(2)
                in_markup = types.InlineKeyboardMarkup()
                btn_4 = types.InlineKeyboardButton('Хорошо', callback_data='abc')
                in_markup.add(btn_4)
                bot.send_message(call.message.chat.id, "Еще не прошло достаточно времени ожидайте логин и пароль...", reply_markup=in_markup)
            if call.data == 'abc':
                time.sleep(2)
                inl_markup = types.InlineKeyboardMarkup()
                btn_3 = types.InlineKeyboardButton('Узнать статус логина и пароля', callback_data='wait')
                inl_markup.add(btn_3)
                bot.send_message(call.message.chat.id,"Отлично, ожидайте логин и пароль.", reply_markup=inl_markup)
    except Exception as e:
        print(repr(e))

bot.infinity_polling()