import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG = os.getenv('DEBUG')
PASSIVE = os.getenv('PASSIVE').lower()

if(not TOKEN):
    print("DISCORD_TOKEN not defined in your .env file")
    quit()

blocked_phrases = ['lol', 'l0l', 'lolz', 'lol2', 'l0lz', 'l0l2', 'rofl', 'r0fl', 'ha', 'h4', 'haha', 'hah4', 'h4ha', 'h4h4', 'lo|', 'l0|', '|ol', '|o|', '|0l', '|0|', 'lo|z', 'lo|2', 'l0|z', 'l0|2', '|olz', '|ol2', '|o|z', '|o|2', '|0lz', '|0l2', '|0|z', '|0|2', 'rof|', 'r0f|', 'loi', 'l0i', 'iol', 'ioi', 'i0l', 'i0i', 'loiz', 'loi2', 'l0iz', 'l0i2', 'iolz', 'iol2', 'ioiz', 'ioi2', 'i0lz', 'i0l2', 'i0iz', 'i0i2', 'rofi', 'r0fi']
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
            if PASSIVE=='true':
                await message.add_reaction('\U0001F92C')
            else:
                await message.delete()
                await message.author.create_dm()
                await message.author.dm_channel.send(
                    f'Hi {message.author}, `{message.content}` by itself doesn\'t really contribute much to the conversation. Consider adding a reaction or expanding your comment instead.'
                )

client = MyClient()
client.run(TOKEN)
blocked_file.close()
