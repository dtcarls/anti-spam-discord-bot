import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG = os.getenv('DEBUG')

if(not TOKEN):
    print("DISCORD_TOKEN not defined in your .env file")
    quit()

blocked_phrases = ['lol', 'l0l', 'lewl', 'rofl', 'lolol' 'ha', 'haha']
blocked_file = open('blocked.txt', 'w')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}! READY!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        if DEBUG:
            print('Message from {0.author}: {0.content}'.format(message))

        if message.content.lower() in blocked_phrases:
            print('Blocked Message {0.author}: {0.content}'.format(message), file = blocked_file)
            await message.delete()
            await message.author.create_dm()
            await message.author.dm_channel.send(
                f'Hi {message.author}, `{message.content}` by itself doesn\'t really contribute much to the conversation. Consider adding a reaction or expanding your comment instead.'
            )

client = MyClient()
client.run(TOKEN)
blocked_file.close()