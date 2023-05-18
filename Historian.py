from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, InputMediaPhoto, FSInputFile)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '5904936340:AAFMhQfTFM0fivgfsLaoSoFu4ZJO0JEF4iE'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Привет! Давая я тебе расскажу про достопримечательности или историю Брянска, '
                              'Выбирай кнопку которая тебе интересует',
                         reply_markup=keyboard)


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


@dp.message(Command(commands=['1']))
async def process_1_command(message: Message):
    await message.answer(
        f'Курган Бессмертия\n\nКурган Бессмертия - памятник тем, кто с оружием в руках отстоял наш светлый сегодняшний день. Он был заложен 7 мая 1967 года по инициативе горкома комсомола. В его основание легла земля Сталинграда, Брестской крепости, Одессы, Ленинграда, Севастополя, Безымянной высоты, болгарской Шипки и других легендарных мест. Эту священную землю по горсти принесли матери солдат, ветераны, Герои Советского Союза, полные кавалеры ордена Славы, руководители и участники партизанского движения и подполья, комсомольцы, пионеры, октябрята.')


@dp.message(Command(commands=['2']))
async def process_2_command(message: Message):
    photo = FSInputFile('14.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

    # with open('14.png', 'rb') as f:
    #     # await message.answer_photo(f, caption="caption")
    #     await bot.send_photo(chat_id=message.chat.id, photo=f)
        # await message.answer(
        #     f'Бульвар им.Гагарина\n\nИсторическое название бульвара Гагарина – Рождественская гора. Его связывают с находившимся здесь некогда храмом Рождества Христова. Церковь была расположена на площадке чуть ниже нынешнего торгового центра «Дубрава» и упоминалась ещё в документах начала XVII века. Последнее каменное здание храма, построенное в 1823 году, снесли в годы советской власти. Впервые же Рождественская гора упоминается в апреле 1595 года в документах, составленных двумя московскими воеводами, которые приезжали в Брянск для описи недвижимого имущества Свенского монастыря.'
        #     'Верхняя, более пологая, часть горы официально называлась Смоленской улицей. Этот топоним возник, скорее всего, из-за направления движения улицы в сторону Смоленска.')
        #

@dp.message(Text(text='История'))
async def process_dog_answer(message: Message):
    await message.answer(
        text='Брянск — один из старейшусских городов — был основан в 985 году как славянское укрепленное поселение на правом берегу реки Десны. Первоначальное название города — Дебрянск — связывают с окружающими город «дебрями» — дремучими и труднопроходимыми лесами и оврагами. Название Брянск вошло в употребление лишь с конца XV века, а окончательно утвердилось только к XVIII веку. Большинство памятников старинного Брянска не сохранилось.')


@dp.message(Text(text='Достопримечательности'))
async def process_dog_answer(message: Message):
    await message.answer(text='Привет! Вижу тебя заинтересовали Достопримечетельности, выбирай любую и запоминай!\n '
                              '\n '
                              'Достопримечетельности которые я знаю:\n'
                              '/1 Курган Бессмертия \n'
                              '/2 Бульвар им.Гагарина')


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Достопримечательности')
button_2: KeyboardButton = KeyboardButton(text='История')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],

    resize_keyboard=True)
# ...


if __name__ == '__main__':
    dp.run_polling(bot)
