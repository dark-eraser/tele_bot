import telebot
import json
from img_analysis import A

# import img_analysis
jfile = json.load(open('credentials.json'))
bot = telebot.TeleBot(jfile['telegram_api'])
API_KEY = jfile ['pushbullet_api']
DICTIONNARY = [
'monitor', 'lautsprecher', 'möbel', 'kamera', 'apparat', 'stereo', 'handy',
'iphone', 'android', 'smartphone', 'kopfhörer', 'airpods', 'maschine', 'laptop','mac'
]
DICTIONNARY_img_recog = [
'monitor', 'speaker', 'furniture', 'camera', 'machine', 'stereo', 'smartphone',
'iphone', 'android', 'phone', 'headset', 'airpods', 'laptop','mac','computer',
'device', 'output', 'gadget', 'peripheral', 'electronic'
]
CHAT_ID = jfile['chat_id']



@bot.message_handler(content_types=['text'])
def text(message):
    for txt in DICTIONNARY:
        if ((txt in message.text.lower())& ('suche' not in message.text.lower())):
            print(message.text)
            bot.send_message(CHAT_ID, message.text)

@bot.message_handler(content_types=['photo'])
def photo(message):
    cap = message.caption
  
    # print("photo "+cap+ message.text)
    if cap != "":
        for txt in DICTIONNARY:
            if (txt in str(cap).lower()):
                bot.send_message(CHAT_ID, cap+message.text)
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    print("downloaded img")
    labels = A.detect_labels("image.jpg")
    for label in labels:
        for w in label.description.lower().split():
            if(w in DICTIONNARY_img_recog):
                bot.send_message(CHAT_ID, label.description+": "+str(label.score*100))
    
bot.infinity_polling()

