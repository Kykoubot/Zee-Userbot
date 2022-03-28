from time import sleep
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import man_cmd, edit_or_reply


@man_cmd(pattern="teemo(?: |$)(.*)")
async def _(teemo):
    zea = await edit_or_reply(teemo, "`Teemo Mulu Lu 😏`")
    sleep(2)
    await zea.edit("`Jadian Juga Kagak😂`")
    sleep(1)
    await zea.edit("`Tapi Kalo Lu Jadian, Ujung-ujungnya Kena Ghosting Yahahayuk🤣`")


@man_cmd(pattern="give(?: |$)(.*)")
async def _(giveaway):
    zee = await edit_or_reply(giveaway, "`Syarat Ikut Giveaway`")
    sleep(2)
    await zee.edit("`Gcast Minimal 10 Grup`")
    sleep(1)
    await zee.edit("`Naik Os dan Ss Bukti Gcast`")


@man_cmd(pattern="uno(?: |$)(.*)")
async def _(uno):
    xd = await edit_or_reply(uno, "`Kakk 👉👈`")
    sleep(2)
    await xd.edit("`Bewan Uno Yuk 🙈`")
    sleep(1)
    await xd.edit("`Yang Kalah Pindah Agama 🙊`")


CMD_HELP.update(
    {
        "gabut2": f"**Plugin : **`gabut2`\
        \n\n  •  **Syntax :** `{cmd}teemo`\
        \n  •  **Function : **Coba sendiri.\
        \n\n  •  **Syntax :** `{cmd}give`\
        \n  •  **Function : **Coba Sendiri.\
        \n\n  •  **Syntax :** `{cmd}uno`\
        \n  •  **Function : **Coba Sendiri.\
    "
    }
)
