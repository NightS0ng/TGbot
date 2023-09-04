import telebot
import subprocess
import psutil

bot = telebot.TeleBot('Bot token')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Отправьте /shutdown, чтобы безопасно выключить компьютер, /restart, чтобы перезагрузить его, или /status, чтобы узнать текущее состояние компьютера.")

@bot.message_handler(commands=['shutdown'])
def shutdown(message):
    bot.reply_to(message, "Компьютер выключается...")
    subprocess.call("shutdown /s /t 10", shell=True)

@bot.message_handler(commands=['restart'])
def restart(message):
    bot.reply_to(message, "Компьютер перезагружается...")
    subprocess.call("shutdown /r /t 10", shell=True)

@bot.message_handler(commands=['status'])
def status(message):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    
    if plugged:
        status = "Питание подключено"
    else:
        status = "Питание не подключено"
    
    bot.reply_to(message, f"Текущий уровень заряда батареи: {percent}%\nСтатус питания: {status}")

bot.polling()