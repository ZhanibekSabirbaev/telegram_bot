import telebot
import config
from telebot import types
from googletrans import Translator
import json
import random
translator = Translator()

print((translator.translate("All okay", src="en", dest="ru")).text)


bot = telebot.TeleBot(config.TG_TOKEN)

kirill = 'абвгдеёжзийклмнопрстуфпхцчшщъыьэюя.,-+=!"№;%:?*()_<>`~'

mydb = config.DB_CONFIG

cursor = mydb.cursor(buffered=True)

try:

    # Извлекаю данные о Past Simple с БД и присваиваю эти данные к переменной pastsimple

    cursor.execute("SELECT PastSimple FROM verbtences")
    for past_simple in cursor:
        pastsimple = past_simple[0]
    print("Информация о Past Simple доступна")

    # Извлекаю данные о Present Simple с БД и присваиваю эти данные к переменной presentsimple

    cursor.execute("SELECT PresentSimple FROM verbtences")
    for present_simple in cursor:
        presentsimple = present_simple[0]
    print("Информация о Present Simple доступна")

    # Извлекаю данные о Future Simple с БД и присваиваю эти данные к переменной futuresimple

    cursor.execute("SELECT FutureSimple FROM verbtences")
    for future_simple in cursor:
        futuresimple = future_simple[0]
    print("Информация о Future Simple доступна")

    # Извлекаю данные о Past Continuous с БД и присваиваю эти данные к переменной pastcontinuous

    cursor.execute("SELECT PastContinuous FROM verbtences")
    for past_continuous in cursor:
        pastcontinuous = past_continuous[0]
    print("Информация о Past Continuous доступна")

    # Извлекаю данные о Present Continuous с БД и присваиваю эти данные к переменной presentcontinuous

    cursor.execute("SELECT PresentContinuous FROM verbtences")
    for present_continuous in cursor:
        presentcontinuous = present_continuous[0]
        print("Информация о Present Continuous доступна")

    # Извлекаю данные о Future Continuous с БД и присваиваю эти данные к переменной futurecontinuous

    cursor.execute("SELECT FutureContinuous FROM verbtences")
    for future_continuous in cursor:
        futurecontinuous = future_continuous[0]
        print("Информация о Future Continuous доступна")

    # Извлекаю данные о Past Perfect с БД и присваиваю эти данные к переменной pastperfect

    cursor.execute("SELECT PastPerfect FROM verbtences")
    for past_perfect in cursor:
        pastperfect = past_perfect[0]
        print("Информация о Past Perfect доступна")

    # Извлекаю данные о Present Perfect с БД и присваиваю эти данные к переменной presentperfect

    cursor.execute("SELECT PresentPerfect FROM verbtences")
    for present_perfect in cursor:
        presentperfect = present_perfect[0]
        print("Информация о Present Perfect доступна")

    # Извлекаю данные о Future Perfect с БД и присваиваю эти данные к переменной futureperfect

    cursor.execute("SELECT FuturePerfect FROM verbtences")
    for future_perfect in cursor:
        futureperfect = future_perfect[0]
        print("Информация о Future Perfect доступна")

    # Извлекаю данные о Past Perfect Continuous с БД и присваиваю эти данные к переменной pastperfectcontinuous

    cursor.execute("SELECT PastPerfectContinuous FROM verbtences")
    for past_perfect_continuous in cursor:
        pastperfectcontinuous = past_perfect_continuous[0]
        print("Информация о Past Perfect Continuous доступна")

    # Извлекаю данные о Present Perfect Continuous с БД и присваиваю эти данные к переменной presentperfectcontinuous

    cursor.execute("SELECT PresentPerfectContinuous FROM verbtences")
    for present_perfect_continuous in cursor:
        presentperfectcontinuous = present_perfect_continuous[0]
        print("Информация о Present Perfect Continuous доступна")

    # Извлекаю данные о Future Perfect Continuous с БД и присваиваю эти данные к переменной futureperfectcontinuous

    cursor.execute("SELECT FuturePerfectContinuous FROM verbtences")
    for future_perfect_continuous in cursor:
        futureperfectcontinuous = future_perfect_continuous[0]
        print("Информация о Future Perfect Continuous доступна")

    # Извлекаю данные об Adverbs с БД и присваиваю эти данные к переменной adverb

    cursor.execute("SELECT adverb FROM grammar")
    for adverbs in cursor:
        adverb = adverbs[0]
        print("Информация об adverbs доступна")

    # Извлекаю данные об Adverbs с БД и присваиваю эти данные к переменной adverb

    cursor.execute("SELECT adjective FROM grammar")
    for adjectives in cursor:
        adjective = adjectives[0]
        print("Информация об adjectives доступна")

