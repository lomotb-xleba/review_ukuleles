import telebot
import back_parser 
from database import DataAccessObject

bot = telebot.TeleBot('6615769203:AAHrp4PiYLIwCmxwudQDKoQZ5b3ljHiWFTA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, please write price range \n for example: "3000-5000".')
    bot.register_next_step_handler(message, parser)
def parser(message):
    global arg, j, h
    url="https://guitar-saloon.ru/shop/ukulele/"
    dao=DataAccessObject()
    aa=str(message.text)
    bot.send_message(message.chat.id, 'pars..please wait')
    a = back_parser.parser(url,aa)
    if a==0:
        bot.send_message(message.chat.id, 'there are no goods in this range \n please try again')
        bot.register_next_step_handler(message, parser)
    elif a=="ERROR":
        bot.send_message(message.chat.id, 'it is not a range \n please write a range \n for example: "3000-5000"')
        bot.register_next_step_handler(message, parser)
    else:
        dao.init()
        dao.create(a)
        arg=dao.show_base()
        j=0; h=1
        while j+2<30:
            bot.send_message(message.chat.id, f'{arg[j], arg[j+1],arg[j+2]}')
            j+=3
        j=0
        bot.send_message(message.chat.id, "that's a part of what I found \n do you want more (yes/no)")
        bot.register_next_step_handler(message, repeater) 
def repeater(message):
    global j, h
    j+=30; h+=1
    if str(message.text)!="yes" and str(message.text)!="no":
        bot.send_message(message.chat.id, "please write only yes or no")
        bot.register_next_step_handler(message, repeater)

    if str(message.text)=="yes" and h*30<len(f'{arg}'):
        while j+2<h*30:
            bot.send_message(message.chat.id, f'{arg[j], arg[j+1],arg[j+2]}')
            j+=3

        bot.send_message(message.chat.id, "that's a part of what I found \n do you want more (yes/no)")
        bot.register_next_step_handler(message, repeater)
    if str(message.text)=="no":
        bot.send_message(message.chat.id, "that's all I found \n you can try another range if you want")
        bot.register_next_step_handler(message, parser)


bot.polling(none_stop=True)
