import logging
from os import getenv, path

import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand
from dotenv import load_dotenv

from data.api import UniversalAPI
from data.crud import user_create, user_statistic, all_users
from db.connection import create_db
from keyboards.admin_keyboards import admin_btn, exit_btn
from states.state import ReklamaState

api = UniversalAPI()
load_dotenv()
logging.basicConfig(level=logging.INFO)
BASE = path.dirname(path.abspath(__file__))

TOKEN = getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    user_create(msg)
    await bot.set_my_commands([BotCommand(command='start', description="Ishga Tushirish ♻"),
                               BotCommand(command='help', description="Yordam olish 🛠"),
                               BotCommand(command='info', description="Sizning ma'lumotlaringiz 🗂")])
    await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
    await msg.answer(text=f"𝐀𝐬𝐬𝐚𝐥𝐨𝐦𝐮 𝐚𝐥𝐚𝐲𝐤𝐮𝐦 {msg.from_user.full_name} 🤖\n𝘉𝘶 𝘣𝘰𝘵 𝘰𝘳𝘲𝘢𝘭𝘪 𝘴𝘪𝘻 ✅\n"
                          f"— 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖𝚍𝚊𝚗 𝚁𝚎𝚎𝚕𝚜 𝚟𝚊 𝙿𝚘𝚜𝚝 𝚢𝚞𝚔𝚕𝚊𝚜𝚑 🗳\n"
                          f"— 𝚃𝚒𝚔𝚃𝚘𝚔𝚍𝚊𝚗 𝚅𝚒𝚍𝚎𝚘 𝚢𝚞𝚔𝚕𝚊𝚜𝚑 📥\n— 𝙻𝚒𝚔𝚎𝚎𝚍𝚊𝚗 𝚅𝚒𝚍𝚎𝚘 𝚢𝚞𝚔𝚕𝚊𝚜𝚑 📂\n"
                          f"— 𝙿𝚒𝚗𝚝𝚎𝚛𝚎𝚜𝚝𝚍𝚊𝚗 𝚅𝚒𝚍𝚎𝚘 𝚟𝚊 𝚁𝚊𝚜𝚖 𝚢𝚞𝚔𝚕𝚊𝚜𝚑 🖇\n— 𝚄𝚜𝚎𝚛 𝚖𝚊'𝚕𝚞𝚖𝚘𝚝𝚕𝚊𝚛𝚒𝚗𝚐𝚒𝚣𝚗𝚒 𝚔𝚘'𝚛𝚒𝚜𝚑 👤\n\n"
                          f"Boshlash uchun bizga xabarning URL manzilini yuboring 🔗\n\n"
                          f"🗣 𝐁𝐨𝐭 𝐨𝐫𝐪𝐚𝐥𝐢 𝐭𝐚𝐥𝐚𝐛 𝐯𝐚 𝐭𝐚𝐤𝐥𝐢𝐟𝐥𝐚𝐫 𝐮𝐜𝐡𝐮𝐧: @Rozievich")


@dp.message_handler(commands=['help'])
async def help_handler(msg: types.Message):
    await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
    await msg.answer(
        text="Sizning ma'lumotlaringiz /info bunda sizga Telegram ID, Username, Ism, Familiya taqdim etamiz ✍️\n\nMavjud Url manzil kiritishingizni so'raymiz ✅\n\nBotda muammolar kuzatilsa Adminga murojat qiling! 👨🏻‍💻\n\nBiz muammolarni tez orada bartaraf etamiz! ⏳")  # noqa


@dp.message_handler(commands=['info'])
async def info_handler(msg: types.Message):
    await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
    await msg.answer(
        text=f"𝐒𝐢𝐳𝐧𝐢𝐧𝐠 𝐌𝐚'𝐥𝐮𝐦𝐨𝐭𝐥𝐚𝐫𝐢𝐧𝐠𝐢𝐳 🗂\nɪᴅ: {msg.from_user.id}\nɪsᴍ: {msg.from_user.first_name}\nᴜsᴇʀɴᴀᴍᴇ: {'@' + msg.from_user.username if msg.from_user.username else '❌'}\n\n@Super_saverBot - 𝙱𝚒𝚣 𝚋𝚒𝚕𝚊𝚗 𝚑𝚊𝚖𝚖𝚊𝚜𝚒 𝚘𝚜𝚘𝚗 📥")


