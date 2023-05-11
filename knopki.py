import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6277154966:AAGvDhJnNRQZ3KUlgy1luuk1cTqqD7fop2Y'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Количество попыток, доступных пользователю в игре
ATTEMPTS: int = 5

# Словарь, в котором будут храниться данные пользователя
users: dict = {}

@dp.message(Command(commands=['играть']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')

@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                           'Играть', 'Хочу играть'], ignore_case=True))
async def process_positive_answer(message: Message):
        print(users)
        if not users[message.from_user.id]['in_game']:
            await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                                 'попробуй угадать!')
            users[message.from_user.id]['in_game'] = True
            users[message.from_user.id]['secret_number'] = get_random_number()
            users[message.from_user.id]['attempts'] = ATTEMPTS
        else:
            await message.answer('Пока мы играем в игру я могу '
                                 'реагировать только на числа от 1 до 100 '
                                 'и команды /cancel и /stat')

    # Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def process_negative_answer(message: Message):
        if not users[message.from_user.id]['in_game']:
            await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                                 'напишите об этом')
        else:
            await message.answer('Мы же сейчас с вами играем. Присылайте, '
                                 'пожалуйста, числа от 1 до 100')

    # Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
        if users[message.from_user.id]['in_game']:
            if int(message.text) == users[message.from_user.id]['secret_number']:
                await message.answer('Ура!!! Вы угадали число!\n\n'
                                     'Может, сыграем еще?')
                users[message.from_user.id]['in_game'] = False
                users[message.from_user.id]['total_games'] += 1
                users[message.from_user.id]['wins'] += 1
            elif int(message.text) > users[message.from_user.id]['secret_number']:
                await message.answer('Мое число меньше')
                users[message.from_user.id]['attempts'] -= 1
            elif int(message.text) < users[message.from_user.id]['secret_number']:
                await message.answer('Мое число больше')
                users[message.from_user.id]['attempts'] -= 1

            if users[message.from_user.id]['attempts'] == 0:
                await message.answer(
                    f'К сожалению, у вас больше не осталось '
                    f'попыток. Вы проиграли :(\n\nМое число '
                    f'было {users[message.from_user.id]["secret_number"]}'
                    f'\n\nДавайте сыграем еще?')
                users[message.from_user.id]['in_game'] = False
                users[message.from_user.id]['total_games'] += 1
        else:
            await message.answer('Мы еще не играем. Хотите сыграть?')

    # Этот хэндлер будет срабатывать на остальные текстовые сообщения
@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


    # Если пользователь только запустил бота и его нет в словаре '
    # 'users - добавляем его в словарь
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}

@dp.message(Command(commands=['joke']))
async def process_Joke_command(message: Message):
        await message.answer('Привет!\nДавай я тебе расскажу шутку"?\n\n'
                            'Чтобы увидить шутку напиши команду /make fun of me')


@dp.message(Command(commands=['make']))
async def process_Joke_command(message: Message):
    await message.answer('я тебе ничего не скажу так как я не знаю шуток \n\n')




# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(
                    f'Всего игр сыграно: '
                    f'{users[message.from_user.id]["total_games"]}\n'
                    f'Игр выиграно: {users[message.from_user.id]["wins"]}')


# Этот хэндлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        users[message.from_user.id]['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Плохо')
button_2: KeyboardButton = KeyboardButton(text='Хорошо')
button_3: KeyboardButton = KeyboardButton(text='666666')
button_4: KeyboardButton = KeyboardButton(text='проверка')
button_5: KeyboardButton = KeyboardButton(text='Как так')
button_6: KeyboardButton = KeyboardButton(text='Пупа')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_1, button_2, button_3],
                                  [button_4, button_5, button_6]],
    resize_keyboard=True)



# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Как у тебя дела?',
                         reply_markup=keyboard)


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(Text(text='Плохо'))
async def process_dog_answer(message: Message):
    await message.answer(text='O ну не грусти.\nДавай я тебе расскажу шутку".\n\n'
                            'Лупа и Пупа пошли получать зарплату. В бухгалтерии все перепутали. В итоге, Лупа получил за Пупу, а Пупа за Лупу')
@dp.message(Text(text='666666'))
async def process_dog_answer(message: Message):
        await message.answer(text='ТЫ ЧЕЕЕЕЕЕ СУМMА СОШEЛ ТАКИЕ ЦИФРЫ НЕЛЬЗЯ ПИСАТЬ СМЕРТНОМУ!!!!! onfgjfgfojfo')

# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(Text(text='Хорошо'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='О тогда зайди на степик и попробуй решить задачку с шахматами,'
                              'тогда твое настроение быстро изменится.')

if __name__ == '__main__':
    dp.run_polling(bot)