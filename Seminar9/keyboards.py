from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_level = KeyboardButton('/level😍')
btn_games = KeyboardButton('/new_game🤩')


kb_main_menu.add(btn_level, btn_games)
