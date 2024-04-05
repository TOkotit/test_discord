import asyncio
import discord
import logging
import pymorphy2
from TOKEN import TOKEN

morph = pymorphy2.MorphAnalyzer()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):

        if message.author == self.user:
            return
        if 'set_timer' in message.content.lower():
            message_ = message.content.split()
            hours = int(message_[message_.index('hours') - 1])
            minutes = int(message_[message_.index('minutes') - 1])
            await message.channel.send(f'the timer start in {hours} hours and {minutes} minutes')
            await asyncio.sleep(hours * 60 * 60 + minutes * 60)
            await message.channel.send('Ахтунг!!! Time X has come!!')

        else:
            await message.channel.send("Спасибо за сообщение")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
