from loader import dp, bot
from aiogram import types
import time
from random import randint


total = 0



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! Давненько тебя не видел!Сыграем в "Убери конфеты"? '
                         f'Если согласен введи "/DA и количество конфет на столе"')

@dp.message_handler(commands=['DA'])
async def mes_start2(message: types.Message):
    global total
    count = message.text.split()[1]
    total = int(count)
    await message.answer(f'Установили количество конфет в размере: {total}')
    time.sleep(2)
    await message.answer('Отлично!!! Правила игры: \n1. Количество конфет на столе изначально не может быть меньше 29. \n2. За раз нельзя выбрать более 28 конфет.'
                         '\n3. Кто ходит первый: ты или я, опеределяется случайной жеребьевкой. '
                         '\n4. Побеждает тот, кто сделал последий ход.'
                         '\nУдачи! :)')
    time.sleep(2)
    await message.answer(f'Надеюсь ты ознакомился с правилами:) А теперь да начнется битва!!!')
    time.sleep(2)
    first_player = 1
    second_player = 2
    draw = randint(1, 2)
    if draw == first_player:
        await message.answer(f'По результатам жеребьевки. Первым ходишь Ты:) Выбери количество конфет которое хочешь убрать со стола?')
    if draw == second_player:
        await message.answer(f'По результатам жеребьевки. Первым хожу я:)')
        time.sleep(1)
        second_player_ch = randint(1, 28)
        if total <= 28:
            second_player_ch = total
        if total <= 57 and total >= 30:
            second_player_ch = total - 29
        await message.answer(f'Я выбираю убрать со стола {second_player_ch} конфет')
        total -= second_player_ch
        await message.answer(f'Конфет на столе осталось - {total}')


@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit() and int(message.text) >= 1 and int(message.text) < 29 and int(message.text) <= total:
        first_player_ch = int(message.text)
        total -= first_player_ch
        await bot.send_message(message.from_user.id, f'Конфет на столе осталось - {total}')
        if total == 0:
            await bot.send_message(message.from_user.id, f'Вы победитель!!!')
            updater.stop()
        time.sleep(1)
        second_player_ch = randint(1, 28)
        if total <= 28:
            second_player_ch = total
        if total <= 57 and total >= 30:
            second_player_ch = total - 29
        await message.answer(f'Я выбираю убрать со стола {second_player_ch} конфет')
        total -= second_player_ch
        await message.answer(f'Конфет на столе осталось - {total}')
        if total == 0:
            await bot.send_message(message.from_user.id, f'Я победил!!!')
            updater.stop()
    else:
        await bot.send_message(message.from_user.id, 'Пожалуйста введите правильное значение')





    
    # if int(message.text) > 29:   #message.text.isdigit(): # and
    #     total = int(message.text)
    #     await bot.send_message(message.from_user.id, f'Количество конфет на столе: {total}')
    # else:
    #     await bot.send_message(message.from_user.id, 'Пожалуйста введи правильную цифру')

# @dp.message_handler(commands=['OOP'])
# async def mes_OOP(message: types.Message):
#     await message.answer('Да что вы говорите!')


# @dp.message_handler(text=['лох'])
# async def mes_loh(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message_id)
#     await message.answer('Так говорить нельзя!')
#
#
# @dp.message_handler()
# async def mes_all(message: types.Message):
#     global total
#     if message.text.isdigit():
#         total -= int(message.text)
#         await bot.send_message(message.from_user.id, f'Конфет на столе осталось - {total}')
#     else:
#         await bot.send_message(message.from_user.id, f'Введи ка ты число майн фройнд')
#     # await message.answer(f'Гляди, что поймал - {message.text}')


