from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, filters
import logging


# Вставьте ваш токен здесь
TOKEN = '7367725633:AAGUqv1h1PnEtGT5mYlPOaXUQtRczXfoHBc'

# Установим логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
# Прямая ссылка на изображение с Google Drive
# Прямые ссылки на изображения с Google Drive
google_drive_photo_links = {
    "Person1":
    "https://drive.google.com/uc?id=1gldtaAYaOyNR9tuCetGg_i5ScU8PL0fR",
    "Person2":
    "https://drive.google.com/uc?id=1Au6P3Rtmcscq50ljICoOT0jGHrSOwyYT",
    "Person3":
    "https://drive.google.com/uc?id=15-i5Vm8De61WNA_Hw0WPIQiTcKmeult5",
    "Person4":
    "https://drive.google.com/uc?id=1ZtLpHe9opHOPnwUiGSrMhO5J2MKKf4Eu",
    "Person5":
    "https://drive.google.com/uc?id=18mieZpitDHbPz0tkoD8fmpxXYpMbtsve",
    "Person6":
    "https://drive.google.com/uc?id=1nsDnlMjPNb9szGhhRNpoi9Ttswf2CWNd",
    "Person7":
    "https://drive.google.com/uc?id=1sJ6VOH8SVgEe4SDkcLY0LCkARPDUPcu0"
}

# Информация о людях (замените на реальные данные)
people_info = {
    "Person1": {
        "text":
        "Гергокаев Ахмат Эльдарович\n"
        "20 лет\n"
        "г. Нальчик, Кабардино-Балкарская Республика\n\n"
        "1) С 12 лет работаю у отца на стройке.\n"
        "2) Неофициальная звезда Артека 2022 года.\n"
        "3) За время обучения на 1 курсе, познакомился с 300 новыми людьми.\n\n"
        "Девиз по жизни - «Легкость дается тяжелым трудом»!",
        "photo":
        "https://drive.google.com/uc?id=1gldtaAYaOyNR9tuCetGg_i5ScU8PL0fR"
    },
    "Person2": {
        "text":
        "Реизов Азиз Серанович \n"
        "19 лет\n"
        "с. Бородино Джанкойского р-на респ.Крым\n\n"
        "1) В детстве хотел быть палеонтологом.\n"
        "2) Частичный дальтоник.\n"
        "3) Умею играть на фортепиано..\n\n"
        "«Девиз по жизни - «Если надо, сделаю»!",
        "photo":
        google_drive_photo_links["Person2"]
    },
    "Person3": {
        "text":
        "Береговая Анна Сергеевна\n"
        "19 лет\n"
        "г.Севастополь\n\n"
        "Факт 1: Прыгала с парашютом.\n"
        "Факт 2: Летала на спортивном самолете.\n"
        "Факт 3: Летала на параплане.\n\n"
        "«Нельзя смотреть на мир глазами, затуманенными ненавистью»!",
        "photo":
        google_drive_photo_links["Person3"]
    },
    "Person4": {
        "text":
        "Соколенко Дмитрий Романович\n"
        "19 лет\n"
        "г. Севастополь\n\n"
        "1) Катаюсь на всем, что ездит.\n"
        "2) Прочитал за жизнь более 2000 книг.\n"
        "3) Умею вкусно готовить.\n\n"
        "Девиз по жизни - «Что не убивает, делает нас сильнее!",
        "photo":
        google_drive_photo_links["Person4"]
    },
    "Person5": {
        "text":
        "Кальмук Юлия Васильевна\n"
        "18 лет\n"
        "г. Севастополь\n\n"
        "1) Состояла в сборной Крыма по карате.\n"
        "2) Занимаюсь плаванием с 6 лет.\n"
        "3) Закончила музыкальную школу.\n\n"
        "Девиз по жизни - «С одного шага начинается дорога в тысячу миль»!",
        "photo":
        google_drive_photo_links["Person5"]
    },
    "Person6": {
        "text":
        "Пивнык Руслан Владимирович\n"
        "20 лет\n"
        "С. Мирное, Симферопольский район, Республика Крым\n\n"
        "1) Кандидатом поехал на ВССО 64.\n"
        "2) Кандидат 1.5 года.\n"
        "3) Кандидат с первой целиной в составе ВСССервО «Мрия».\n\n"
        "Девиз по жизни - «Вчерашний день — это история. Завтрашний — загадка. Сегодняшний — подарок»!",
        "photo":
        google_drive_photo_links["Person6"]
    },
    "Person7": {
        "text":
        "Вострецова Юлия Владимировна\n"
        "18 лет\n"
        "пгт. Каланчак, Херсонская область\n\n"
        "1) Не умеет придумывать себе факты.\n"
        "2) Самый перспективный кандидат по производственной части.\n"
        "3) Написала ЕГЭ в сумме по 3 предметам на 275баллов .\n\n"
        "Девиз по жизни - «Выход есть всегда»!",
        "photo":
        google_drive_photo_links["Person7"]
    }
}


