import discord
import config

client = discord.Client()

@client.event # our connection to discord, this interacts with the Discord WebSocket and API
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.display_name == 'VAbreezy':
        await message.channel.send('well well well... look who decided to bless us with their presence today...')

    if message.content.find('@here') != -1:
        await message.channel.send('hey is there anyone who wants to play?')
        await message.channel.send(file=discord.File('./photos/anyone_wanna_play.jpg'))
        await message.channel.send('p-p-p-please?')

    if message.content.startswith('spooky'):
        await message.channel.send('Happy Halloween! MUAHAHAHA!')
        await message.channel.send(file=discord.File('./photos/spooky_smile.jpg'))

    if message.content.find('play') != -1:
        await message.channel.send('oh you want to play?')
        await message.channel.send(file=discord.File('./photos/mud_boys.jpg'))
        await message.channel.send('LETS PLAY')

client.run(config.BOT_TOKEN)
