import telebot
import json
import pushbullet
# import img_analysis
jfile = json.load(open('credentials.json'))
bot = telebot.TeleBot(jfile['telegram_api'])
API_KEY = jfile ['pushbullet_api']
pb = pushbullet.Pushbullet(API_KEY)
DICTIONNARY = [
'monitor', 'lautsprecher', 'möbel', 'kamera', 'apparat', 'stereo', 'handy',
'iphone', 'android', 'smartphone', 'kopfhörer'
]
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