finally:
    cursor.close()


class User:
    def __init__(self, message_chat_id):

        self.user_id = message_chat_id

        self.lst = []

        self.mydict = {}

        self.initial_amount = None

        self.count_correct = None

        self.count_incorrect = None

        self.added_words = None


current_user = None

# команда /start


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        cursor = mydb.cursor(buffered=True)
        sql = 'INSERT INTO userwords (user_id) VALUES (%s)'
        val = (message.chat.id,)
        cursor.execute(sql, val)
        mydb.commit()
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} \U0001F642 \n'
                                          'Я бот-помощник для изучения английского языка!\n'
                                          'Для получения информации нажми /help')
    except config.MYSQL_ERROR:
        cursor = mydb.cursor(buffered=True)
        bot.send_message(message.chat.id, "С возвращением! \U0001F601\n"
                                          "Воспользуйся командой /help")
        cursor.execute('alter table userwords auto_increment=1')
        mydb.commit()

    # команда /help


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "1. /translate поможет тебе перевести слова \U0001F4DA\n"
                                      "\n2. /grammar поможет тебе в изучении грамматики \U0001F4D6\n"
                                      "\n3. /words изучение, добавление и повторение слов \U0001F393\n"
                                      "\n4. /talk общение на английском \U0001F4AC\n"
                                      "\n5. /developer расскажет тебе о разработчике \U0001F466\n")

    # команда /grammar


@bot.message_handler(commands=['grammar'])
def grammar_message(message):
    bot.send_message(message.chat.id, "Вот список доступных тем:\n"
                                      "\n1. *Времена глагола*  /verbtences\n"
                                      "\n2. *Наречия*  /adverbs\n"
                                      "\n3. *Прилагательные*  /adjectives", parse_mode='Markdown')

    # команда /translate (при вызове команды предложится ввести слово для перевода)


@bot.message_handler(commands=['translate'])
def dictionary_message(message):
    button_quit = types.KeyboardButton('Выйти из переводчика')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_quit)
    a = bot.send_message(message.chat.id, "Введи слово для перевода \U0001F642", reply_markup=keyboard)
    bot.register_next_step_handler(a, translate)


def translate(message):
    word = message.text
    if word.lower() == "выйти из переводчика":
        bot.send_message(message.chat.id, f"Хорошо, {message.from_user.first_name} \U0001F642,"
                                          " выбери новую команду", reply_markup=types.ReplyKeyboardRemove())
    else:
        try:
            for x in word:
                if x.lower() in kirill:
                    bot.send_message(message.chat.id, f"Перевод: *"
                                                      f"{translator.translate(word, src='ru', dest='en').text.title()}*",
                                     parse_mode='Markdown')
                    break
                else:
                    bot.send_message(message.chat.id, f"Перевод: *"
                                                      f"{translator.translate(word, src='en', dest='ru', ).text.title()}*",
                                     parse_mode='Markdown')
                    break
            a = bot.send_message(message.chat.id, "Введи новое слово")
            bot.register_next_step_handler(a, translate)
        except Exception as error:
            print(error)
            bot.send_message(message.chat.id, "Ой, переводчик временно не работает \U0001F615")


@bot.message_handler(commands=['words'])
def words_message(message):
    bot.send_message(message.chat.id, "1. /learnwords изучение слов \U0001F520\n"
                                      "\n2. /addwords добавление слов \U0000270D\n"
                                      "\n3. /repeat повторение слов \U0001F9E0")

    # команда /developer


