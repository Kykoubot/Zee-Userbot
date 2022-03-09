# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @zeafeya
# FROM Zee-Userbot <https://github.com/kykoubot/Zee-Userbot>
# t.me/Dbzea & t.me/Storezeastore

import random
import time
from datetime import datetime

from speedtest import Speedtest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, man_cmd

absen = [
    "**Saya Hadir** 😁",
    "**Absen Gweh Juga** 😉",
    "**Cok Ikutan** 😁",
    "**Hadir Ganteng** 😐",
    "**Hadir Kawan** 😎",
    "**Hadir Bang Maap Telat** 😴",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@man_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**.**")
    await xx.edit("**..**")
    await xx.edit("**...**")
    await xx.edit("**....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await xx.edit(
        f"**PONG🏓..!!**\n"
        f"**▹ Pinger ·** `%sms`\n"
        f"**▹ Uptime ·** `{uptime}` \n"
        f"**▹ Master ·** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )



@man_cmd(pattern="xping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@man_cmd(pattern="lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await edit_or_reply(ping, "**★**")
    await lping.edit("**★★**")
    await lping.edit("**★★★**")
    await lping.edit("**★★★★**")
    await lping.edit("**✦҈͜͡➳ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"❃ **Ping !!** "
        f"`%sms` \n"
        f"❃ **Uptime -** "
        f"`{uptime}` \n"
        f"**✦҈͜͡➳ Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@man_cmd(pattern="keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**AKU**")
    await kopong.edit("**SAYANG**")
    await kopong.edit("**KAMU**")
    await kopong.edit("**TAPI BOONG HAHA**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**✲ BOMB** "
        f"\n HEYAAA `%sms` \n"
        f"**✲ KENALIN NIH SI PALING CAKEP** "
        f"\n TUAN『[{user.first_name}](tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala


@man_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8===✊D💦")
    await kping.edit("8====D💦💦")
    await kping.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**ENAK!! 🐨**\n**NJIRR** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@man_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@man_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Sepong.....💫`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("💫 **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(incoming=True, from_users=2120344815, pattern=r"^.absen$")
async def zeafeya(ganteng):
    await ganteng.reply(random.choice(absen))


# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  •  **Syntax :** `{cmd}ping` ; `{cmd}lping` ; `{cmd}xping` ; `{cmd}kping`\
        \n  •  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  •  **Syntax :** `{cmd}pong`\
        \n  •  **Function : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  •  **Syntax :** `{cmd}speedtest`\
        \n  •  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
