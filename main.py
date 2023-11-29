import telebot

bot = telebot.TeleBot('6562163720:AAFG17bguAPuAPjPuHz-whunRar-ArWcHck')


@bot.message_handler(commands=['Hello!'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Меня зовут ТелеНав. Я отправлю тебе 3 сообщения')


@bot.message_handler(commands=['first_message'])
def main(message):
    bot.send_message(message.chat.id, 'Сегодня у тебя будет *замечательный* день', pars_mode='Markdown')


@bot.message_handler(commands=['second_message'])
def main(message):
    bot.send_message(message.chat.id, 'С вами приятно иметь дело!')


@bot.message_handler(commands=['third_message'])
def main(message):
    bot.send_message(message.chat.id, 'Удачного дня!', pars_mode='Markdown')


bot.infinity_polling()
