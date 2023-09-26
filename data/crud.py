from models.model import User, InstaLikeeTik, Pin

user = User('users')
insta = InstaLikeeTik('instagram')
tiktok = InstaLikeeTik('tiktok')
likee = InstaLikeeTik('likee')
pin = Pin('pinterest')


def user_create(msg):
    try:
        telegram_id = msg.from_user.id
        username = msg.from_user.username
        first_name = msg.from_user.first_name
        if user.get_user(telegram_id):
            return user
        else:
            return user.create_user(telegram_id=telegram_id, username=username, first_name=first_name)
    except:
        return None


def all_users():
    try:
        data = user.get_medias()
        return data
    except:
        return None


def user_statistic():
    data = user.statistika()
    return (f"𝐀𝐝𝐦𝐢𝐧 𝐮𝐜𝐡𝐮𝐧 𝐮𝐬𝐞𝐫𝐥𝐚𝐫 𝐒𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐤𝐚𝐬𝐢 🤖📂\n\n"
            f"ʙᴜ ᴏʏᴅᴀ ᴊᴀᴍɪ ǫᴏ'sʜɪʟɢᴀɴ ᴜsᴇʀʟᴀʀ sᴏɴɪ: {len(data['month'])}\n"
            f"ʙᴜ ʜᴀꜰᴛᴀ ᴊᴀᴍɪ ǫᴏ'sʜɪʟɢᴀɴ ᴜsᴇʀʟᴀʀ sᴏɴɪ: {len(data['week'])}\n"
            f"ʙᴜɢᴜɴ ᴊᴀᴍɪ ǫᴏ'sʜɪʟɢᴀɴ ᴜsᴇʀʟᴀʀ sᴏɴɪ: {len(data['day'])}\n\n"
            f"ʀᴏ'ʏʜᴀᴛɢᴀ ᴏʟɪɴɢᴀɴ ʙᴀʀᴄʜᴀ ᴜsᴇʀʟᴀʀ sᴏɴɪ: {len(all_users())}\n\n"
            f"𝗨𝘀𝗲𝗿𝗹𝗮𝗿𝗻𝗶 𝗾𝗶𝗱𝗶𝗿𝗶𝘀𝗵 𝘂𝗰𝗵𝘂𝗻 👤 Find User 𝗙𝘂𝗻𝗸𝘀𝗶𝘆𝗮𝘀𝗶𝗱𝗮𝗻 𝗳𝗼𝘆𝗱𝗮𝗹𝗮𝗻𝗶𝗻𝗴 🔎")


def media_statistic():
    insta_stat = insta.statistika()
    tiktok_stat = tiktok.statistika()
    likee_stat = likee.statistika()
    pin_stat = pin.statistika()

    return (f"𝐀𝐝𝐦𝐢𝐧 𝐮𝐜𝐡𝐮𝐧 𝐦𝐞𝐝𝐢𝐚𝐥𝐚𝐫 𝐒𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐤𝐚𝐬𝐢 🤖📂\n\n"
            f"𝗕𝘂 𝗼𝘆𝗱𝗮 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(insta_stat['month'])}\n"
            f"𝗕𝘂 𝗵𝗮𝗳𝘁𝗮 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(insta_stat['week'])}\n"
            f"𝗕𝘂𝗴𝘂𝗻 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(insta_stat['day'])}\n"
            f"𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝗷𝗮𝗺𝗶 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(insta.get_medias())}\n\n"
            f"𝗕𝘂 𝗼𝘆𝗱𝗮 𝗧𝗶𝗸𝗧𝗼𝗸 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(tiktok_stat['month'])}\n"
            f"𝗕𝘂 𝗵𝗮𝗳𝘁𝗮 𝗧𝗶𝗸𝗧𝗼𝗸 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(tiktok_stat['week'])}\n"
            f"𝗕𝘂𝗴𝘂𝗻 𝗧𝗶𝗸𝗧𝗼𝗸 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(tiktok_stat['day'])}\n"
            f"𝗧𝗶𝗸𝗧𝗼𝗸 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝗷𝗮𝗺𝗶 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(tiktok.get_medias())}\n\n"
            f"𝗕𝘂 𝗼𝘆𝗱𝗮 𝗟𝗶𝗸𝗲𝗲 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(likee_stat['month'])}\n"
            f"𝗕𝘂 𝗵𝗮𝗳𝘁𝗮 𝗟𝗶𝗸𝗲𝗲 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(likee_stat['week'])}\n"
            f"𝗕𝘂𝗴𝘂𝗻 𝗟𝗶𝗸𝗲𝗲 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(likee_stat['day'])}\n"
            f"𝗟𝗶𝗸𝗲𝗲 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝗷𝗮𝗺𝗶 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(likee.get_medias())}\n\n"
            f"𝗕𝘂 𝗼𝘆𝗱𝗮 𝗣𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(pin_stat['month'])}\n"
            f"𝗕𝘂 𝗵𝗮𝗳𝘁𝗮 𝗣𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(pin_stat['week'])}\n"
            f"𝗕𝘂𝗴𝘂𝗻 𝗣𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(pin_stat['day'])}\n"
            f"𝗣𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝘁𝗮𝗿𝗺𝗼𝗴'𝗶𝗱𝗮𝗻 𝗷𝗮𝗺𝗶 𝘆𝘂𝗸𝗹𝗮𝗯 𝗼𝗹𝗶𝗻𝗴𝗮𝗻 𝗺𝗲𝗱𝗶𝗮𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(pin.get_medias())}\n\n")


def find_user(msg):
    if msg.isdigit():
        user_data = user.get_user(msg)
        if user_data:
            return (f"𝐔𝐬𝐞𝐫 𝐦𝐚'𝐥𝐮𝐦𝐨𝐭𝐥𝐚𝐫𝐢: 🗂\n\n"
                    f"ɪᴅ: {user_data['telegram_id']}\n"
                    f"ɪsᴍ: {user_data['first_name']}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ: {'@' + user_data['username'] if user_data['username'] else '❌'}\n"
                    f"ʀᴇɢɪsᴛᴇʀ ᴛɪᴍᴇ: {user_data['created_at']}")
        else:
            return f"𝐔𝐬𝐞𝐫 𝐭𝐨𝐩𝐢𝐥𝐦𝐚𝐝𝐢 𝐛𝐮 𝐈𝐃 𝐞𝐠𝐚𝐬𝐢 𝐛𝐨𝐭𝐝𝐚 𝐫𝐨'𝐲𝐱𝐚𝐭𝐝𝐚𝐧 𝐨'𝐭𝐦𝐚𝐠𝐚𝐧 🤖👤❌"
    else:
        return f"𝐔𝐬𝐞𝐫 𝐭𝐨𝐩𝐢𝐥𝐦𝐚𝐝𝐢 𝐛𝐮 𝐈𝐃 𝐞𝐠𝐚𝐬𝐢 𝐛𝐨𝐭𝐝𝐚 𝐫𝐨'𝐲𝐱𝐚𝐭𝐝𝐚𝐧 𝐨'𝐭𝐦𝐚𝐠𝐚𝐧 🤖👤❌"
