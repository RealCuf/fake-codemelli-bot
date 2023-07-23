from pyrogram import Client, filters
from pyrogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from .generator import round_generator, default_generator


@Client.on_message(filters.command('start'))
async def start_bot(client: Client, message:Message):
    await message.reply_photo('https://i.ibb.co/4ftD0wz/original-515ec38f937144c069daf031244d3449-1.jpg',
                              caption='سلام به ربات تولید کننده کد ملی معتبر خوش اومدید!\n\nاین ربات ابزاری برای تولید کد ملی معتبر و برای کمک به تست برنامه ها، مختص برنامه نویسان تولید شده است.',
                            reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text='تولید کد ملی رند', callback_data='button1'),
                                    InlineKeyboardButton(text='تولید کد ملی', callback_data='button2')
                                ],
                                [
                                    InlineKeyboardButton(text='گیت هاب', url='https://github.com/RealCuf')
                                ]
                            ]
                            ))


@Client.on_callback_query()
async def callback_button(client: Client, callback: CallbackQuery):
    CodeRoundGenerator = round_generator()
    CodeGenerator = default_generator()
    if callback.data == 'button1':
        await callback.message.reply_text(f"✅ →  ||{CodeRoundGenerator}||\n\n@IRCodeMelliBot v1.2")
    elif callback.data == 'button2':
        await callback.message.reply_text(f"✅ →  ||{CodeGenerator}||\n\n@IRCodeMelliBot v1.2")