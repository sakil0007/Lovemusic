#
# Copyright (C) 2021-2022 by Insane_Help365 @Github, < https://github.com/TheTeamInsane >.
# #

# Kanged By © @always_hungry365
# Rocks © @Dosto_ki_Mehfil786
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Insane © Insane


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from InsaneMusic import LOGGER, app, userbot
from InsaneMusic.core.call import Insane
from InsaneMusic.plugins import ALL_MODULES
from InsaneMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("InsaneMusic").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("InsaneMusic.plugins" + all_module)
    LOGGER("InsaneMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Insane.start()
    try:
        await Insane.stream_call("https://telegra.ph//file/90412f6f3e1037fb0a1c4.jpg")
    except NoActiveGroupCall:
        LOGGER("InsaneMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Insane.decorators()
    LOGGER("InsaneMusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("InsaneMusic").info("Stopping Music Bot")
