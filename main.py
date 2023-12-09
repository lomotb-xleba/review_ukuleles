import telebot
import parser_1
import database

bot = telebot.TeleBot('6615769203:AAHrp4PiYLIwCmxwudQDKoQZ5b3ljHiWFTA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.register_next_step_handler(message, parser)
def parser(message):
    bot.send_message(message.chat.id, 'pars..')
    url="https://guitar-saloon.ru/shop/ukulele/"
    parser_1.parser(url)
    bot.send_message(message.chat.id, 'write your price range:')
    bot.register_next_step_handler(message, get_range)
def get_range(message):
    dao = database.DataAccessObject()
    print(dao)
    # n, m =map(int(message).split(' '))
    # for r in dao:
    #     if r[1]:    
    #         if n[0]<=float(r[1])<=n[1]:
    #             print("name   :",r[0])
    #             print("price  :",r[1])
    #             print("description   :",r[2])

bot.polling(none_stop=True)