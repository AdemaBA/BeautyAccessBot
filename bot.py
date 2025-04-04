import telebot
import os

# Получаем токен из переменной окружения
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Список комедогенных ингредиентов
comedogenic_ingredients = [
    "Acetylated Lanolin", "Acetylated Lanolin Alcohol", "Algae Extract", "Algin",
    "Beeswax", "Bismuth", "Butyl Stearate", "Carrageenan", "Cetearyl Alcohol",
    "Ceteareth 20", "Cetyl Acetate", "Chlorella", "Chondrus Crispus",
    "Coal Tar", "Cocoa Butter", "Coconut Oil", "Cocos nucifera oil",
    "Isopropyl Myristate", "Isopropyl Palmitate", "Myristyl Myristate",
    "PEG 8 Stearate", "Red Algae", "Seaweed", "Shea Butter", "Sodium Laureth Sulfate",
    "Sodium Lauryl Sulfate", "Stearic Acid Tea", "Wheat Germ Oil", "Xylene"
]

# Обработка входящего сообщения
@bot.message_handler(func=lambda message: True)
def analyze_ingredients(message):
    text = message.text
    found = []

    for ingredient in comedogenic_ingredients:
        if ingredient.lower() in text.lower():
            found.append(ingredient)

    if found:
        response = "⚠️ Обнаружены комедогенные ингредиенты:\n\n" + "\n".join(found)
    else:
        response = "✅ Комедогенные ингредиенты не обнаружены!"

    bot.reply_to(message, response)

# Запуск бота
print("Polling started...")
bot.polling()
