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

    if message.content.startswith('nick'):
        await message.channel.send('nick loves dick!')

    if message.content.startswith('nicks body pillow'):
        await message.channel.send('I\'m abused by him daily, I have been traumatized beyond your wildest dreams...')

    if message.content.startswith('frank'):
        await message.channel.send('frank stank!')

    if message.content.startswith('@Im a shoe'):
        await message.channel.send('austin be flossin!')

    if message.content.startswith('joey'):
        await message.channel.send('joe a hoe!')

    if message.content.startswith('jon'):
        await message.channel.send('hail our lord and savior!')

    if message.content.startswith('@here'):
        await message.channel.send('real gaming hours are upon us!')

    if message.content.startswith('spooky'):
        await message.channel.send('Happy Halloween! MUAHAHAHA!')
        await message.channel.send(file=discord.File('./photos/spooky_smile.jpg'))

client.run(config.BOT_TOKEN)