# Функция для создания главного меню
def get_main_menu():
    # Создаем кнопки для каждого человека
    keyboard = [
        [InlineKeyboardButton("Сигма", callback_data='Person1')],
        [
            InlineKeyboardButton("Томас Шелби или просто Татарин",
                                 callback_data='Person2')
        ],
        [InlineKeyboardButton("Анна Сергеевна", callback_data='Person3')],
        [InlineKeyboardButton("Экстремал", callback_data='Person4')],
        [InlineKeyboardButton("Люля Кебаб", callback_data='Person5')],
        [InlineKeyboardButton("Владимирович Руслан", callback_data='Person6')],
        [InlineKeyboardButton("ТА Е МАЕ", callback_data='Person7')],
    ]
    return InlineKeyboardMarkup(keyboard)


# Функция для создания стартового меню
def get_start_menu():
    # Создаем кнопку "Start"
    keyboard = [[InlineKeyboardButton("Start", callback_data='start')]]
    return InlineKeyboardMarkup(keyboard)


# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    # Отправляем приветственное сообщение с кнопкой "Start"
    await update.message.reply_text('Привет! Нажмите "Start", чтобы начать.',
                                    reply_markup=get_start_menu())


# Обработчик всех сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    # Отправляем приветственное сообщение с кнопкой "Start" при любом новом сообщении
    await update.message.reply_text('Привет! Нажмите "Start", чтобы начать.',
                                    reply_markup=get_start_menu())


# Обработчик кнопок
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # Проверяем, не устарел ли запрос
    if not query:
        return

    await query.answer()
    person = query.data

    # Если пользователь нажал "Start", отправляем главное меню
    if person == 'start':
        await query.edit_message_text(
            text='Выберите человека, чтобы получить информацию о нем:',
            reply_markup=get_main_menu())
        return

    info = people_info.get(person, {
        "text": "Информация отсутствует.",
        "photo": None
    })

    # Отправляем фотографию, если она есть
    if info['photo']:
        try:
            await context.bot.send_photo(chat_id=query.message.chat_id,
                                         photo=info['photo'])
        except Exception as e:
            logging.error(f"Ошибка при отправке фото: {e}")
            await context.bot.send_message(chat_id=query.message.chat_id,
                                           text="Ошибка при загрузке фото.")

    # Отправляем информацию о человеке
    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text=f"Информация о {person}:\n{info['text']}")

    # Создаем кнопки для возврата в главное меню или выбора другого человека
    keyboard = [[
        InlineKeyboardButton("Назад к списку", callback_data='back_to_menu')
    ],
                [
                    InlineKeyboardButton("Выбрать другого человека",
                                         callback_data='choose_another')
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопками
    await context.bot.send_message(chat_id=query.message.chat_id,
                                   text='Выберите действие:',
                                   reply_markup=reply_markup)


# Обработчик возврата в меню
async def back_to_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    # Отправляем главное меню
    await query.edit_message_text(
        text='Выберите человека, чтобы получить информацию о нем:',
        reply_markup=get_main_menu())


def main() -> None:
    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд и кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(
        CallbackQueryHandler(button, pattern='^Person[1-7]$'))
    application.add_handler(CallbackQueryHandler(button, pattern='^start$'))
    application.add_handler(
        CallbackQueryHandler(back_to_menu, pattern='^back_to_menu$'))
    application.add_handler(
        CallbackQueryHandler(back_to_menu, pattern='^choose_another$'))

    # Запускаем приложение
    application.run_polling()


if __name__ == '__main__':
    main()
