from typing import List

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

# Defines a simple paginator of buttons for the embed.
class Menu(discord.ui.View):
    def __init__(self, embeds: List[discord.Embed]):
        super().__init__(timeout=None)

        # Sets the embed list variable.
        self.embeds = embeds

        # Current embed number.
        self.embed_count = 0

        # Disables previous page button by default.
        self.prev_page.disabled = True

        # Sets the footer of the embeds with their respective page numbers.
        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"Page {i + 1} of {len(self.embeds)}")

    @discord.ui.button(label="Previous page", emoji="◀️", style=discord.ButtonStyle.red)
    async def prev_page(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        # Decrements the embed count.
        self.embed_count -= 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

        # Enables the next page button and disables the previous page button if we're on the first embed.
        self.next_page.disabled = False
        if self.embed_count == 0:
            self.prev_page.disabled = True

        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Next page", emoji="▶️", style=discord.ButtonStyle.green)
    async def next_page(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        # Increments the embed count.
        self.embed_count += 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

        # Enables the previous page button and disables the next page button if we're on the last embed.
        self.prev_page.disabled = False
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True

        await interaction.response.edit_message(embed=embed, view=self)


@bot.command()
async def paginator(ctx: commands.Context):

    # Creates the embeds as a list.
    embeds = [
        discord.Embed(
            title="Paginator example",
            description="This is the first embed.",
            colour=discord.Colour.random(),
        ),
        discord.Embed(
            title="Paginator example",
            description="This is the second embed.",
            colour=discord.Color.random(),
        ),
        discord.Embed(
            title="Paginator example",
            description="This is the third embed.",
            colour=discord.Color.random(),
        ),
    ]

    # Sets the footer of the first embed.
    embeds[0].set_footer(text=f"Page 1 of {len(embeds)}")

    # Sends first embed with the buttons, it also passes the embeds list into the View class.
    await ctx.send(embed=embeds[0], view=Menu(embeds))


bot.run("token")
