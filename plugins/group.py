from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.group & filters.text)
async def delete_after_delay_group(client, message):
    if len(message.text) > 2:
        await asyncio.sleep(300)  # 5 minutes
        try:
            await message.delete()
        except Exception as e:
            print(f"Error deleting group message: {e}")