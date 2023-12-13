import telebot
import back_parser
from database import DataAccessObject

bot = telebot.TeleBot('6615769203:AAHrp4PiYLIwCmxwudQDKoQZ5b3ljHiWFTA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, please write price range \n for example: "3000-5000".')
    bot.register_next_step_handler(message, parser)
def parser(message):
    bot.send_message(message.chat.id, 'pars..please wait')
    url="https://guitar-saloon.ru/shop/ukulele/"
    dao=DataAccessObject()
    aa=str(message.text)
    a = back_parser.parser(url,aa)
    dao.init()
    dao.create(a)
    arg=dao.show_base()
    j=0
    while j<len(f'{arg}'):
        bot.send_message(message.chat.id, f'{arg[j]}')
        j+=1
    #self.bot.send_message(message.chat.id, 'write your price range:')
#    self.bot.register_next_step_handler(message, get_range)
# def get_range(message):
    # dao = database.DataAccessObject()
    # dao.create(arg)
    # print(dao)
    # n, m =map(int(message).split(' '))
    # for r in dao:
    #     if r[1]:    
    #         if n[0]<=float(r[1])<=n[1]:
    #             print("name   :",r[0])
    #             print("price  :",r[1])
    #             print("description   :",r[2])

bot.polling(none_stop=True)

