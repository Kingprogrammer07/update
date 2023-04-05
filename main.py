from config.config                  import client, events, is_admin
from telethon.tl.functions.account  import UpdateProfileRequest
from datetime                       import datetime
from asyncio                        import sleep
import random
from database.sqlDataBase           import db
from config.iloncha                 import *
import base64
from deep_translator                import GoogleTranslator
import pytz


uz_tz = pytz.timezone('Asia/Tashkent')
async def delete_messages(entity):
    async for message1 in client.iter_messages(entity, reverse=True):
        await client.delete_messages(entity, [message1.id])


async def update_name():
    name = await client.get_entity('me')

    while True:
        now = datetime.now(uz_tz)
        yil = now.year
        oy = now.month
        kun = now.day
        kun_nomi = GoogleTranslator(source='auto', target=f'uz').translate(now.strftime('%A'))

        try:
            soat = now.strftime("%H:%M ")
            if not ":" in name.first_name:
                if kun_nomi.lower() == "juma":
                    await client(UpdateProfileRequest(first_name = f"""{name.first_name} | {soat}""", about = f"Kun: {kun}.{oy}.{yil} | Kun nomi: {kun_nomi} || Juma Muborak Qadrdonlar !!🙂"))
                else:
                    await client(UpdateProfileRequest(first_name = f"""{name.first_name} | {soat}""", about = f"FullStack Programmer 🧑🏼‍💻 - ✅Obuna bo'lamiz: @foydali_dastur_kitobbot"))
            else:
                if kun_nomi.lower() == "juma":
                    await client(UpdateProfileRequest(first_name = f"""{name.first_name[:15]} | {soat}""", about = f"Kun: {kun}.{oy}.{yil} | Kun nomi: {kun_nomi} || Juma Muborak Qadrdonlar !!🙂"))
                else:
                    await client(UpdateProfileRequest(first_name = f"""{name.first_name[:15]} | {soat}""", about = f"FullStack Programmer🧑🏼‍💻✅Obuna bo'lamiz: @foydali_dastur_kitobbot"))

            await sleep(60) # har 1 minutda yangilanish uchun
            await client.send_message("@kesh_online_bot", "yangilash! => online")
            await sleep(1)
            await delete_messages("@kesh_online_bot")

        except:
            pass


