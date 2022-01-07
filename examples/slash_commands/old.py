"""
An example of old-style options.
Not the most convenient syntax.
"""
import discord
from discord.ext import commands

bot = commands.Bot("!")


@bot.slash_command(
    name="slash_command",
    description="A Simple Slash Command",
    options=[
        discord.Option("string", description="A string to send", required=True),
        discord.Option(
            "channel", description="The destination channel", type=discord.OptionType.channel
        ),
        discord.Option(
            "number", description="The number of repetitions", type=discord.OptionType.integer
        ),
    ],
)
async def command(inter, string, channel=None, number=1):
    channel = channel or inter.channel
    await inter.response.send_message(
        f"Sending {string} {number}x to {channel.mention}", ephemeral=True
    )
    await channel.send(string * number)
