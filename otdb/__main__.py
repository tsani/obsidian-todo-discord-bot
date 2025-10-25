import asyncio
import discord
from urllib.parse import quote
from os import getenv

BOT_TOKEN = getenv('BOT_TOKEN')

class OTDB(discord.Client):
    async def on_ready(self):
        print('ready!')

    async def on_message(self, message):
        if message.channel.name != 'todo-obsidian': return

        todo_string = quote(f'- [ ] #task {message.content}')
        proc = await asyncio.create_subprocess_exec(
            '/usr/bin/xdg-open',
            f"obsidian://new?silent&vault=household-vault&append&file=meta%2fTask%20list&content={todo_string}",
        )
        await proc.wait()
        print('added a todo')

intents = discord.Intents.default()
intents.message_content = True

client = OTDB(intents=intents)
client.run(BOT_TOKEN)
