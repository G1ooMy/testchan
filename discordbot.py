from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('--------------')
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    channel = client.get_channel('チャンネルID')
    await channel.send('楽しいTRPGを始めましょう！')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!dice"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