@dp.message_handler(commands=['panel'])
async def admin_panel(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await msg.answer(
            text=f"𝐀𝐬𝐬𝐚𝐥𝐨𝐦𝐮 𝐚𝐥𝐚𝐲𝐤𝐮𝐦 {msg.from_user.full_name} 🤖\n𝙰𝚍𝚖𝚒𝚗 𝚜𝚊𝚑𝚒𝚏𝚊𝚐𝚊 𝚡𝚞𝚜𝚑 𝚔𝚎𝚕𝚒𝚋𝚜𝚒𝚣 🖇👤",
            reply_markup=admin_btn())


@dp.message_handler(Text("📊 Statistics"))
async def user_statistic_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        data = user_statistic()
        await msg.answer(text=data)


@dp.message_handler(Text("🗣 Reklama"))
async def reklama_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await ReklamaState.rek.set()
        await msg.answer(text="Reklama Tarqatish bo'limi 🤖", reply_markup=exit_btn())


@dp.message_handler(state=ReklamaState.rek, content_types=types.ContentType.ANY)
async def rek_state(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer(text="Reklama yuborish bekor qilindi!", reply_markup=admin_btn())
        await state.finish()
    else:
        await msg.answer(text="Reklama jo'natish boshlandi!")
        users = all_users()
        summa = 0
        for i in users:
            if int(i[1]) != int(getenv("ADMIN")):
                try:
                    await msg.copy_to(int(i[1]), caption=msg.caption, caption_entities=msg.caption_entities,
                                      reply_markup=msg.reply_markup)
                except:  # noqa
                    summa += 1
        await bot.send_message(int(getenv("ADMIN")), text=f"Botni Bloklagan userlar soni: {summa}")
        await state.finish()


@dp.message_handler(Text("📈 Media Statistics"))
async def media_statistic_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        data = user_statistic()
        await msg.answer(text=data)


@dp.message_handler(Text("👤 Find User"))
async def find_user_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        data = user_statistic()
        await msg.answer(text=data)


@dp.message_handler()
async def result_handler(msg: types.Message):
    await bot.send_chat_action(msg.chat.id, types.ChatActions.CHOOSE_STICKER)
    await msg.answer_sticker(sticker=open(BASE + '/data/sticer.tgs', 'rb'))
    data = api.get_media(msg.text)
    await bot.delete_message(msg.from_user.id, msg.message_id + 1)
    if data and data['type'] == 'insta' and not data.get('post', False):
        await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
        await msg.answer_video(video=data['data'], caption=f"@Super_SaverBot - Orqali yuklab olindi!")
    elif data and data['type'] == 'insta' and data.get('post', False):
        await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
        await msg.answer_media_group(media=data['data'])
    elif data and data['type'] == 'likee':
        await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
        await msg.answer_video(video=requests.get(url=data['data']).content,
                               caption=f"@Super_SaverBot - Orqali yuklab olindi!")
    elif data and data['type'] == 'tiktok':
        await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
        await msg.answer_video(video=requests.get(url=data['data']).content,
                               caption=f"@Super_SaverBot - Orqali yuklab olindi!")
    elif data and data['type'] == 'pin':
        if data['post'] == 'gif':
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_PHOTO)
            await msg.answer_animation(animation=data['data'], caption=f"@Super_SaverBot - Orqali yuklab olindi!")
        elif data['post'] == 'image':
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_PHOTO)
            await msg.answer_photo(photo=data['data'], caption=f"@Super_SaverBot - Orqali yuklab olindi!")
        elif data['post'] == 'video':
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
            await msg.answer_video(video=data['data'], caption=f"@Super_SaverBot - Orqali yuklab olindi!")
    else:
        await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
        await msg.answer(text="Invalid Url ❌")


async def startup(dp):
    create_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup, skip_updates=True)