# @client.on(events.NewMessage(chats=777967425))
@client.on(events.NewMessage)
async def handler(event):
    text = event.message.message
    message_id = event.message.id
    message = event.message
    get_id = await client.get_entity('me')
    admin_id = get_id.id

    # try:
    #     user_id = event.message.peer_id.user_id
    # except:
    #     user_id = event.message.peer_id.channel_id
    #
    # try:
    #     chat_id = event.message.from_id.user_id
    # except:
    #     chat_id =  event.message.peer_id.user_id



    reply = await message.get_reply_message()


    if text.startswith("."):
        if text == '.magic2':
            try:
                await event.message.edit('🌟')
                await sleep(0.2)
                await event.message.edit('🌟❤️')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟❤️')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟❤️❤️')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟\n❤️')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟\n❤️💜')
                await sleep(0.2)
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜')
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️')
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜')
                await event.message.edit('🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜')
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟🌟🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟🌟🌟❤️""")
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟🌟🌟❤️🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟🌟🌟❤️🌟🌟""")
                await sleep(0.2)
                await event.message.edit("""🌟❤️❤️🌟❤️❤️🌟\n❤️💜💜❤️💜💜❤️\n❤️💜💜❤️💜💜❤️\n🌟❤️💜💜💜❤️🌟\n🌟🌟❤️💜❤️🌟🌟\n🌟🌟🌟❤️🌟🌟🌟""")
                await event.message.edit("""💜""")
                await sleep(0.2)
                await event.message.edit("""💙""")
                await event.message.edit("""💚""")
                await sleep(0.2)
                await event.message.edit("""💛""")
                await event.message.edit("""🤍""")
                await sleep(0.2)
                await event.message.edit("""🖤""")
                await event.message.edit("""❤️‍🔥""")
                await sleep(0.2)
                await event.message.edit("""❤️‍🩹""")
                await sleep(0.4)
                await event.message.edit("""❤️""")
                await sleep(0.3)
                await event.message.edit("""I ❤️ YOU!""")
            except:
                await client.send_message(admin_id, '‼️ Diqqat Admin\n-**magic2**- so`zida xatolik')

        elif text == '.magic':
            try:
                arr = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "💖"]
                h = "🤍"
                first = ""
                for i in "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4]).split("\n"):
                    first += i + "\n"
                    await message.edit(first)
                    await sleep(0.2)
                for i in arr:
                    await message.edit("".join([h*9, "\n", h*2, i*2, h, i*2, h*2, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h*2, i*5, h*2, "\n", h*3, i*3, h*3, "\n", h*4, i, h*4, "\n", h*9]))
                    await sleep(0.3)
                for _ in range(8):
                    rand = random.choices(arr, k=34)
                    await message.edit("".join([h*9, "\n", h*2, rand[0], rand[1], h, rand[2], rand[3], h*2, "\n", h, rand[4], rand[5], rand[6], rand[7], rand[8],rand[9],rand[10], h, "\n", h, rand[11], rand[12], rand[13], rand[14], rand[15], rand[16],rand[17], h, "\n", h, rand[18], rand[19], rand[20], rand[21], rand[22], rand[23],rand[24], h, "\n", h*2, rand[25], rand[26], rand[27], rand[28], rand[29], h*2, "\n", h*3, rand[30], rand[31], rand[32], h*3, "\n", h*4, rand[33], h*4, "\n", h*9]))
                    await sleep(0.3)
                fourth = "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4, "\n", h*9])
                await message.edit(fourth)
                for _ in range(47):
                    fourth = fourth.replace("🤍", "❤️", 1)
                    await message.edit(fourth)
                    await sleep(0.1)
                for i in range(8):
                    await message.edit((arr[0]*(8-i)+"\n")*(8-i))
                    await sleep(0.4)
                for i in ["I", "I ❤️", "I ❤️ YOU", "I ❤️ YOU!"]:
                    await message.edit(f"<b>{i}</b>", parse_mode = "HTML")
                    await sleep(0.5)

            except:
                await client.send_message(admin_id, '‼️ Diqqat Admin\n-**magic**- so`zida xatolik')

        elif text == ".qor":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            if is_admin(admin_id, chat_id):
                try:
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit(' ☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n   ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(1.25)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️  \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    await sleep(0.75)
                    await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
                    sleep(1)
                    await message.edit("Qor kelyapti!🥳")
                except:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**qor**- so`zida xatolik')


        elif text == ".politsiya":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            if is_admin(admin_id, chat_id):
                try:
                    for _ in range(12):
                        for police in ['🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵',
                            '🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴']:
                            await message.edit(police)
                            await sleep(0.3)
                    await message.edit("<b>Tarqal tarqal!</b> 😂😂", parse_mode = "HTML")
                except:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**politsiya**- so`zida xatolik')


        elif text == ".juma":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    """juma bilan qutlash"""
                    juma = """
    ──╔╗
    ──║║
    ──║╠╗╔╦╗╔╦══╗
    ╔╗║║║║║╚╝║╔╗║
    ║╚╝║╚╝║║║║╔╗╠╦╦╦╦╗
    ╚══╩══╩╩╩╩╝╚╩╩╩╩╩╝"""
                    muborak = """
    ╔═╗╔═╗──╔╗─────────╔╗
    ║║╚╝║║──║║─────────║║
    ║╔╗╔╗╠╗╔╣╚═╦══╦═╦══╣║╔╗
    ║║║║║║║║║╔╗║╔╗║╔╣╔╗║╚╝╝
    ║║║║║║╚╝║╚╝║╚╝║║║╔╗║╔╗╗
    ╚╝╚╝╚╩══╩══╩══╩╝╚╝╚╩╝╚╝"""
                    ohiri = "<b>◍ Juma Muborak!</b> Qadrdonlar <b>(◍•ᴗ•◍)</b>"
                    await message.edit(juma,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(muborak,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(juma,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(muborak,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(juma,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(muborak,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(ohiri,parse_mode = "HTML")


            except:
                try:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**juma**- so`zida xatolik')
                except:
                    pass


        elif text == ".ajuma":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    """juma bilan qutlash - animatsiya"""
                    juma = """
    ──╔╗
    ──║║
    ──║╠╗╔╦╗╔╦══╗
    ╔╗║║║║║╚╝║╔╗║
    ║╚╝║╚╝║║║║╔╗╠╦╦╦╦╗
    ╚══╩══╩╩╩╩╝╚╩╩╩╩╩╝
    ╔═╗╔═╗──╔╗─────────╔╗
    ║║╚╝║║──║║─────────║║
    ║╔╗╔╗╠╗╔╣╚═╦══╦═╦══╣║╔╗
    ║║║║║║║║║╔╗║╔╗║╔╣╔╗║╚╝╝
    ║║║║║║╚╝║╚╝║╚╝║║║╔╗║╔╗╗
    ╚╝╚╝╚╩══╩══╩══╩╝╚╝╚╩╝╚╝"""
                    muborak = """
    ╔═╗╔═╗──╔╗─────────╔╗
    ║║╚╝║║──║║─────────║║
    ║╔╗╔╗╠╗╔╣╚═╦══╦═╦══╣║╔╗
    ║║║║║║║║║╔╗║╔╗║╔╣╔╗║╚╝╝
    ║║║║║║╚╝║╚╝║╚╝║║║╔╗║╔╗╗
    ╚╝╚╝╚╩══╩══╩══╩╝╚╝╚╩╝╚╝
    ──╔╗
    ──║║
    ──║╠╗╔╦╗╔╦══╗
    ╔╗║║║║║╚╝║╔╗║
    ║╚╝║╚╝║║║║╔╗╠╦╦╦╦╗
    ╚══╩══╩╩╩╩╝╚╩╩╩╩╩╝"""
                    ohiri = "<b>◍ Juma Muborak!</b> Qadrdonlar <b>(◍•ᴗ•◍)</b>"
                    await message.edit(juma,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(muborak,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(juma)
                    await sleep(1.0)
                    await message.edit(muborak,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(juma,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(muborak,parse_mode = "HTML")
                    await sleep(1.0)
                    await message.edit(ohiri,parse_mode = "HTML")


            except:
                try:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**ajuma**- so`zida xatolik')
                except:
                    pass


        elif text == ".tjuma":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    """juma bilan qutlash - katta yozuv"""
                    katta_yozuv = """

            ─╔╗─────────────╔╗───────╔╗
            ─║╠╦╦══╦═╗─╔══╦╦╣╚╦═╦╦╦═╗║╠╗
            ╔╣║║║║║║╬╚╗║║║║║║╬║╬║╔╣╬╚╣═╣
            ╚═╩═╩╩╩╩══╝╚╩╩╩═╩═╩═╩╝╚══╩╩╝"""
                    await message.edit(katta_yozuv, parse_mode = "HTML")
            except:
                try:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**tjuma**- so`zida xatolik')
                except:
                    pass


        elif text == ".magic3":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    arr = ["🥰", "😚", "☺️", "😘", "🤭", "😍", "😙", "🙃", "🤗"]
                    h = "◽"
                    first = ""
                    for i in "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4]).split("\n"):
                        first += i + "\n"
                        await message.edit(first)
                        await sleep(0.2)
                    for i in arr:
                        await message.edit("".join([h*9, "\n", h*2, i*2, h, i*2, h*2, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h*2, i*5, h*2, "\n", h*3, i*3, h*3, "\n", h*4, i, h*4, "\n", h*9]))
                        await sleep(0.3)
                    for _ in range(8):
                        rand = random.choices(arr, k=34)
                        await message.edit("".join([h*9, "\n", h*2, rand[0], rand[1], h, rand[2], rand[3], h*2, "\n", h, rand[4], rand[5], rand[6], rand[7], rand[8],rand[9],rand[10], h, "\n", h, rand[11], rand[12], rand[13], rand[14], rand[15], rand[16],rand[17], h, "\n", h, rand[18], rand[19], rand[20], rand[21], rand[22], rand[23],rand[24], h, "\n", h*2, rand[25], rand[26], rand[27], rand[28], rand[29], h*2, "\n", h*3, rand[30], rand[31], rand[32], h*3, "\n", h*4, rand[33], h*4, "\n", h*9]))
                        await sleep(0.3)
                    fourth = "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4, "\n", h*9])
                    await message.edit(fourth)
                    await sleep(0.1)
                    for i in range(8):
                        await message.edit((arr[0]*(8-i)+"\n")*(8-i))
                        await sleep(0.5)
                    for i in ["MEN", "MEN ❤️", "MEN SIZNI ❤️", "MEN SIZNI ❤️ SEVAMAN!"]:
                        await message.edit(f"<b>{i}</b>", parse_mode = "HTML")
                        await sleep(0.5)
            except:
                await client.send_message("me", '‼️ Diqqat Admin\n-**magic3**- so`zida xatolik')


        elif text == ".sana":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            now = datetime.now(uz_tz)
            yil = now.year
            oy = now.month
            kun = now.day
            soat = now.hour
            minut = now.minute
            sekunt = now.second
            kun_nomi = GoogleTranslator(source='auto', target=f'uz').translate(now.strftime('%A'))

            try:
                if is_admin(admin_id, chat_id):
                    try:
                        if oy < 10:
                            await message.edit(f"Bugun sana - **{kun}.0{oy}.{yil}**\nBugungi kun - **{kun_nomi.capitalize()}**\nHozir soat - **{soat}:{minut}:{sekunt}**")
                        else:
                            await message.edit(f"Bugun sana - **{kun}.{oy}.{yil}**\nHozir soat - **{soat}:{minut}:{sekunt}**")
                    except:
                        await client.send_message(admin_id, '‼️ Diqqat Admin\n-**sana**- so`zida xatolik')
            except:
                pass


        elif text == ".ilon":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    await message.edit(ii)
                    await sleep(0.5)
                    await message.edit(i1)
                    await sleep(0.5)
                    await message.edit(i2)
                    await sleep(0.5)
                    await message.edit(i3)
                    await sleep(0.5)
                    await message.edit(i4)
                    await sleep(0.5)
                    await message.edit(i5)
                    await sleep(0.5)
                    await message.edit(i6)
                    await sleep(0.5)
                    await message.edit(i7)
                    await sleep(0.5)
                    await message.edit(i8)
                    await sleep(0.5)
                    await message.edit(i9)
                    await sleep(0.5)
                    await message.edit(i10)
                    await sleep(0.5)
                    await message.edit(i11)
                    await sleep(0.5)
                    await message.edit(i12)
                    await sleep(0.5)
                    await message.edit(i13)
                    await sleep(0.5)
                    await message.edit(i14)
                    await sleep(0.5)
                    await message.edit(i15)
                    await sleep(0.5)
                    await message.edit(i16)
                    await sleep(0.5)
                    await message.edit(i17)
                    await sleep(0.5)
                    await message.edit(i18)
                    await sleep(0.5)
                    await message.edit(i19)
                    await sleep(0.5)
                    await message.edit(i20)
                    await sleep(0.5)
                    await message.edit(i21)
                    await sleep(0.5)
                    await message.edit(i22)
                    await sleep(0.5)
                    await message.edit(i23)
                    await sleep(0.5)
                    await message.edit(i24)
                    await sleep(0.5)
                    await message.edit(i25)
                    await sleep(0.5)
                    await message.edit(i26)
                    await sleep(0.5)
                    await message.delete()
            except:
                try:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**ilon**- so`zida xatolik')
                except:
                    pass


        elif text == ".ilonfull":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    await message.edit(ii)
                    await sleep(0.5)
                    await message.edit(i1)
                    await sleep(0.5)
                    await message.edit(i2)
                    await sleep(0.5)
                    await message.edit(i3)
                    await sleep(0.5)
                    await message.edit(i4)
                    await sleep(0.5)
                    await message.edit(i5)
                    await sleep(0.5)
                    await message.edit(i6)
                    await sleep(0.5)
                    await message.edit(i7)
                    await sleep(0.5)
                    await message.edit(i8)
                    await sleep(0.5)
                    await message.edit(i9)
                    await sleep(0.5)
                    await message.edit(i10)
                    await sleep(0.5)
                    await message.edit(i11)
                    await sleep(0.5)
                    await message.edit(i12)
                    await sleep(0.5)
                    await message.edit(i13)
                    await sleep(0.5)
                    await message.edit(i14)
                    await sleep(0.5)
                    await message.edit(i15)
                    await sleep(0.5)
                    await message.edit(i16)
                    await sleep(0.5)
                    await message.edit(i17)
                    await sleep(0.5)
                    await message.edit(i18)
                    await sleep(0.5)
                    await message.edit(i19)
                    await sleep(0.5)
                    await message.edit(i20)
                    await sleep(0.5)
                    await message.edit(i21)
                    await sleep(0.5)
                    await message.edit(i22)
                    await sleep(0.5)
                    await message.edit(i23)
                    await sleep(0.5)
                    await message.edit(i24)
                    await sleep(0.5)
                    await message.edit(i25)
                    await sleep(0.5)
                    await message.edit(i26)
                    await sleep(0.5)
                    await message.edit(i1)
                    await sleep(0.5)
                    await message.edit(i2)
                    await sleep(0.5)
                    await message.edit(i3)
                    await sleep(0.5)
                    await message.edit(i4)
                    await sleep(0.5)
                    await message.edit(i5)
                    await sleep(0.5)
                    await message.edit(i6)
                    await sleep(0.5)
                    await message.edit(i7)
                    await sleep(0.5)
                    await message.edit(i8)
                    await sleep(0.5)
                    await message.edit(i9)
                    await sleep(0.5)
                    await message.edit(i10)
                    await sleep(0.5)
                    await message.edit(i11)
                    await sleep(0.5)
                    await message.edit(i12)
                    await sleep(0.5)
                    await message.edit(i13)
                    await sleep(0.5)
                    await message.edit(i14)
                    await sleep(0.5)
                    await message.edit(i15)
                    await sleep(0.5)
                    await message.edit(i16)
                    await sleep(0.5)
                    await message.edit(i17)
                    await sleep(0.5)
                    await message.edit(i18)
                    await sleep(0.5)
                    await message.edit(i19)
                    await sleep(0.5)
                    await message.edit(i20)
                    await sleep(0.5)
                    await message.edit(i21)
                    await sleep(0.5)
                    await message.edit(i22)
                    await sleep(0.5)
                    await message.edit(i23)
                    await sleep(0.5)
                    await message.edit(i24)
                    await sleep(0.5)
                    await message.edit(i25)
                    await sleep(0.5)
                    await message.edit(i26)
                    await sleep(0.5)
                    await message.edit(i1)
                    await sleep(0.5)
                    await message.edit(i2)
                    await sleep(0.5)
                    await message.edit(i3)
                    await sleep(0.5)
                    await message.edit(i4)
                    await sleep(0.5)
                    await message.edit(i5)
                    await sleep(0.5)
                    await message.edit(i6)
                    await sleep(0.5)
                    await message.edit(i7)
                    await sleep(0.5)
                    await message.edit(i8)
                    await sleep(0.5)
                    await message.edit(i9)
                    await sleep(0.5)
                    await message.edit(i10)
                    await sleep(0.5)
                    await message.edit(i11)
                    await sleep(0.5)
                    await message.edit(i12)
                    await sleep(0.5)
                    await message.edit(i13)
                    await sleep(0.5)
                    await message.edit(i14)
                    await sleep(0.5)
                    await message.edit(i15)
                    await sleep(0.5)
                    await message.edit(i16)
                    await sleep(0.5)
                    await message.edit(i17)
                    await sleep(0.5)
                    await message.edit(i18)
                    await sleep(0.5)
                    await message.edit(i19)
                    await sleep(0.5)
                    await message.edit(i20)
                    await sleep(0.5)
                    await message.edit(i21)
                    await sleep(0.5)
                    await message.edit(i22)
                    await sleep(0.5)
                    await message.edit(i23)
                    await sleep(0.5)
                    await message.edit(i24)
                    await sleep(0.5)
                    await message.edit(i25)
                    await sleep(0.5)
                    await message.edit(i26)
                    await sleep(0.5)
                    await message.edit(i1)
                    await sleep(0.5)
                    await message.edit(i2)
                    await sleep(0.5)
                    await message.edit(i3)
                    await sleep(0.5)
                    await message.edit(i4)
                    await sleep(0.5)
                    await message.edit(i5)
                    await sleep(0.5)
                    await message.edit(i6)
                    await sleep(0.5)
                    await message.edit(i7)
                    await sleep(0.5)
                    await message.edit(i8)
                    await sleep(0.5)
                    await message.edit(i9)
                    await sleep(0.5)
                    await message.edit(i10)
                    await sleep(0.5)
                    await message.edit(i11)
                    await sleep(0.5)
                    await message.edit(i12)
                    await sleep(0.5)
                    await message.edit(i13)
                    await sleep(0.5)
                    await message.edit(i14)
                    await sleep(0.5)
                    await message.edit(i15)
                    await sleep(0.5)
                    await message.edit(i16)
                    await sleep(0.5)
                    await message.edit(i17)
                    await sleep(0.5)
                    await message.edit(i18)
                    await sleep(0.5)
                    await message.edit(i19)
                    await sleep(0.5)
                    await message.edit(i20)
                    await sleep(0.5)
                    await message.edit(i21)
                    await sleep(0.5)
                    await message.edit(i22)
                    await sleep(0.5)
                    await message.edit(i23)
                    await sleep(0.5)
                    await message.edit(i24)
                    await sleep(0.5)
                    await message.edit(i25)
                    await sleep(0.5)
                    await message.edit(i26)
                    await sleep(0.5)
                    await message.edit(i1)
                    await sleep(0.5)
                    await message.edit(i2)
                    await sleep(0.5)
                    await message.edit(i3)
                    await sleep(0.5)
                    await message.edit(i4)
                    await sleep(0.5)
                    await message.edit(i5)
                    await sleep(0.5)
                    await message.edit(i6)
                    await sleep(0.5)
                    await message.edit(i7)
                    await sleep(0.5)
                    await message.edit(i8)
                    await sleep(0.5)
                    await message.edit(i9)
                    await sleep(0.5)
                    await message.edit(i10)
                    await sleep(0.5)
                    await message.edit(i11)
                    await sleep(0.5)
                    await message.edit(i12)
                    await sleep(0.5)
                    await message.edit(i13)
                    await sleep(0.5)
                    await message.edit(i14)
                    await sleep(0.5)
                    await message.edit(i15)
                    await sleep(0.5)
                    await message.edit(i16)
                    await sleep(0.5)
                    await message.edit(i17)
                    await sleep(0.5)
                    await message.edit(i18)
                    await sleep(0.5)
                    await message.edit(i19)
                    await sleep(0.5)
                    await message.edit(i20)
                    await sleep(0.5)
                    await message.edit(i21)
                    await sleep(0.5)
                    await message.edit(i22)
                    await sleep(0.5)
                    await message.edit(i23)
                    await sleep(0.5)
                    await message.edit(i24)
                    await sleep(0.5)
                    await message.edit(i25)
                    await sleep(0.5)
                    await message.edit(i26)
                    await sleep(0.5)
                    await message.delete()
            except:
                try:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**ilonfull**- so`zida xatolik')
                except:
                    pass


        elif text.startswith(".tr"):
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    text = " ".join(text.split()[1:])
                    til = db.equals_view()
                    translate = GoogleTranslator(source='auto', target=f'{til}').translate(text)
                    await message.edit(translate, parse_mode = "HTML")
            except:
                try:
                    await client.send_message(admin_id, '‼️ Diqqat Admin\n-**tr**- tarjima qilishda xatolik')
                except:
                    pass

        elif text.startswith(".select"):
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            if is_admin(admin_id, chat_id):
                try:
                    text = text.split()[1]
                    text = text.lower()
                except:
                    await message.edit("Tilni doimiy qilish uchun <pre>.select</pre> so`zidan keyin tilning kodini kiriting!!", parse_mode = "HTML")
                if db.is_code_country(text):
                    db.equals(text)
                    await  message.edit(f"<b>Til tanlandi!</b>\n<pre>.tr</pre> So`zidan keyin xohlagan so`zingizni <b>{text}</b> tiliga tarjima qilamiz..", parse_mode = "HTML")
                else:
                    await  message.edit("<b>Bazada bo`lmagan tilni tanlamoqchisizz!!!!</b>", parse_mode = "HTML")



        elif text.startswith('.load'):
            mod_name = text.split()[1]
            if mod_name.startswith("."):
                mod_url = text.split()[2]
                try:
                    chat_id = event.message.from_id.user_id
                except:
                    chat_id = event.message.peer_id.user_id
                    
                if is_admin(admin_id, chat_id):
                    try:
                        await message.edit(text = f"{db.voice_table_update_insert(mod_name, mod_url)}", parse_mode = "Markdown")
                    except:
                        await client.send_message(admin_id, f'‼️ Diqqat Admin\n-**load**- qilish so`zida xatolik')

            else:
                await message.edit("Ovoz modullarini boshlanishida <b>.</b>(nuqta) bilan qo`shing!!", parse_mode = "HTML")

        elif text == ".help":
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id):
                    try:
                        royhat_data = str()
                        for kod,about in db.voice_code_royhat_view():
                            royhat_data += f"\n<pre>{kod}</pre> - <b>{about}</b>"
                        await message.edit(f"🔊 Ovozli Buyruqlarning kodlari:\n{royhat_data}", parse_mode = "HTML")
                    except:
                        await client.send_message(admin_id, f'‼️ Diqqat Admin\n-**help**- so`zida xatolik')
            except:
                pass

        else:
            try:
                user_id = event.message.peer_id.user_id
            except:
                user_id = event.message.peer_id.channel_id
            try:
                chat_id = event.message.from_id.user_id
            except:
                chat_id = event.message.peer_id.user_id
            try:
                if is_admin(admin_id, chat_id) and db.is_voice_code(text):
                    try:
                        await client.delete_messages(user_id,message_id)
                        await client.send_file(user_id, file = f"{db.voice_code_view(text)}", reply_to = reply.id if reply else None)
                    except:
                        await client.send_message(admin_id, f'‼️ Diqqat Admin\n-**{text}**- so`zida xatolik')
            except:
                pass




if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(update_name())
        client.start()
        client.run_until_disconnected()
