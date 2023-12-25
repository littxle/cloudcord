import asyncio

import nextcord

import ezycord


class Bot(ezycord.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.default())

    async def setup_hook(self):
        await super().setup_hook()
        await self.tree.sync()


async def main():
    async with Bot() as bot:
        bot.add_help_command()
        bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
        await bot.start("TOKEN")  # Replace with your bot token


if __name__ == "__main__":
    asyncio.run(main())
