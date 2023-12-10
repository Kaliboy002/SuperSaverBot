import logging
from os import getenv, path

import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand
from dotenv import load_dotenv

from data.api import UniversalAPI
from data.crud import user_create, user_statistic, user, get_channels, delete_channel, create_channel, check_channels
from db.connection import create_db
from keyboards.buttons import admin_btn, exit_btn, channels_btn, forced_channel
from states.state import ReklamaState, AddChannelState, DeleteChannelState

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
    await bot.set_my_commands([BotCommand(command='start', description="Ishga Tushirish ♻"), BotCommand(command='help', description="Yordam olish 🛠"), BotCommand(command='info', description="Sizning ma'lumotlaringiz 🗂")])
    await bot.send_message(chat_id=msg.chat.id,
                           text=f"Assalomu alaykum {msg.from_user.full_name} 🤖\n"
                                f"Bu bot orqali siz ✅\n\n"
                                f"— Instagramdan Reels va Post yuklash 🗳\n"
                                f"— TikTokdan Video yuklash 📥\n"
                                f"— Likeedan Video yuklash 📂\n"
                                f"— Pinterestdan Video va Rasm yuklash 🖇\n"
                                f"— User ma'lumotlarini ko'rish 👤\n\n"
                                f"Boshlash uchun bizga xabarning URL manzilini yuboring 🔗\n\n"
                                f"🗣 𝐁𝐨𝐭 𝐨𝐫𝐪𝐚𝐥𝐢 𝐭𝐚𝐥𝐚𝐛 𝐯𝐚 𝐭𝐚𝐤𝐥𝐢𝐟𝐥𝐚𝐫 𝐮𝐜𝐡𝐮𝐧: @Rozievich")


@dp.message_handler(commands=['help'])
async def help_handler(msg: types.Message):
    await bot.send_message(chat_id=msg.chat.id, text="Sizning ma'lumotlaringiz /info bunda sizga Telegram ID, Username, Ism, Familiya taqdim etamiz ✍️\n\nMavjud Url manzil kiritishingizni so'raymiz ✅\n\nBotda muammolar kuzatilsa Adminga murojat qiling! 👨🏻‍💻\n\nBiz muammolarni tez orada bartaraf etamiz! ⏳")  # noqa


@dp.message_handler(commands=['info'])
async def info_handler(msg: types.Message):
    await bot.send_message(chat_id=msg.chat.id, text=f"𝐒𝐢𝐳𝐧𝐢𝐧𝐠 𝐌𝐚'𝐥𝐮𝐦𝐨𝐭𝐥𝐚𝐫𝐢𝐧𝐠𝐢𝐳 🗂\nɪᴅ: {msg.from_user.id}\nɪsᴍ: {msg.from_user.first_name}\nᴜsᴇʀɴᴀᴍᴇ: {'@' + msg.from_user.username if msg.from_user.username else '❌'}\n\n@Super_saverBot - 𝙱𝚒𝚣 𝚋𝚒𝚕𝚊𝚗 𝚑𝚊𝚖𝚖𝚊𝚜𝚒 𝚘𝚜𝚘𝚗 📥")


