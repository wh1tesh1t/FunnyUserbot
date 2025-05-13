import asyncio
from hydrogram import Client
from userbot_config import *

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH
)

async def send_message_1():
    try:
        await app.send_message(chat_id=f"{FARM_GROUP_ID}", text=f"{FARM_MESSAGE}")
        print(f"Message `{FARM_MESSAGE}`, {FARM_GROUP_ID} sended.")
    except Exception as e:
        return

async def t_message_sending():
    await asyncio.sleep(5)

    while True:
        await send_message_1()
        await asyncio.sleep(INTERVAL_SECONDS)

async def main():
    print("Userbot Starting.")
    await app.start()
    print("Userbot Started.")

    asyncio.create_task(t_message_sending())

    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nError: KeyboardInterrupt")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'app' in locals() and isinstance(app, Client):
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    loop.run_until_complete(app.stop())
                else:
                    if sys.version_info >= (3, 7):
                         asyncio.run(app.stop())
                    else:
                         try:
                            new_loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(new_loop)
                            new_loop.run_until_complete(app.stop())
                         finally:
                            asyncio.set_event_loop(loop)
            except Exception as stop_e:
                 print(f"Error: {stop_e}")
            print("Exit from script.")
