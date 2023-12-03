import telebot

BOT_TOKEN = '6324577120:AAHGIGO3F1EkEGUE4gCdINjDj4vb4g9TuVA'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey, how are you doing?")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"""
    The following commands are available:
    
    /start -> Welcome to the channel
    /help -> This message
    /content ->We offers various courses free of course through our video tutorials
    /Python  -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification 
    /contact -> contact information 
     """)

@bot.message_handler(commands=['content'])
def content(message):
    bot.reply_to(message,"We have various playlists and articles available!")

@bot.message_handler(commands=['python'])
def Python(message):
    bot.reply_to(message,"tutorial link : https://www.youtube.com/watch?v=XKHEtdqhLK8")

@bot.message_handler(commands=['sql'])
def SQL(message):
    bot.reply_to(message,"tutorial link : https://www.youtube.com/watch?v=7S_tz1z_5bA")

@bot.message_handler(commands=['java'])  
def Java(message):
    bot.reply_to(message,"tutorial link : https://www.youtube.com/watch?v=BGTx91t8q50&t=28865s")

@bot.message_handler(commands=['skillup'])   
def Skillup(message):
    bot.reply_to(message,"tutorial link : https://varda-portfolio.vercel.app/")

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.reply_to(message,"You can contact on the official mail id")

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    bot.reply_to(message,f"You said {message.text}, use the commands using /")


bot.infinity_polling()