from pyrogram import Client, filters
from pyrogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from .generator import round_generator, default_generator


BOT_USERNAME = 'mybotusername'


@Client.on_message(filters.command('start'))
async def start_handler(client: Client, message:Message):
    await message.reply_photo(
        'https://i.ibb.co/4ftD0wz/original-515ec38f937144c069daf031244d3449-1.jpg', #bot start text picture
        caption='سلام به ربات تولید کننده کد ملی معتبر خوش اومدید!\n\nاین ربات ابزاری برای تولید کد ملی معتبر و برای کمک به تست برنامه ها، مختص برنامه نویسان تولید شده است.',
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text='تولید کد ملی رند', #the text of the first button
                                     callback_data='button_1'),
                InlineKeyboardButton(text='تولید کد ملی', #the text of the second button
                                     callback_data='button_2')
            ],
            [
                InlineKeyboardButton(text='گیت هاب',
                                     url='https://github.com/RealCuf')
            ]
        ]
        ))


@Client.on_callback_query()
async def callback_button(client: Client, callback: CallbackQuery):
    coderoundgenerator = round_generator()
    codegenerator = default_generator()
    if callback.data == 'button_1':
        await callback.message.reply_text(
            f"✅ →  ||{coderoundgenerator}||\n\n@{BOT_USERNAME} v1.2")

    elif callback.data == 'button_2':
        await callback.message.reply_text(
            f"✅ →  ||{codegenerator}||\n\n@{BOT_USERNAME} v1.2")