@dp.message_handler(commands=['panel'])
async def admin_panel(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await bot.send_message(chat_id=msg.chat.id, text=f"𝐀𝐬𝐬𝐚𝐥𝐨𝐦𝐮 𝐚𝐥𝐚𝐲𝐤𝐮𝐦 {msg.from_user.full_name} 🤖\n𝙰𝚍𝚖𝚒𝚗 𝚜𝚊𝚑𝚒𝚏𝚊𝚐𝚊 𝚡𝚞𝚜𝚑 𝚔𝚎𝚕𝚒𝚋𝚜𝚒𝚣 🖇👤", reply_markup=admin_btn())


@dp.message_handler(Text("Statistics 📊"))
async def user_statistic_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        data = user_statistic()
        await bot.send_message(chat_id=msg.chat.id, text=data)
    else:
        await bot.send_message(chat_id=msg.chat.id, text="𝗦𝗶𝘇 𝗮𝗱𝗺𝗶𝗻 𝗲𝗺𝗮𝘀𝘀𝗶𝘇 👨🏻‍💻❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text("Reklama 🗣"))
async def reklama_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await ReklamaState.rek.set()
        await bot.send_message(chat_id=msg.chat.id, text="𝐑𝐞𝐤𝐥𝐚𝐦𝐚 𝐓𝐚𝐫𝐪𝐚𝐭𝐢𝐬𝐡 𝐛𝐨'𝐥𝐢𝐦𝐢 🤖", reply_markup=exit_btn())
    else:
        await bot.send_message(chat_id=msg.chat.id, text="𝗦𝗶𝘇 𝗮𝗱𝗺𝗶𝗻 𝗲𝗺𝗮𝘀𝘀𝗶𝘇 👨🏻‍💻❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=ReklamaState.rek, content_types=types.ContentType.ANY)
async def rek_state(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await bot.send_message(chat_id=msg.chat.id, text="𝐑𝐞𝐤𝐥𝐚𝐦𝐚 𝐲𝐮𝐛𝐨𝐫𝐢𝐬𝐡 𝐛𝐞𝐤𝐨𝐫 𝐪𝐢𝐥𝐢𝐧𝐝𝐢 🤖❌", reply_markup=admin_btn())
        await state.finish()
    else:
        await state.finish()
        await bot.send_message(chat_id=msg.chat.id, text="𝐑𝐞𝐤𝐥𝐚𝐦𝐚 𝐲𝐮𝐛𝐨𝐫𝐢𝐬𝐡 𝐛𝐨𝐬𝐡𝐚𝐧𝐝𝐢 🤖✅", reply_markup=admin_btn())
        summa = 0
        for i in user.get_users():
            if int(i[1]) != int(getenv("ADMIN")):
                try:
                    await msg.copy_to(int(i[1]), caption=msg.caption, caption_entities=msg.caption_entities, reply_markup=msg.reply_markup)
                except:  # noqa
                    summa += 1
        await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
        await bot.send_message(int(getenv("ADMIN")), text=f"𝐁𝐨𝐭𝐧𝐢 𝐁𝐥𝐨𝐤𝐥𝐚𝐠𝐚𝐧 𝐮𝐬𝐞𝐫𝐥𝐚𝐫 𝐬𝐨𝐧𝐢: {summa}")


@dp.message_handler(Text("Channels 🖇"))
async def channels_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await msg.answer(text=get_channels(), reply_markup=channels_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text("Kanal qo'shish ⚙️"))
async def add_channel_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await AddChannelState.username.set()
        await msg.answer(text="Qo'shish kerak bo'lgan kanal Usernameni kiriting ✍️", reply_markup=exit_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=AddChannelState.username)
async def add_channel_handler_func(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer("Kanal qo'shish bekor qilindi ❌", reply_markup=channels_btn())
        await state.finish()
    else:
        data = create_channel(msg.text)
        if data:
            await msg.answer("Kanal muvaffaqiyatli qo'shildi ✅", reply_markup=channels_btn())
            await state.finish()
        else:
            await msg.answer("Bu kanal oldin qo'shilgan ❌", reply_markup=channels_btn())
            await state.finish()


@dp.message_handler(Text("Kanal o'chirish 🗑"))
async def movie_delete_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await DeleteChannelState.username.set()
        await msg.answer(text="O'chirish kerak bo'lgan kanal Usernameni kiriting ✍️", reply_markup=exit_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text("❌"))
async def exit_handler(msg: types.Message):
    if msg.from_user.id == int(getenv("ADMIN")):
        await msg.answer("Bosh menu 🔮", reply_markup=admin_btn())
        
        
@dp.callback_query_handler(lambda x: x.data == "channel_check")
async def channel_check_handler(callback: types.CallbackQuery):
    check = check_channels(callback.from_user.id)
    if check:
        await callback.message.delete()
        await callback.answer("Obuna uchun rahmat 🤖")
    else:
        await callback.message.answer("Iltimos quidagi kanallarga obuna bo'ling", reply_markup=forced_channel())


@dp.message_handler(state=DeleteChannelState.username)
async def delete_channel_handler_func(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer("Kanal o'chirish bekor qilindi ❌", reply_markup=channels_btn())
        await state.finish()
    else:
        data = delete_channel(msg.text)
        if data:
            await msg.answer("Kanal muvaffaqiyatli o'chirildi ✅", reply_markup=channels_btn())
        else:
            await msg.answer("Bunday usernameli kanal mavjud emas ❌", reply_markup=channels_btn())
        await state.finish()


@dp.message_handler()
async def result_handler(msg: types.Message):
    check = check_channels(msg.from_user.id)
    if check:
        await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
        msg_sticer = await bot.send_message(chat_id=msg.chat.id, text="⏳")
        data = api.get_media(msg.text)
        if data and data['type'] == 'insta' and not data.get('post', False):
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
            try:
                await bot.send_video(chat_id=msg.chat.id, video=data['data'], caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                await msg_sticer.delete()
            except:
                await bot.send_video(chat_id=msg.chat.id, video=requests.get(data['data']).content, caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                await msg_sticer.delete()
        elif data and data['type'] == 'insta' and data.get('post', False):
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
            try:
                await bot.send_media_group(chat_id=msg.chat.id, media=data['data'])
                await msg_sticer.delete()
            except:
                await bot.send_media_group(chat_id=msg.chat.id, media=requests.get(data['data']).content)
                await msg_sticer.delete()
        elif data and data['type'] == 'likee':
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
            await bot.send_video(chat_id=msg.chat.id, video=requests.get(url=data['data']).content, caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
            await msg_sticer.delete()
        elif data and data['type'] == 'tiktok':
            await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
            await bot.send_video(chat_id=msg.chat.id, video=requests.get(url=data['data']).content, caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
            await msg_sticer.delete()
        elif data and data['type'] == 'pin':
            if data['post'] == 'gif':
                await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_PHOTO)
                try:
                    await bot.send_animation(chat_id=msg.chat.id, animation=data['data'], caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                    await msg_sticer.delete()
                except:
                    await bot.send_animation(chat_id=msg.chat.id, animation=requests.get(url=data['data']).content, caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                    await msg_sticer.delete()
            elif data['post'] == 'image':
                await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_PHOTO)
                try:
                    await bot.send_photo(chat_id=msg.chat.id, photo=data['data'], caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                    await msg_sticer.delete()
                except:
                    await bot.send_photo(chat_id=msg.chat.id, photo=requests.get(data['data']).content, caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                    await msg_sticer.delete()
            elif data['post'] == 'video':
                await bot.send_chat_action(msg.chat.id, types.ChatActions.UPLOAD_VIDEO)
                try:
                    await bot.send_video(chat_id=msg.chat.id, video=data['data'], caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                    await msg_sticer.delete()
                except:
                    await bot.send_video(chat_id=msg.chat.id, video=requests.get(data['data']).content, caption=f"@super_saverbot - 𝐎𝐫𝐪𝐚𝐥𝐢 𝐲𝐮𝐤𝐥𝐚𝐛 𝐨𝐥𝐢𝐧𝐝𝐢 📥")
                    await msg_sticer.delete()
        else:
            await bot.send_chat_action(msg.chat.id, types.ChatActions.TYPING)
            await bot.send_message(chat_id=msg.chat.id, text="𝐁𝐮𝐧𝐝𝐚𝐲 𝐔𝐑𝐋 𝐦𝐚𝐧𝐳𝐢𝐥 𝐦𝐚𝐯𝐣𝐮𝐝 𝐞𝐦𝐚𝐬 𝐢𝐥𝐭𝐢𝐦𝐨𝐬 𝐭𝐞𝐤𝐬𝐡𝐢𝐫𝐢𝐛 𝐪𝐚𝐲𝐭𝐚𝐝𝐚𝐧 𝐲𝐮𝐛𝐨𝐫𝐢𝐧𝐠 🔎📂❌")
            await msg_sticer.delete()
    else:
        await msg.answer("Iltimos quidagi kanallarga obuna bo'ling", reply_markup=forced_channel())


async def startup(dp):
    create_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup, skip_updates=True)
