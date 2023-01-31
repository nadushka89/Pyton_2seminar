from create import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
import text
import game
import random
from keyboards import kb_main_menu
from datetime import datetime


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}'
                         f'{text.greeting}',
                         reply_markup=kb_main_menu)
    user = []
    user.append(datetime.now())
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str,user))
    with open('text.txt', 'a', encoding='UTF-8') as data:
        data.write(':'.join(user)+'\n')


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    game.new_game()
    if game.check_game():
        toss = random.choice([True, False])
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)


async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, '
                         f' твой ход! Сколько возьмешь конфет?')

@dp.message_handler(commands=['set_total'])
async def set_total_candies(message: Message):
    if not game.check_game():
        max_total=message.text.split()
        if len(max_total)>1 and max_total[1].isdigit():
            game.set_max_total(int(message.text.split()[1]))
            await message.reply(text=f'Максимальное количество изменилось и равно {max_total[1]}')
        else:
            await message.reply(text='Этой командой можно настроить максимальное '
            'количество конфет. Введите /set_total и количество конфет')
    else:
        await message.reply(text='Danger!'
                                'Данную настройку можно изменить после окончания игры')

@dp.message_handler(commands=['level'])
async def set_bot_level(message: Message):
    if not game.check_game():
        game.change_level()
        await message.reply(text=f'Уровень сложности установлен {game.bot_level}')
    else:
        await message.reply(text='Danger!'
                                'Данную настройку можно изменить после окончания игры')

@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= game.get_total():
                game.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял {take} конфет, на столе осталось '
                                     f'{game.get_total()}. Ходит бот ...')
                await bot_turn(message)
            else:
                await message.answer('Возьми поменьше. Возьми от 1 до 28.')
        else:
            pass


async def bot_turn(message):
    total = game.get_total()
    take=0
    if game.get_bot_level()=='light':
        if total <= 28:
            take = total
        else:
            take = random.randint(1, 28)
    else:
        if total <= 28:
            take = total
        else:
            var=(game.get_total()-29)%28
            take = var if var>0 else random.randint(1,28)
    game.take_candies(take)
    await message.answer(f'Бот взял {take} конфет. Осталось {game.get_total()}')
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)


async def check_win(message, take: int, player: str):
    if game.get_total() <= 0:
        if player == 'player':
            await message.answer(f'{message.from_user.first_name} взял {take} и '
                                 f'Одержал победу над Ботом. '
                                 'Введите команду для начала новой игры /new_game')

        else:
            await message.answer(f'{message.from_user.first_name}, к сожалению, ты проиграл!'
                                 f'Бот взял {take} конфет и выиграл. '
                                 ' Введите команду для начала новой игры /new_game')
        game.new_game()
        return True
    else:
        return False




# @dp.message_handler(commands=['candy'])
# async def mes_candy(message: Message):
#     global total
#     count = int(message.text.split()[1])
#     total=count
#     await message.answer(f'Максимальное количество конфет - {total} ')

# @dp.message_handler(commands=['help'])
# async def mes_help(message: Message):
#     await message.answer('За один ход можно забрать не более чем 28 конфет')

# @dp.message_handler(text=['Бла', 'бла', 'bla'])
# async def mes_bla(message: Message):
#     await message.answer('Бла бла бла')

# @dp.message_handler()
# async def mes_all(message: Message):
#     global total
#     if message.text.isdigit():
#         total-=int(message.text)
#         await message.answer(f'{message.from_user.full_name}, на столе осталось  {total} конфет')
#     else:
#         await message.answer(f'{message.from_user.full_name}, ВВЕДИ ЧИСЛО')
