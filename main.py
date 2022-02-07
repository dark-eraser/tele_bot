import telebot
import pushbullet
# import img_analysis
bot = telebot.TeleBot('5274258108:AAHTFGSISX6XQ_K5AZU5lg7s0_BZFqEXZwI')
API_KEY = "o.vFmaJ46t3msllT0UPbjlyjAckdKIV6fV"
pb = pushbullet.Pushbullet(API_KEY)
DICTIONNARY = ['monitor', 'lautsprecher', 'möbel', 'kamera', 'apparat', 'stereo']
# img_analysis.IMG_ANALSIS

@bot.message_handler(content_types=['text'])
def echo_all(message):
    for txt in DICTIONNARY:
        if ((txt in message.text.lower())& ('suche' not in message.text.lower())):
            print(message.text)
            pb.push_note("new item", message.text)

@bot.message_handler(content_types=['photo'])
def photo(message):
    cap = message.caption
    print(cap)
    if cap != "":
        for txt in DICTIONNARY:
            if (txt in str(cap).lower()):
                pb.push_note("new item", cap)
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    print("downloaded img")
    

bot.infinity_polling()

