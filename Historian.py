from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '5904936340:AAFMhQfTFM0fivgfsLaoSoFu4ZJO0JEF4iE'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Привет! Давая я тебе расскажу про достопримечательности или историю Брянска'
                              'Выбирай кнопку которая тебе интересует',
                         reply_markup=keyboard)

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')

@dp.message(Text(text='История'))
async def process_dog_answer(message: Message):
        await message.answer(text='Брянск — один из старейших русских городов — был основан в 985 году как славянское укрепленное поселение на правом берегу реки Десны. Первоначальное название города — Дебрянск — связывают с окружающими город «дебрями» — дремучими и труднопроходимыми лесами и оврагами. Название Брянск вошло в употребление лишь с конца XV века, а окончательно утвердилось только к XVIII веку. Большинство памятников старинного Брянска не сохранилось.')



# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Достопримечательности')
button_2: KeyboardButton = KeyboardButton(text='История')



# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_1, button_2]],

    resize_keyboard=True)
# ...

# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(Text(text='Собак 🦮'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?')


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(Text(text='Огурцов 🥒'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки боятся больше')







if __name__ == '__main__':
    dp.run_polling(bot)