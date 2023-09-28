import telebot

BOT_TOKEN = '6324577120:AAHGIGO3F1EkEGUE4gCdINjDj4vb4g9TuVA'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

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
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
     """)

@bot.message_handler(commands=['content'])
def content(message):
    bot.reply_to(message,"We have various playlists and articles available!")

@bot.message_handler(commands=['python'])
def Python(message):
    bot.reply_to(message,"tutorial link : https://youtu.be/Tm5u97I7OrM")

@bot.message_handler(commands=['sql'])
def SQL(message):
    bot.reply_to(message,"tutorial link : https://youtu.be/pFq1pgli0OQ")

@bot.message_handler(commands=['java'])  
def Java(message):
    bot.reply_to(message,"tutorial link : https://youtu.be/i6AZdFxTK9I")

@bot.message_handler(commands=['skillup'])   
def Skillup(message):
    bot.reply_to(message,"tutorial link : https://www.simplilearn.com/?&utm_source=google&utm_medium=cpc&utm_term=%2Bwww%20%2Bsimplilearn%20%2Bcom&utm_content=803350713-40537012023-467574577661&utm_device=c&utm_campaign=Search-Brand-Broad-IN-AllDevice-adgroup-brand-navigation&gclid=Cj0KCQjw0oyYBhDGARIsAMZEuMv5mA9EysZZ5NfhK65Cb5OU0Q0TVC4con6DQzHF502-dfgA7QQFCgQaAu5sEALw_wcB")

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.reply_to(message,"You can contact on the official mail id")

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    bot.reply_to(message,f"You said {message.text}, use the commands using /")


bot.infinity_polling()