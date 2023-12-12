import asyncio
import importlib
from pyrogram import Client, idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Bootingཽ͡ ⃝𝆺𝅥𝐌ꝛ፝֟ [🃜]❛𝐊ɩŋʛ𝅃꯭᳚𝅃꯭᳚𓄂️𓆪ꪾ..")
    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported ཽ͡ ⃝𝆺𝅥𝐌ꝛ፝֟ [🃜]❛𝐊ɩŋʛ𝅃꯭᳚𝅃꯭᳚𓄂️𓆪ꪾ {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
