import telebot
from telebot import types
import sqlite3

name = ""

def db_table_val(user_id:int,nam: str, fone_numbe: str, lang: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT or IGNORE INTO user (user_id, name, fone_number, language) VALUES (?,?,?,?)', (user_id,nam,fone_numbe,lang))
        conn.commit()
def get_GO(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][2]
def get_GO1(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][3]
def get_GO_history(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][4]
def get_travel_history(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][5]
def get_name(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][1]
def get_lang(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][6]
def get_fone_number(us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user WHERE user_id=(?)', (us_id,)).fetchall()
    return res[0][2]
def get_update_name(message):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('UPDATE user SET name = (?) WHERE user_id = (?)', (message.text,message.from_user.id,)).fetchall()
    bot.send_message(message.from_user.id, text=f"{N[language][20].format(get_name(message.from_user.id))}\n{N[language][21].format(get_fone_number(message.from_user.id))}\n{N[language][22].format(get_GO1(message.from_user.id))}", reply_markup=keybord6)
def get_update_num(message):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('UPDATE user SET fone_number = (?) WHERE user_id = (?)', (message.text,message.from_user.id,)).fetchall()
    bot.send_message(message.from_user.id, text=f"{N[language][20].format(get_name(message.from_user.id))}\n{N[language][21].format(get_fone_number(message.from_user.id))}\n{N[language][22].format(get_GO1(message.from_user.id))}", reply_markup=keybord6)
def get_update_lang(lang, us_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute('UPDATE user SET language = (?) WHERE user_id = (?)', (lang,us_id,)).fetchall()


bot = telebot.TeleBot("1851402995:AAE4BFg8EbzQEhy0rJUGeWRY90akM7aMLCM")
N = {
    "ru":["Привет! Я GOGO, Как тебя зовут?",
          "Рад познакомиться {}. Отправьте нам ваш номер телефона с которым могут связаться наши пользователи",
          " {}, ваш номер {} на каких платформах еще зареган?",
          "{} отличных вам путешествий!",
          "Найти водителя",
          "Найти пассажира",
          "Мой баланс - {} GO",
          "Истоия моих поездок",
          "Мой профиль",
          "Поддержка",
          "История баланса",
          "История поездок",
          "Пополнить баланс",
          "назад в главное меню",
          "Сменить имя",
          "Сменить номер",
          "Сменить WhatsApp номер",
          "Сменить Telegram номер либо логин",
          "Сменить Вайбер номер",
          "Сменить логин в фейсбук мессенджер",
          "Ваше имя: {},",
          "Ваш номер: {},",
          "Ваш баланс: {} GO"],
    "en":["Hey! I'm GOGO, what's your name?",
          "Glad to meet {}. Send us your phone number that our users can contact",
          "{}, your number is {} on what platforms is it still registered?",
          "{} great travels!",
          "Find a driver",
          "Find a Passenger",
          "My balance is {} GO",
          "History of my travels",
          "My profile",
          "Support",
          "Balance history",
          "Travel history",
          "Top up balance",
          "back to the main menu",
          "Change name",
          "Change number",
          "Change WhatsApp number",
          "Change Telegram number or login",
          "Change Viber number",
          "Change your Facebook messenger login",
          "Your name: {},",
          "Your room number is: {},",
          "Your balance is: {} GO"],
    "de":["Hallo! Ich bin GOGO, wie heißt du?",
          "Freut mich dich kennen zu lernen {}. Senden Sie uns Ihre Telefonnummer, die unsere Benutzer kontaktieren können",
          "{}, deine Nummer ist {} auf welchen Plattformen ist sie noch registriert?",
          "{} tolle Reisen!",
          "Suchen Sie einen Fahrer",
          "Suche einen Passagier",
          "Mein Guthaben ist {} LOS",
          "Geschichte meiner Reisen",
          "Mein Profil",
          "Unterstützung",
          "Bilanzhistorie",
          "Reisegeschichte",
          "Guthaben aufladen",
          "zurück zum Hauptmenü",
          "Namen ändern",
          "Nummer wechseln",
          "WhatsApp-Nummer ändern",
          "Telegrammnummer oder Login ändern",
          "Viber-Nummer ändern",
          "Ändern Sie Ihr Facebook-Messenger-Login",
          "Ihr Name: {},",
          "Ihr Zimmernummer ist: {},",
          "Ihr Guthaben ist: {} GO"]}
keybord1 = types.InlineKeyboardMarkup(row_width=2)
keybord1.add(types.InlineKeyboardButton(text="Русский", callback_data="ru"),
             types.InlineKeyboardButton(text="English", callback_data="en"),
             types.InlineKeyboardButton(text="Deutsche", callback_data="de"))

@bot.message_handler(commands=["start"])
def send_mess(message):
    bot.send_message(message.from_user.id, text="Select language", reply_markup=keybord1)

@bot.message_handler(commands=["inf"])
def get_inf(message):
    print(get_name(message.from_user.id))

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global language
    global keybord3
    global keybord6
    if query.data == "en":
        language = "en"
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=N[language][0])
        bot.register_next_step_handler(query.message, reg_name)
    elif query.data == "ru":
        language = "ru"
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=N[language][0])
        bot.register_next_step_handler(query.message, reg_name)
    elif query.data == "de":
        language = "de"
        bot.send_message(query.message.chat.id, N[language][0])
        bot.register_next_step_handler(query.message, reg_name)
    elif query.data == "ru1":
        keybord6 = types.InlineKeyboardMarkup(row_width=2)
        i2 = 11
        for i in range(14, 20):
            keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][i], callback_data=f"{i2}"))
            i2 += 1
        keybord6.add(types.InlineKeyboardButton(text="Сменить язык", callback_data="17"))
        keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][13], callback_data="10"))
        get_update_lang("ru",query.message.chat.id)
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,text=f"{N[language][20].format(get_name(query.message.chat.id))}\n{N[language][21].format(get_fone_number(query.message.chat.id))}\n{N[language][22].format(get_GO1(query.message.chat.id))}",reply_markup=keybord6)
    elif query.data == "en1":
        keybord6 = types.InlineKeyboardMarkup(row_width=2)
        i2 = 11
        for i in range(14, 20):
            keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][i], callback_data=f"{i2}"))
            i2 += 1
        keybord6.add(types.InlineKeyboardButton(text="Сменить язык", callback_data="17"))
        keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][13], callback_data="10"))
        get_update_lang("en", query.message.chat.id)
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,text=f"{N[language][20].format(get_name(query.message.chat.id))}\n{N[language][21].format(get_fone_number(query.message.chat.id))}\n{N[language][22].format(get_GO1(query.message.chat.id))}",reply_markup=keybord6)
    elif query.data == "de1":
        keybord6 = types.InlineKeyboardMarkup(row_width=2)
        i2 = 11
        for i in range(14, 20):
            keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][i], callback_data=f"{i2}"))
            i2 += 1
        keybord6.add(types.InlineKeyboardButton(text="Сменить язык", callback_data="17"))
        keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][13], callback_data="10"))
        get_update_lang("de",query.message.chat.id)
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,text=f"{N[language][20].format(get_name(query.message.chat.id))}\n{N[language][21].format(get_fone_number(query.message.chat.id))}\n{N[language][22].format(get_GO1(query.message.chat.id))}",reply_markup=keybord6)
    elif query.data == "whatsapp" or query.data == "viber" or query.data == "telegram":
        keybord3 = types.InlineKeyboardMarkup(row_width=2)
        keybord3.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][4], callback_data="1"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][5], callback_data="2"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][6].format(get_GO1(query.message.chat.id)), callback_data="3"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][7], callback_data="4"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][8], callback_data="5"),
                     types.InlineKeyboardButton(text="FAQ", callback_data="6"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][9], callback_data="7"))
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=N[get_lang(query.message.chat.id)][3].format(get_name(query.message.chat.id)), reply_markup=keybord3)
    elif query.data == "3":
        keybord4 = types.InlineKeyboardMarkup(row_width=2)
        keybord4.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][12], callback_data="8"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][13], callback_data="9"))
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=f"{N[get_lang(query.message.chat.id)][6].format(get_GO1(query.message.chat.id))}\n{N[language][10]}{get_GO_history(query.message.chat.id)}", reply_markup=keybord4)
    elif query.data == "4":
        keybord5 = types.InlineKeyboardMarkup()
        keybord5.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][13], callback_data="10"))
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=f"{N[get_lang(query.message.chat.id)][11]}{get_travel_history(query.message.chat.id)}", reply_markup=keybord5)
    elif query.data == "5":
        keybord6 = types.InlineKeyboardMarkup(row_width=2)
        i2=11
        for i in range(14,20):
            keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][i],callback_data=f"{i2}"))
            i2 += 1
        keybord6.add(types.InlineKeyboardButton(text="Сменить язык", callback_data="17"))
        keybord6.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][13],callback_data="10"))
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=f"{N[get_lang(query.message.chat.id)][20].format(get_name(query.message.chat.id))}\n{N[get_lang(query.message.chat.id)][21].format(get_fone_number(query.message.chat.id))}\n{N[get_lang(query.message.chat.id)][22].format(get_GO1(query.message.chat.id))}", reply_markup=keybord6)
    elif query.data == "9":
        keybord3 = types.InlineKeyboardMarkup(row_width=2)
        keybord3.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][4], callback_data="1"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][5], callback_data="2"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][6].format(get_GO1(query.message.chat.id)), callback_data="3"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][7], callback_data="4"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][8], callback_data="5"),
                     types.InlineKeyboardButton(text="FAQ", callback_data="6"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][9], callback_data="7"))
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=N[get_lang(query.message.chat.id)][3].format(get_name(query.message.chat.id)), reply_markup=keybord3)
    elif query.data == "10":
        keybord3 = types.InlineKeyboardMarkup(row_width=2)
        keybord3.add(types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][4], callback_data="1"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][5], callback_data="2"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][6].format(get_GO1(query.message.chat.id)), callback_data="3"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][7], callback_data="4"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][8], callback_data="5"),
                     types.InlineKeyboardButton(text="FAQ", callback_data="6"),
                     types.InlineKeyboardButton(text=N[get_lang(query.message.chat.id)][9], callback_data="7"))
        bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=N[get_lang(query.message.chat.id)][3].format(get_name(query.message.chat.id)), reply_markup=keybord3)
    elif query.data == "11":
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="Введите имя")
        bot.register_next_step_handler(query.message, get_update_name)
    elif query.data == "12":
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="Введите номер телефона")
        bot.register_next_step_handler(query.message, get_update_num)
    elif query.data == "17":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton(text="Русский", callback_data="ru1"),
                   types.InlineKeyboardButton(text="English", callback_data="en1"),
                   types.InlineKeyboardButton(text="Deutsche", callback_data="de1"))
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="Выберите язык", reply_markup=markup)
    
def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, N[language][1].format(name))
    bot.register_next_step_handler(message,reg_fone)
def reg_fone(message):
    fone_number = message.text
    db_table_val(user_id=message.from_user.id, nam=name, fone_numbe=fone_number, lang=language)
    keybord2 = types.InlineKeyboardMarkup(row_width=2)
    keybord2.add(types.InlineKeyboardButton(text="WhatsApp", callback_data="whatsapp"),
                 types.InlineKeyboardButton(text="Viber", callback_data="viber"),
                 types.InlineKeyboardButton(text="Telegram", callback_data="telegram"))
    bot.send_message(message.from_user.id, N[language][2].format(name,fone_number), reply_markup=keybord2)
bot.polling(none_stop=True)