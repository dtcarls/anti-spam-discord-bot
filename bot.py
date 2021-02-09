import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG = os.getenv('DEBUG')

if(not TOKEN):
    print("DISCORD_TOKEN not defined in your .env file")
    quit()

blocked_phrases = ['lol', 'l0l', 'lewl', 'rofl', 'lolol' 'ha', 'haha', '|o|', '|0|', 'ioi', 'i0i', 'loi', 'l0i', 'i0l', 'iol']
blocked_file = open('blocked.txt', 'w')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}! READY!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user or message.attachments:
            return
        if DEBUG:
            print('Message {0.author}: {0.content}'.format(message))

        stripped_msg = "".join(message.content.lower().split()).replace(",","").replace(".","").replace("!","")
        if stripped_msg in blocked_phrases:
            print('Blocked Message {0.author}: {0.content}'.format(message), file = blocked_file)
            await message.delete()
            await message.author.create_dm()
            await message.author.dm_channel.send(
                f'Hi {message.author}, `{message.content}` by itself doesn\'t really contribute much to the conversation. Consider adding a reaction or expanding your comment instead.'
            )

client = MyClient()
client.run(TOKEN)
blocked_file.close()