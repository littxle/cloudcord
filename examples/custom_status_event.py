import cloudcord
import discord

bot = cloudcord.Bot()

def get_coins(): # This can also be async
    return 69

bot.add_status_changer(
    [
        "{guild_count} servers", # Strings will be converted to CustonActivity
        discord.Game("with {coins} coins")
    ],
    coins = get_coins
)