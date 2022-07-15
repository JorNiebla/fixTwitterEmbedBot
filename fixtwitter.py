import discord
import os

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if (not message.author.bot) and ("twitter.com" in message.content):
            fixedembed = message.content.replace("twitter.com", "twxtter.com")
            await message.edit(suppress=True)
            await message.reply(fixedembed,mention_author=False)


TOKEN = os.getenv('TOKEN')
intents = discord.Intents(messages=True, guilds=True)
client = MyClient(intents=intents)
client.run(str(TOKEN))