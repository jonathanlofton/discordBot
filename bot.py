import discord
import emoji
import config
import constants

client = discord.Client()

# all current users id's
channel_users = config.channel_users
# raw ids which will match the message request
nick_author_id = channel_users['Nick']['author_id']
jon_author_id = channel_users['Jon']['author_id']
austin_author_id = channel_users['Austin']['author_id']
frank_author_id = channel_users['Frank']['author_id']
# notifies users
nick_tag = f'<@{str(nick_author_id)}>'
jon_tag = f'<@{str(jon_author_id)}>'
austin_tag = f'<@{str(austin_author_id)}>'
frank_tag = f'<@{str(frank_author_id)}>'

# emojis in scope...
eye_emoji = emoji.emojize(':eyes:')
gun_emoji = emoji.emojize(':gun:')
muscle_emoji = emoji.emojize(':muscle:')
soccer_emoji = emoji.emojize(':soccer:')
demon_emoji = emoji.emojize(':smiling_face_with_horns:')
sparkle_emoji = emoji.emojize(':sparkles:')

@client.event # our connection to discord, this interacts with the Discord WebSocket and API
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    author_id = message.author.id
    name_of_messager = message.author.name
    name_of_channel = message.channel.name
    channel = message.channel
    message_content = message.content.lower()

    if message.author == client.user:
        return

    if name_of_messager == 'VAbreezy':
        await channel.send('well well well... look who decided to bless us with their presence today...')

    if message_content.find('@here') != -1:
        await channel.send('hey is there anyone who wants to play?')
        await channel.send(file=discord.File('./photos/anyone_wanna_play.jpg'))
        await channel.send('p-p-p-please?')

    if message_content.startswith('@spooky'):
        await channel.send(f'**Happy Halloween! {demon_emoji} MUAHAHAHA!**')
        await channel.send(file=discord.File('./photos/spooky_smile.jpg'))

    if message_content.find('@playtime') != -1:
        await channel.send('oh you want play time?')
        await channel.send(file=discord.File('./photos/mud_boys.jpg'))
        await channel.send('**LETS PLAY**')

    if message_content.find('@val') != -1:
        if author_id == nick_author_id:
            await channel.send(f'{jon_tag}, {name_of_messager} needs your help, he is hard stuck plat 2... straight buns.')
        elif author_id == jon_author_id:
            # tag nick _____ times :)
            huge_nick_tag, x = '', 0
            while x < 5: 
                huge_nick_tag += f'{nick_tag}\n'
                x += 1
            await channel.send(f'{huge_nick_tag} \n **GET THE FUCK ON DUDE**')
        else:
            await channel.send(f'oh shit, {name_of_messager} is stepping up... about god damn time... legooooo {nick_tag} {jon_tag}')

    if message_content.find('@rl') != -1:
        await channel.send(f'{jon_tag}{nick_tag}{austin_tag}{frank_tag} lets chase some balls...')

    if message_content.find('@csgo') != -1:
        await channel.send(f'shut up, boomer.')

    if message_content.find('!commands') != -1:
        list_of_commands = """
        {0}{0}**current commands:**{0}{0}
        **@rl:** notifies ball chasers {1}
        **@val:** notifies studs in the channel {2}{3}
        **@playtime:** you asked for it {4} 
        **@spooky:** {5} 
        **@csgo:**
        """
        await channel.send(list_of_commands.format(sparkle_emoji, soccer_emoji, gun_emoji, muscle_emoji, demon_emoji, eye_emoji))


@client.event
async def on_message_delete(message):
    name_of_messager = message.author.name
    await message.channel.send(f'{name_of_messager} why did you just delete: \n\n {message.content}... But, I\'ve been thinking a lot about these two...')
    await message.channel.send(file=discord.File('./photos/mud_boys.jpg'))

@client.event
async def on_message_edit(before_message, after_message):
    name = before_message.author.name
    await before_message.channel.send(f'{name} what are you editing? ' + emoji.emojize(':thinking_face:'))

client.run(config.BOT_TOKEN)