@bot.message_handler(commands=['developer'])
def start_message(message):
    bot.send_message(message.chat.id, "Разработчик этого бота - студент группы ИС-1705, Сабирбаев Жанибек")

    # команда /talk (При вызове команды начнется общение с ботом)


@bot.message_handler(commands=['talk'])
def dictionary_message(message):
    msg = bot.send_message(message.chat.id, "hello, lets talk")
    bot.register_next_step_handler(msg, talk_step)


def talk_step(message):
    word = message.text
    if word.lower() == 'hello':
        a = bot.send_message(message.chat.id, "How are you?")
        bot.register_next_step_handler(a, talk_step)
    elif word.lower() == 'good':
        b = bot.send_message(message.chat.id, 'Ok')
        bot.register_next_step_handler(b, talk_step)
    elif word.lower() == 'bye':
        bot.send_message(message.chat.id, 'ок')

# команда /verbtences(при вызове команды появятся кнопки для выбора времен глаголов)


@bot.message_handler(commands=['verbtences'])
def start_message(message):

    # создаем inline кнопки для выбора времени глагола

    inline_button_past_simple = types.InlineKeyboardButton('\U0001F4D6 Past Simple', callback_data='past.simple')
    inline_button_present_simple = types.InlineKeyboardButton('\U0001F4D6 Present Simple',
                                                              callback_data='present.simple')
    inline_button_future_simple = types.InlineKeyboardButton('\U0001F4D6 Future Simple',
                                                             callback_data='future.simple')

    # кнопка разделитель

    inline_button_verb1 = types.InlineKeyboardButton(' ', callback_data='verb1')

    # кнопки времен Continuous

    inline_button_past_continuous = types.InlineKeyboardButton('\U0001F4D6 Past Continuous',
                                                               callback_data='past.continuous')
    inline_button_present_continuous = types.InlineKeyboardButton('\U0001F4D6 Present Continuous',
                                                                  callback_data='present.continuous')
    inline_button_future_continuous = types.InlineKeyboardButton('\U0001F4D6 Future Continuous',
                                                                 callback_data='future.continuous')

    # кнопка разделитель

    inline_button_verb2 = types.InlineKeyboardButton(' ', callback_data='verb2')

    # кнопки времен Perfect

    inline_button_past_perfect = types.InlineKeyboardButton('\U0001F4D6 Past Perfect', callback_data='past.perfect')
    inline_button_present_perfect = types.InlineKeyboardButton('\U0001F4D6 Present Perfect',
                                                               callback_data='present.perfect')
    inline_button_future_perfect = types.InlineKeyboardButton('\U0001F4D6 Future Perfect',
                                                              callback_data='future.perfect')

    # кнопка разделитель

    inline_button_verb3 = types.InlineKeyboardButton(' ', callback_data='verb3')

    # кнопки времен Perfect Continuous

    inline_button_past_perfect_continuous = types.InlineKeyboardButton('\U0001F4D6 Past Perfect Continuous',
                                                                       callback_data='past.perfect.continuous')
    inline_button_present_perfect_continuous = types.InlineKeyboardButton('\U0001F4D6 Present Perfect Continuous',
                                                                          callback_data='present.perfect.continuous')
    inline_button_future_perfect_continuous = types.InlineKeyboardButton('\U0001F4D6 Future Perfect Continuous',
                                                                         callback_data='future.perfect.continuous')

    # добавляю созданные кнопки

    inline_keyboard = types.InlineKeyboardMarkup().add(inline_button_past_simple).add(inline_button_present_simple). \
        add(inline_button_future_simple).add(inline_button_verb1).add(inline_button_past_continuous). \
        add(inline_button_present_continuous).add(inline_button_future_continuous).add(inline_button_verb2). \
        add(inline_button_past_perfect).add(inline_button_present_perfect).add(inline_button_future_perfect). \
        add(inline_button_verb3).add(inline_button_past_perfect_continuous).add(
        inline_button_present_perfect_continuous). \
        add(inline_button_future_perfect_continuous)

    bot.send_message(message.chat.id, 'Пожалуйста, выбери любое время глагола', reply_markup=inline_keyboard)

    # обработчик inline кнопок(здесь выполняются действия, соответсвующие нажатой inline-кнопке)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'present.simple':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/sMQPVUGBonE")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Present Simple")
        bot.send_message(call.message.chat.id, presentsimple, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'past.simple':
        bot.answer_callback_query(call.id, text="Информация о Past Simple")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/PA-5w8TOBQ8")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, pastsimple, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'future.simple':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/4rNGbkpKAgc")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Future Simple")
        bot.send_message(call.message.chat.id, futuresimple, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'past.continuous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/GllsXVPAhhg")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Past Continuous")
        bot.send_message(call.message.chat.id, pastcontinuous, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'present.continuous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/wdGPEclofMI")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Present Continuous")
        bot.send_message(call.message.chat.id, presentcontinuous, reply_markup=keyboard,  parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'future.continuous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/rcVFEeRoIzc")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Future Continuous")
        bot.send_message(call.message.chat.id, futurecontinuous, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'past.perfect':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/zL5heUmiThc")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Past Perfect")
        bot.send_message(call.message.chat.id, pastperfect, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'present.perfect':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/_7CBgVx1e9E")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Present Perfect")
        bot.send_message(call.message.chat.id, presentperfect, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'future.perfect':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/gyeORf5qFjE")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Future Perfect")
        bot.send_message(call.message.chat.id, futureperfect, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'past.perfect.continuous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/gVkQrA1Mjuc")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Past Perfect Continuous")
        bot.send_message(call.message.chat.id, pastperfectcontinuous, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'present.perfect.continuous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/hcKyX-bmqz8")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Present Perfect Continuous")
        bot.send_message(call.message.chat.id, presentperfectcontinuous, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'future.perfect.continuous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/I_FI0soOnOc")
        keyboard.add(url_button)
        bot.answer_callback_query(call.id, text="Информация о Future Perfect Continuous")
        bot.send_message(call.message.chat.id, futureperfectcontinuous, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Список времен глагола: /verbtences")
    elif call.data == 'verb1' or call.data == 'verb2' or call.data == 'verb3':
        bot.answer_callback_query(call.id, text="Выбери любое время глагола")


# команда /adverbs(при вызове команды пользователю отправляется небольшое сообщение о наречиях
# и предлагается кнопка со ссылкой на сайт для подробного изучения)


@bot.message_handler(commands=['adverbs'])
def start_message(message):
    bot.send_message(message.chat.id, adverb, parse_mode='Markdown')
    # после сообщения создаем inline кнопку, с ссылкой на сайт с данной темой
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к Adverbs", url="https://grammarway.com/ru/adverbs")
    url_button1 = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/QRm0JxlAGQs")
    keyboard.add(url_button).add(url_button1)
    bot.send_message(message.chat.id, "Перейди по ссылке для подробного изучения", reply_markup=keyboard)

# команда /adjectives(при вызове команды пользователю отправляется небольшое сообщение о прилагательных
# и предлагается кнопка со ссылкой на сайт для подробного изучения)


@bot.message_handler(commands=['adjectives'])
def start_message(message):
    bot.send_message(message.chat.id, adjective, parse_mode='Markdown')
    # после сообщения создаем inline кнопку, с ссылкой на сайт с данной темой
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к Adjectives", url="https://grammarway.com/ru/adjectives")
    url_button1 = types.InlineKeyboardButton(text="Перейти к видеоуроку", url="https://youtu.be/0cMEa1Rd2XM")
    keyboard.add(url_button).add(url_button1)
    bot.send_message(message.chat.id, "Перейди по ссылке для подробного изучения", reply_markup=keyboard)


# команда /addwords(при вызове команды пользователю предлагается ввести слово с переводом в определенном формате,
# после введения слова, оно добавляется в БД)


@bot.message_handler(commands=['addwords'])
def add_word(message):

    # создаем кнопку выхода

    button_quit = types.KeyboardButton('Отменить добавление')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_quit)

    # сообщение которое отправляет бот после вызова команды /addwords

    a = bot.send_message(message.chat.id, 'Введи слово в формате *СЛОВО-ПЕРЕВОД*\n'
                                          '\nНапример \U0001F447\n'
                                          '\nfriend - друг\n'
                                          '\nЧтобы добавить несколько слов'
                                          ' нужно ввести каждое новое слово с новой строки\n'
                                          '\nНапример \U0001F447\n'
                                          '\nfriend - друг\n'
                                          'cat - кот\n'
                                          'dog - собака', reply_markup=keyboard, parse_mode='Markdown')
    bot.register_next_step_handler(a, add_word_step)


def add_word_step(message):

    cursor = mydb.cursor(buffered=True)
    word = message.text
    if word == 'Отменить добавление':
        bot.send_message(message.chat.id, f"Хорошо, {message.from_user.first_name} \U0001F642,"
                                          " выбери новую команду", reply_markup=types.ReplyKeyboardRemove())
        return
    current_user = User(message.chat.id)
    current_user.added_words = word.split('\n')
    for value in current_user.added_words:
        for value1 in value.split('-')[0]:
            if value1 in kirill:
                a = bot.send_message(message.chat.id, f"Ошибка в слове «*{value.split('-')[0].strip()}*»\n "
                                                      f"\nСлово должно быть английское!\n"
                                                      f"Ты можешь отправить всё заново в исправленном виде \U0001F609",
                                     parse_mode='Markdown')
                bot.register_next_step_handler(a, add_word_step)
                return

    cursor.execute(f"SELECT dict FROM userwords where user_id = {current_user.user_id}")
    for user_dict in cursor:
        if user_dict[0] == None:
            break
        else:
            current_user.mydict = json.loads(user_dict[0])
            for check_word in current_user.mydict.keys():
                for item in current_user.added_words:
                    if check_word in item:
                        current_user.lst.append(check_word)
                        current_user.added_words.remove(item)
    if len(current_user.added_words) == 0:
        msg = bot.send_message(message.chat.id, "Эти слова уже есть в твоем словаре, "
                                                "добавь что-нибудь новое \U0001F601")
        bot.register_next_step_handler(msg, add_word_step)
        return
    else:
        try:
            for words in current_user.added_words:
                current_user.mydict.update({words.split('-')[0].strip().lower(): words.split('-')[1].strip().lower()})
            current_user.mydict = json.dumps(current_user.mydict, ensure_ascii=False)
            cursor = mydb.cursor(buffered=True)
            sql = f"UPDATE userwords SET dict=%s WHERE user_id={current_user.user_id}"
            val = (current_user.mydict,)
            cursor.execute(sql, val)
            mydb.commit()
        except IndexError:
            a = bot.send_message(message.chat.id, 'Введи слово в формате *СЛОВО-ПЕРЕВОД*\n'
                                                  '\nНапример \U0001F447\n'
                                                  '\nfriend - друг', parse_mode='Markdown')
            bot.register_next_step_handler(a, add_word_step)
            return

    if len(current_user.lst) == 0:
        bot.send_message(message.chat.id, 'Слова успешно добавлены в твой словарь! \U00002705',
                         reply_markup=types.ReplyKeyboardRemove())
        return
    else:
        bot.send_message(message.chat.id, f'Некоторые слова (*{", ".join(current_user.lst)}*) уже есть в твоем словаре.'
                                          f' Они не будут добавлены повторно!', parse_mode='Markdown')
        bot.send_message(message.chat.id, 'Остальные слова успешно добавлены в твой словарь! \U00002705',
                         reply_markup=types.ReplyKeyboardRemove())
        return


# команда /learnwords

@bot.message_handler(commands=['learnwords'])
def learn_words(message):
    button_know = types.KeyboardButton('Я знаю это \U0001F60E')
    button_learn = types.KeyboardButton('Изучить \U00002705')
    button_bye = types.KeyboardButton('Закончить изучение \U0001F3C1')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)\
        .row(button_know, button_learn).add(button_bye)
    current_user = User(message.chat.id)

    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM dictionary order by rand()")

    def learn_step(message):
        word = message.text
        cursor = mydb.cursor(buffered=True)
        cursor.execute("SELECT * FROM dictionary order by rand()")
        if word == "Я знаю это \U0001F60E":
            bot.send_message(message.chat.id, 'Ладно, едем дальше \U0001F44D')
            for x in cursor:
                bot.send_message(message.chat.id, f"\U0001F4D6 *{x[1].upper()}* - {x[2]}", parse_mode='Markdown')
                audio = open(rf'D:/Projects/words/{x[1].lower()}.ogg', 'rb')
                a = bot.send_audio(message.from_user.id, audio)
                audio.close()
                bot.register_next_step_handler(a, learn_step)
                del current_user.lst[0]
                del current_user.lst[0]
                current_user.lst.append(x[1])
                current_user.lst.append(x[2])
                print(current_user.lst)
                break
        elif word == "Изучить \U00002705":
            cursor2 = mydb.cursor(buffered=True)
            cursor2.execute(f"SELECT dict FROM userwords where user_id = {current_user.user_id}")
            for user_dict in cursor2:
                try:
                    current_user.mydict = json.loads(user_dict[0])
                except TypeError:
                    break
            try:
                current_user.mydict.update({current_user.lst[0]: current_user.lst[1]})
                current_user.mydict = json.dumps(current_user.mydict, ensure_ascii=False)
                sql = f"UPDATE userwords SET dict=%s WHERE user_id={current_user.user_id}"
                val = (current_user.mydict,)
                cursor2.execute(sql, val)
                mydb.commit()
                bot.send_message(message.chat.id, "Я добавил это в твой словарь! \U0001F609")
                for x in cursor:
                    bot.send_message(message.chat.id, f"\U0001F4D6 *{x[1].upper()}* - {x[2]}",
                                         parse_mode='Markdown')
                    audio = open(rf'D:/Projects/words/{x[1].lower()}.ogg', 'rb')
                    a = bot.send_audio(message.from_user.id, audio)
                    audio.close()
                    bot.register_next_step_handler(a, learn_step)
                    del current_user.lst[0]
                    del current_user.lst[0]
                    current_user.lst.append(x[1])
                    current_user.lst.append(x[2])
                    break
            except KeyError:
                bot.send_message(message.chat.id, "Это слово уже есть в твоем словаре!")
                for x in cursor:
                    bot.send_message(message.chat.id, f"\U0001F4D6 *{x[1].upper()}* - {x[2]}", parse_mode='Markdown')
                    audio = open(rf'D:/Projects/words/{x[1].lower()}.ogg', 'rb')
                    a = bot.send_audio(message.from_user.id, audio)
                    audio.close()
                    bot.register_next_step_handler(a, learn_step)
                    del current_user.lst[0]
                    del current_user.lst[0]
                    current_user.lst.append(x[1])
                    current_user.lst.append(x[2])
                    break
        elif word == "Закончить изучение \U0001F3C1":
            del current_user.lst[0]
            del current_user.lst[0]
            bot.send_message(message.chat.id, f'Okay, до скорого! \U0001F60A', reply_markup=types.ReplyKeyboardRemove())
            return
    for x in cursor:
        bot.send_message(message.chat.id, "Let's go!")
        bot.send_message(message.chat.id, f"\U0001F4D6 *{x[1].upper()}* - {x[2]}", parse_mode='Markdown',
                         reply_markup=keyboard)
        audio = open(rf'D:/Projects/words/{x[1].lower()}.ogg', 'rb')
        a = bot.send_audio(message.from_user.id, audio)
        audio.close()
        bot.register_next_step_handler(a, learn_step)
        current_user.lst.append(x[1])
        current_user.lst.append(x[2])
        print(current_user.lst)
        break

# команда /repeat


@bot.message_handler(commands=['repeat'])
def repeat(message):
    button_show = types.KeyboardButton('Показать значение \U0001F914')
    button_bye = types.KeyboardButton('Остановить повторение \U0001F3C1')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)\
        .add(button_show).add(button_bye)
    if message.text == "Остановить повторение \U0001F3C1":
        return
    current_user = User(message.chat.id)
    cursor = mydb.cursor(buffered=True)
    cursor.execute(f"SELECT dict FROM userwords where user_id = {current_user.user_id}")
    for x in cursor:
        try:
            current_user.mydict = json.loads(x[0])
            lst = list(current_user.mydict.items())
            random.shuffle(lst)
            current_user.mydict = dict(lst)
            current_user.initial_amount = len(current_user.mydict)
            current_user.count_correct = len(current_user.mydict)
            current_user.count_incorrect = len(current_user.mydict)
        except TypeError:
            bot.send_message(message.chat.id, "В твоем словаре еще нет слов для повторения \U0001F601\n"
                                              "\nПредлагаю тебе:\n"
                                              "\n1. /learnwords - изучить новые слова\n"
                                              "\n2. /addwords - добавить свои слова",
                             reply_markup=types.ReplyKeyboardRemove())
            return
    bot.send_message(message.chat.id, "Отлично! Давай повторим слова, добавленные в твой словарь.\n"
                                      "Твоя задача вспомнить их значение на английском \U0001F60A",
                     reply_markup=keyboard)
    print(current_user.mydict)

    def repeat_step(message):
        word = message.text
        for x in current_user.mydict:
            if word.lower().strip() == x:
                current_user.count_correct -= 1
                bot.send_message(message.chat.id, 'Good job \U0001F44D')
                del current_user.mydict[x]
                break
            elif word == 'Остановить повторение \U0001F3C1':
                bot.send_message(message.chat.id, f'Ты повторил '
                                                  f'*{current_user.initial_amount-len(current_user.mydict)}* '
                                                  f'слов(а) из твоего словаря!\n'
                                                  f'\n\U00002705 Правильных переводов: '
                                                  f'*{current_user.initial_amount-current_user.count_correct}*\n'
                                                  f'\n\U0000274E Кол-во не переведенных слов: '
                                                  f'*{current_user.initial_amount-current_user.count_incorrect}*\n'
                                                  f'\n\U0001F4DA Всего слов в твоем словаре: '
                                                  f'*{current_user.initial_amount}*',
                                 parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
                return
            elif word == 'Показать значение \U0001F914':
                current_user.count_incorrect -= 1
                for value in current_user.mydict.keys():
                    bot.send_message(message.chat.id, f'*{value.title()}*', parse_mode='Markdown')
                    try:
                        audio = open(rf'D:/Projects/words/{value.lower()}.ogg', 'rb')
                        bot.send_audio(message.from_user.id, audio)
                        audio.close()
                        break
                    except FileNotFoundError:
                        break
                for key in current_user.mydict.keys():
                    del current_user.mydict[key]
                    break
                break
            else:
                a = bot.send_message(message.chat.id, "No, try again \U0001F609")
                bot.register_next_step_handler(a, repeat_step)
                return

        if len(current_user.mydict) != 0:
            for z in current_user.mydict.values():
                a = bot.send_message(message.chat.id, f"Переведи слово:"
                                                      f"\n\U0001F4D6 *{z.upper()}*", parse_mode='Markdown')
                bot.register_next_step_handler(a, repeat_step)
                break
        else:
            bot.send_message(message.chat.id, f'Ты повторил *все* слова из твоего словаря, молодец! \U0001F44D\n'
                                              f'\n\U00002705 Правильных переводов: '
                                              f'*{current_user.initial_amount - current_user.count_correct}*\n'
                                              f'\n\U0000274E Кол-во не переведенных слов: '
                                              f'*{current_user.initial_amount - current_user.count_incorrect}*\n'
                                              f'\n\U0001F4DA Всего слов в твоем словаре: '
                                              f'*{current_user.initial_amount}*',
                             parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
            return

    for i in current_user.mydict.values():
        a = bot.send_message(message.chat.id, f"Переведи слово:\n\U0001F4D6 *{i.upper()}*", parse_mode='Markdown')
        bot.register_next_step_handler(a, repeat_step)
        break


# ответы на сообщения пользователя


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "привет" or message.text.lower() == "хай":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")
    elif message.text.lower() == "пока" or message.text.lower() == "bye":
        bot.send_message(message.chat.id, f"До новых встреч, {message.from_user.first_name}!")
    elif message.text.lower() == "мой айди":
        bot.send_message(message.chat.id, f"Твой id: {message.chat.id}")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, воспользуйся командой /help")


bot.polling(none_stop=True)
