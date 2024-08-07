import telebot

bot = telebot.TeleBot('7084337272:AAEQS4PlKLEmRw4_VMqLrD-8l4sM-o-BpIE')


@bot.message_handler(commands=['start'])
def start_main(message):
    bot.send_message(message.chat.id, '*Nay*', parse_mode='Markdown')


@bot.message_handler(commands=['mew'])
def mew_main(message):
    bot.send_message(message.chat.id, 'How are you?', )


@bot.message_handler(commands=['cat'])
def cat_main(message):
    bot.send_message(message.chat.id, '*Nay, What your name?*', parse_mode='Markdown')


@bot.message_handler(commands=['new'])
def new_main(message):
    bot.send_message(message.chat.id, 'ссылка', parse_mode='Markdown')


bot.infinity_polling()
