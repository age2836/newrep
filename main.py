

import telebot
import time
from telebot import types

bot = telebot.TeleBot("1844267856:AAHei-Lj8hl5Jph0S2vT5I1WuLNYOJnRVWw")

# команда старт
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
	name = message.from_user.first_name
	bot.send_message(message.chat.id,"😎 Привет, " + str(name) + "!" + "\nВведи свой город")

@bot.message_handler(content_types=['text'])
def send_text(message):
        otvet = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("🙎‍♀ Девушка", url="https://m-loves.ru")
        button2 = types.InlineKeyboardButton("🙎‍♂ Парень", callback_data='boy')
        otvet.add(button1, button2)
        bot.send_message(message.chat.id, "Отлично, твой город " + str(message.text) + "!" + "\nКто ты?", reply_markup=otvet)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "boy":
            vozrast = types.InlineKeyboardMarkup(row_width=4)
            but1 = types.InlineKeyboardButton("18-30", callback_data='1')
            but2 = types.InlineKeyboardButton("31-43", callback_data='1')
            but3 = types.InlineKeyboardButton("44 и старше", callback_data='1')
            vozrast.add(but1, but2, but3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сколько тебе лет?", reply_markup=vozrast)

        elif call.data == "1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            otvet = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button2 = types.InlineKeyboardButton("➡", callback_data='2')
            otvet.add(button1, button2)
            file = open('1.jpg', 'rb')
            bot.send_photo(call.message.chat.id, file, "Вика, 22 года Ищу надежного сильного и заботливого мужчину для интимных встречь. 🔥 есть квартира пишите не стесняйтесь ", reply_markup=otvet)

        elif call.data == "2":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='1')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='3')
            otvet.add(button1, button2, button3)
            file = open('2.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Валерия, 25 лет Здравствуйте , я ищу надежного, достойного, доброго, сильного и уравновешенного по характеру, целеустремленного, заботливого, уверенного в себе мужчину. Люблю трах в попку. А ещё мне нравится когда облизывают мое тело"), reply_markup=otvet)

        elif call.data == "3":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='2')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='4')
            otvet.add(button1, button2, button3)
            file = open('3.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Вика, 22 года Ищу надежного сильного и заботливого мужчину для интимных встречь. 🔥 есть квартира )По началу могу быть немного стеснительна,но зато потом...😅👍🔞пишите ,жду 🥺"), reply_markup=otvet)

        elif call.data == "4":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='3')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='5')
            otvet.add(button1, button2, button3)
            file = open('4.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Ника, 23 года Люблю хороший развратный секс в котором можно осуществлять разные, порой даже запретные фантазии.нюдсы только в моем профиле 👇 .Так же очень люблю выполнять всякие желания ,игрушки 🔞имеются 😋"), reply_markup=otvet)

        elif call.data == "5":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='4')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='6')
            otvet.add(button1, button2, button3)
            file = open('5.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Юля, 42 года Я обеспеченная взрослая дама, большую часть времени провожу на работе, но иногда хотеться мужской ласки.Познакомлюсь со свободным мужчиной от 25. Отношений не ищу, интересуют интимные встречи, встречаться можем у меня. Есть авто,могу забрать если нужно ,Фото могу отправить, пишите я не кусаюсь)"), reply_markup=otvet)

        elif call.data == "6":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='5')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='7')
            otvet.add(button1, button2, button3)
            file = open('6.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Алина - 18 лет, худышка.Ищу мужчину для приятного ... на расстояние(Видеозвонок-Фото-Переписка) Я сексуальная девушка без комплексов, , покажу вам своё видео, фото или онлайн трансляцию! Для адекватных могу выступать и с личиком и даже не исключаю реальных встреч."), reply_markup=otvet)

        elif call.data == "7":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='6')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='8')
            otvet.add(button1, button2, button3)
            file = open('7.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Маша, 24 года Обожаю секс! Я знаю, что делать руками, губами, языком… Мое сексуальное изящное тело и пылкий темперамент доведут вас до изнеможения.В поисках экзотического разнообразия, выходящего за все рамки... 😏Есть очень много разных игрушек, плеток и приспособ, мне не нужен обычный секс, поэтому если не умеешь ими пользоваться, не пиши!Цель знакомства: регулярный секс, виртуальное общение, bdsm, хочу умелого мужчину который сможет только руками и языком доводить до сквирта 😍💦"), reply_markup=otvet)

        elif call.data == "8":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='7')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='9')
            otvet.add(button1, button2, button3)
            file = open('8.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Света, 23 года Буду рада встречам 1-2 раза в неделю с мужчиной в возрасте от 23 до 43 лет. Ceкc очень люблю, поэтому будьте готовы тpaxaтьcя всю нoчь!)"), reply_markup=otvet)

        elif call.data == "9":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='8')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='10')
            otvet.add(button1, button2, button3)
            file = open('9.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Лиза, 27 лет. Хочу чтобы ты жестко тpaxнул мою пoпку. Просто напиши и договоримся о всех деталях встречи) Жду тебя"), reply_markup=otvet)

        elif call.data == "10":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='9')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='11')
            otvet.add(button1, button2, button3)
            file = open('10.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Катя 19 лет ищу взрослого опытного мужчину пишите отвечу всем парни молодые тоже пишите может пошалим я вас научу😜"), reply_markup=otvet)

        elif call.data == "11":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='10')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='12')
            otvet.add(button1, button2, button3)
            file = open('11.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Настолько люблю cocaть члeн, что готова делать это бесплатно каждый день! "), reply_markup=otvet)

        elif call.data == "12":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='11')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='13')
            otvet.add(button1, button2, button3)
            file = open('12.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Хочу пошлого мальчика 💋 Напишет мне кто-нибудь? Скучно 😔 Люблю сверху и paкoм. Жду сообщений"), reply_markup=otvet)

        elif call.data == "13":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='12')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='14')
            otvet.add(button1, button2, button3)
            file = open('13.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Аня, 21 год Обожаю трaxaться! Ищу того, кто сможет поставить меня рaком и трaxaть несколько часов подряд! Можешь даже вместе с друзьями 😊"), reply_markup=otvet)

        elif call.data == "14":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='13')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='15')
            otvet.add(button1, button2, button3)
            file = open('14.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Недавно исполнилось 18 лет Хочешь вcунуть в мою узeнькую пиceчку? В пoпку даю только со смазкoй!"), reply_markup=otvet)

        elif call.data == "15":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='14')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='16')
            otvet.add(button1, button2, button3)
            file = open('15.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Виктория, 28 лет Люблю когда меня дерут в общественных местах  Огромный опыт, моему разврату нет предела 🔥Хотим с подругой устроить секс вечеринку где парни будут в роли нашей прислуги! 😍Требуются незакомплексованые молодые люди от 25 лет и с членом от 16 см!Пишите я не кусаюсь 💋"), reply_markup=otvet)

        elif call.data == "16":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='15')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='17')
            otvet.add(button1, button2, button3)
            file = open('16.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Незамужняя. Хочу найти не старого любoвника, есть фото без лифчика и трусиков. Пиши если заинтересован.Нужен только сeкc и очень часто, никаких ухаживаний и отношений. Встретились, потрaxалиcь, и разбежались 💦 Иногда устраиваем девичник и нам очень скучно без парней, поэтому парни с большими компаниями вам ко мне 😜"), reply_markup=otvet)

        elif call.data == "17":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='16')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='18')
            otvet.add(button1, button2, button3)
            file = open('17.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "📸 Фотографировать себя это моя маленькая слабость, муж об этом не знает 👙🤫В поисках личного фотографа ❤️ Возможны дальнейшие отношения.Мне нравится читать ваши комментарии, очень возбуждает! 🔥 Комментируйте фото и видео, пишите запросы как сфотографироваться и в какой позе, в каком белье, я люблю исполнять заказы и радовать вас собой😘"), reply_markup=otvet)

        elif call.data == "18":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='17')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='19')
            otvet.add(button1, button2, button3)
            file = open('18.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Я немного стеснительная, но обожаю смотреть развратное порно, генгбенг, бдсм, лезби доминирование!В жизни секс не отличался особым разнообразием, но фантазий развратных предостаточно, которые хотелось бы воплотить в реале 🤤Хочу попробовать пошалить с парнем по видеосвязи😅 Пишите без комплексов, обсудим 💋"), reply_markup=otvet)

        elif call.data == "19":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='18')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='20')
            otvet.add(button1, button2, button3)
            file = open('19.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Оля, 20 лет Человек я творческий. Занимаюсь журналистикой, пишу песенки, стихи. Не могу и дня представить без хорошей музыки в ушах . Люблю своих друзей, котейку, ходить на концерты, читать хорошие книги, интересные места и неординарных людей с богатой фантазией 😏Пока родителей дома нет, я люблю становится рачком и насаживать себя на различные игрушки, которых у меня ну ооочень много, и хотела бы с кем то поделиться фотками и видео, возбуждает когда на меня дрочат) Раньше никогда этим не занималась 🤷‍♀️Пиши если ты думаешь что можешь меня заинтересовать!При взаимной симпатии возможно многое 💋"), reply_markup=otvet)

        elif call.data == "20":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='19')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='21')
            otvet.add(button1, button2, button3)
            file = open('20.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Встречусь с парнем (группой), желаю подчиняться , люблю унижения и наказания. Нужно сделать фототчёт для мужа рогоносца ❤️Возраст от 21 года.  Конфиденциальность строго соблюдается. Место для встреч есть. Исключительно индивидуальный подход. Необходимая атрибутика и девайсы имеются.  В теме много лет! 😏Кайфую от практик бондажа, порки, контроля оргазма. Хочу быть униженной и наказанной 🔥"), reply_markup=otvet)

        elif call.data == "21":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='20')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='22')
            otvet.add(button1, button2, button3)
            file = open('21.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Наташа, 24 года Интересует Встреча Или Вирт! Общение, дружба все это не ко мне !!! Обожаю секс во всех его проявлениях 🔥Нравятся всякие фетиши и особенно мужское доминирование, но по твоей просьбе могу сесть мокрой киской на лицо 😏💦 Отбираю лучший член в моей коллекции, ваше портфолио кидайте в личку, НЕ НА СТЕНУ! "), reply_markup=otvet)

        elif call.data == "22":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='21')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='23')
            otvet.add(button1, button2, button3)
            file = open('22.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Мила, 22 года Рыжеволосая замужняя бестия, ищу развратного мужчину для интимных встречь. 🔥Мои интересы анальный секс, подчинение, связывание с широко раздвинутыми ногами, игры со спермой, секс в людных местах , общественных туалетах. Скрашу вечер группе мужчин в поездке, сауне. Хочу попробовать ганг- бенг. 😍Будет ещё плюсиком если вы любите в процессе снимать все на камеру, прям очень возбуждает эта темка, есть собственная коллекция порнофильмов 😏Кончаю от ваших комплиментиков под моими фотками и видосами, пишите БОЛЬШЕ, всем рада 💋"), reply_markup=otvet)

        elif call.data == "23":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='22')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='24')
            otvet.add(button1, button2, button3)
            file = open('23.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Кира, 21 год Встретимся с парнем или группой парней на выходных! Ушла от родителей, выносят мозг 🤦‍♀️Есть подруга у которой сейчас и обитаю, у неё можно и организовать встречу 😏 Любим меф и порно! 💦Скучно уже вдвоём развлекаться, нужны не стеснительные выносливые ребята!Пишите, не стесняйтесь, мы общительные, можем повиртить 🔥"), reply_markup=otvet)

        elif call.data == "24":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='23')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='25')
            otvet.add(button1, button2, button3)
            file = open('24.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Вика, 22 года. Ещё учусь в универе. Не курю, выпиваю редко.Я открытый, добрый и веселый человек, хочется больше экспериментов в сексе 🔥Бывший был мудаком, часто бухал и обижал меня, поэтому ищу адекватного парня желающего воплотить все свои самые развратные фантазии со мной! Возможны длительные отношения ❤️Сразу пишите о себе и желательно с фото, всем отвечу, первое время если понравишься можем даже просто повиртить 😜"), reply_markup=otvet)

        elif call.data == "25":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='24')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='26')
            otvet.add(button1, button2, button3)
            file = open('25.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Мария, 30 лет Ищу доминирующего парня, чтобы жестко и грубо смог трахать меня - использовать как вещь. Можно группой парней 😱Обожаю анал 🍆Люблю слюнявые поцелую и пощечины 😏Вирт с перепиской и с голосовыми так же для начала сойдут! 🔥"), reply_markup=otvet)

        elif call.data == "26":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='25')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='27')
            otvet.add(button1, button2, button3)
            file = open('26.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Инна, 27 лет Я очень пошлая и страшно ебливая шлюшка 😏Мне нравится когда меня несколько мужчин пускают по кругу, люблю себя ощущать беспомощной блядью, хоть и в жизни я довольно строгая!  🔥Те кто добавляется в друзья и не пишут - пойдут в бан. Для коллекции в друзья не принимаю.Я не бедная, поэтому ваши копейки меня не интересуют! Место для встреч есть!Хочу получать кайф несколько раз за день, поэтому умение работать языком и руками тебе так же пригодится 😏Люблю энергичных мужчин, возраст не имеет значения 💋"), reply_markup=otvet)

        elif call.data == "27":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='26')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='28')
            otvet.add(button1, button2, button3)
            file = open('27.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Марина, 35 лет Я в разводе! Долгое время была в отношениях sexwife, муж куколд 😂Для серьёзных отношений ищу активного парня. Я не спешу. 😏Люблю доминировать над своим мужчиной. Не терплю грубого отношения к себе, я домина, но в качестве игры могу побыть покорной шлюшкой, но только для альфа самцов с большими членами 🍆💦В деньгах не нуждаюсь, обеспечена, все игрушки и место для встреч имеется!"), reply_markup=otvet)

        elif call.data == "28":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='27')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='29')
            otvet.add(button1, button2, button3)
            file = open('28.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Света, 23 года Скажи-ка, зеркальце, мой свет... Да успокой хозяйке нервы... Я ХОРОША ? - Базара нет ! Змеиный нрав с натурой стервы ! 😏Да мне нравятся секс игрушки да я люблю ласкать красивый член если кому-то что-то не нравится проходите просто мимо) Обожаю когда меня трахают в попку, но это нужно заслужить 👅Для начала я буду в роли главной и оседлаю твоё личико, а дальше оцениваю твои способности и уже обсудим дальнейшее взаимодействие 💦Писать только по делу и кратко, на привет, как дела, не отвечаю!"), reply_markup=otvet)

        elif call.data == "29":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='28')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='30')
            otvet.add(button1, button2, button3)
            file = open('29.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Ира, 21 год Активная, красивая, спортивная фигура и длинные ноги. В кровати НЕ БРЕВНО.С недавнего времени живу без родителей в собственной квартире с котиком, без подруг и теперь могу себе позволить все 😍Ещё немного скромная, но хочу в себе это побороть. Обожаю куни и сосать большие члены 😋🍆Всегда в поиске новых ощущений и нового опыта! Поэтому если ты любишь эксперименты - смело пиши мне 💋"), reply_markup=otvet)

        elif call.data == "30":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='29')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='31')
            otvet.add(button1, button2, button3)
            file = open('30.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Диана, 27 лет Недавно развелась и теперь думаю можно реализовать все мои пошлые фантазии 💦Муж был полным и неуклюжим, до секса ему вообще не было дела 😔 Натерпелась конечно, а так хотелось чтоб меня нормально оттрахали 🔥Обожаю ceкc, в пoпу дaю и глoтаю с большим удовольствием)Всем подряд не даю, для начала пишите пообщаемся, обсудим всё 😜"), reply_markup=otvet)

        elif call.data == "31":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='30')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='32')
            otvet.add(button1, button2, button3)
            file = open('31.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Алиса, 37 лет Кто готов заняться сексом с 37-летней женщиной? 🔥Я абсолютно серьезно. Мне не 20 лет и мое время подходит к концу, секса с мужем никакого нет. В реальной жизни мне трудной найти молодого партнера. Боятся, все воспринимают как шутку. А мне нужно, блин, понимаете? 😱Почему пишу сюда. Я осведомлена, что к так называемым милфам вы относитесь положительно. У меня нормальные сиськи, длинные ноги, вполне норм состояние, но муж очень разленился и никогда не удовлетворял.  Встречаемся в условном месте, делаем дело, разбегаемся. 🍆👅"), reply_markup=otvet)

        elif call.data == "32":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='31')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='33')
            otvet.add(button1, button2, button3)
            file = open('32.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Екатерина, 20 лет. Ищу партнера который может организовать встречи, место и прочее... Если ты маменькин сыночек и стесняшка, то даже не пытайся!У меня знойный темперамент, та  ещё штучка как многие говорят 😏Поэтому, кому мало фоточек, пишите в личку если есть что показать, устроим обмен, могу скину видео с разных встреч где меня трахали 🔥Возбуждает когда на меня дрочат, люблю читать пошлости, прям теку от этого! 💦"), reply_markup=otvet)

        elif call.data == "33":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='32')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='34')
            otvet.add(button1, button2, button3)
            file = open('33.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Лера, 31 год Сексуальная, стройная девушка! Хорошее телосложение и все в меру!Кофе не пью, гулять не люблю. В машине не сижу) Только реальная встреча 😼 Ищу мужчин для секса от 30 лет с волосатой грудью (член 18+) без комплексов.Желательно футфетишистов, люблю когда лижут мои ножки 💦Мужчин для секса строго отбираю. Фото - обычные и интимного характера и такие же видео обязательны."), reply_markup=otvet)

        elif call.data == "34":
            otvet = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton("⬅", callback_data='33')
            button2 = types.InlineKeyboardButton("Написать", url="https://m-loves.ru")
            button3 = types.InlineKeyboardButton("➡", callback_data='34')
            otvet.add(button1, button2, button3)
            file = open('34.jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(file, "Анастасия, 27 лет.Ищу взрослого опытного мужчину, который может оказать материальную помощь за встречи! Молодых тоже люблю 😏 Но от 30 в приоритете  и с хорошим членом! 💦Для желающих чего-то новенького есть подруга с который мы часто вместе развлекаемся, не проч так же будет составить компанию 💋 Писать сразу и по делу, не люблю долгих переписок! "), reply_markup=otvet)









bot.polling()


