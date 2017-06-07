import os
import telebot
from PIL import Image

insert_text = '✅ درج نوار حمایتی'
welcome_text = 'درود. برای درج نوار حمایتی روی تصویر نمایهٔ خود، دکمهٔ زیر را بزنید.'
wait_text = 'لطفاً چند لحظه صبر کنید…'
promo_text= 'با سپاس! لطفا دوستان خود را نیز دعوت کنید.\n #اتحادایران\n @etehadiran_bot'

def insert_banner(pic):
    #resize image to banner size
    im = Image.open(pic, 'r')
    size = 400, 400
    thumb = im.resize(size)
    #apply banner
    banner = Image.open('wmark.png', 'r')
    thumb.paste(banner, (0, 0), banner)
    thumb.save(pic, "PNG")

TOKEN = 'Your Token'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chatid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup()
    item_insert = telebot.types.KeyboardButton(insert_text)
    markup.row(item_insert)
    bot.send_message(chatid, welcome_text , reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == insert_text)
def insert(message):
    try:
        chatid = message.chat.id
        sender = message.from_user
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(chatid, wait_text, reply_markup=markup)
        try:
            pic = bot.get_user_profile_photos(sender.id, 0).photos[0][-1]
            path=bot.get_file(pic.file_id).file_path
            address="https://api.telegram.org/file/bot"+TOKEN+"/"+path
            image_name = str(chatid)+".jpg"
            downloaded_file = bot.download_file(path)
            with open(image_name,'wb') as old_pic:
                old_pic.write(downloaded_file)
            insert_banner(image_name)
            bot.send_chat_action(chatid, "upload_photo")
            with open(image_name,'rb') as new_pic:
                bot.send_photo(chatid, new_pic)
            os.remove(image_name)
        except IndexError:
            bot.send_chat_action(chatid, "upload_photo")
            with open('wmark.png','rb') as new_pic:
                bot.send_photo(chatid, new_pic)
        try:
            bot.send_message(chatid, promo_text)
        except FileNotFoundError:
            pass
    except:
        pass

bot.polling(none_stop=True)
