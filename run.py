import os, nextcord
from dotenv import load_dotenv
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from nextcord.abc import GuildChannel


# Load .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# test guild 
test_guild_id = 1004101892781133975
intents = nextcord.Intents.all()
vestra = commands.Bot(command_prefix=">" , intents=intents)
vestra.remove_command("help")

@vestra.event
async def on_ready():
    print(f"{vestra.user} has connected to Discord!")

@vestra.command(description="Ping command")
async def ping(ctx):
    em = nextcord.Embed(
        title = f"{vestra.user.name}'s ping",
        description = f'**{round (vestra.latency * 1000)}**ms',
        color = 0xffef75
    )
    await ctx.reply(embed=em, mention_author=False)

@vestra.command(description="Help command")
async def help(ctx):
    em = nextcord.Embed(
        title = f"{vestra.user.name} Help Menu",
        description = "`💻 Ping` Return's the bot's latency.\n`📝 Help` Shows the help menu for the bot.\n`☢️ Nuke` Nukes a specified channel.",
        color = 0xffef75
    )
    em.add_field(name="Contribute to the bot", value=f"This bot is 100% open source. You can find it on [**GitHub**](https://github.com/3jm/nuke-bot)\nMade by [**rac#9999**](https://discord.com/users/911033722550222859)")
    await ctx.reply(embed=em, mention_author=False)

@vestra.command(description="Nuke command")
async def nuke(ctx, channel: GuildChannel = None):
    if channel == None:
        await ctx.reply("Please specify a channel to nuke.")
        return

    nuke_channel = nextcord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason='channel nuked')
        await new_channel.edit(position=nuke_channel.position)
        await nuke_channel.delete()
        await new_channel.send('Successfully Nuked')
        await new_channel.send('https://media0.giphy.com/media/4jyU0IuAH6a1q/200.gif?cid=95b27944e6cd82e7bf264019a6d2b03bc70e197a68db60dc&rid=200.gif&ct=g')
        await ctx.reply(f"Success.", mention_author=False)
    else:
        await ctx.reply(f'No channel named {channel.name}')

vestra.run(TOKEN)