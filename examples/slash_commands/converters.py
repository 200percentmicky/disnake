import discord
from discord.ext import commands

bot = commands.Bot("!")

# classic commands.Converter classes have been replaced by more user-friendly converter functions
# These can be set using a parameter of Param
@bot.slash_command()
async def clean_content_converter(
    inter: discord.CommandInteraction,
    text: str = commands.Param(converter=lambda inter, text: text.replace("@", "\\@")),
):
    ...


# Converters may also set the type of the option using annotations
# here the converter is actually using a user option despite the actual command being annotated as str
def avatar_converter(inter: discord.CommandInteraction, user: discord.User) -> str:
    return user.display_avatar.url


@bot.slash_command()
async def command_with_avatar(
    inter: discord.CommandInteraction,
    avatar: str = commands.Param(converter=avatar_converter),
):
    ...


# Converting to custom classes is also very easy using class methods
class SomeCustomClass:
    def __init__(self, username: str, discriminator: str) -> None:
        self.username = username
        self.discriminator = discriminator

    @classmethod
    async def from_option(cls, inter: discord.CommandInteraction, user: discord.User):
        return cls(user.name, user.discriminator)


@bot.slash_command()
async def command_with_clsmethod(
    inter: discord.CommandInteraction,
    some: SomeCustomClass = commands.Param(converter=SomeCustomClass.from_option),
):
    ...


# an even better approach is to register a method
# as the class converter to be able to use only an annotation
class OtherCustomClass:
    def __init__(self, username: str, discriminator: str) -> None:
        self.username = username
        self.discriminator = discriminator

    @commands.converter_method
    async def convert(cls, inter: discord.CommandInteraction, user: discord.User):
        return cls(user.name, user.discriminator)


@bot.slash_command()
async def command_with_convmethod(
    inter: discord.CommandInteraction,
    other: OtherCustomClass,
):
    ...
