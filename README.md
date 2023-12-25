[![ezycord]( https://raw.githubusercontent.com/Timoo12/ezycord/main/docs/_static/ezycord.png)](https://github.com/Timoo12/ezycord)

[![](https://img.shields.io/pypi/v/ezycord.svg?style=for-the-badge&logo=pypi&color=yellow&logoColor=white)](https://pypi.org/project/ezycord/)
[![](https://img.shields.io/pypi/l/ezycord?style=for-the-badge)](https://github.com/Timoo12/ezycord/blob/main/LICENSE)

An easy-to-use extension for [Discord.py](https://github.com/Rapptz/discord.py)
and [Pycord](https://github.com/Pycord-Development/pycord) with some utility functions.

## Features
### ✏️ Reduce boilerplate code
- Easy cog management
- Embed templates
- Datetime and file utilities
- Wrapper for [aiosqlite](https://github.com/omnilib/aiosqlite)

### ✨ Error handling
- Automatic error handling for slash commands
- Error webhook reports
- Custom logging

### ⚙️ Extensions
- **Help command** - Automatically generate a help command for your bot
- **Status changer** - Change the bot's status in an interval
- **Blacklist** - Block users from using your bot

## Installing
Python 3.9 or higher is required.
```
pip install ezycord
```
You can also install the latest version from GitHub. Note that this version may be unstable
and requires [git](https://git-scm.com/downloads) to be installed.
```
pip install git+https://github.com/Timoo12/ezycord
```
If you need the latest version in your `requirements.txt` file, you can add this line:
```
ezycord @ git+https://github.com/Timoo12/ezycord
```

## Useful Links
- [Documentation](https://ezycord.readthedocs.io/) | [Getting started](https://ezycord.readthedocs.io/en/latest/pages/getting_started.html)
- [Pycord](https://docs.pycord.dev/) | [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [PyPi](https://pypi.org/project/ezycord/)

## Examples
- For more examples, see the [example repository](https://github.com/Timoo12/ezycord-template)
or the [sample code](https://ezycord.readthedocs.io/en/latest/examples/examples.html).
- **Note:** It's recommended to [load the token](https://guide.pycord.dev/getting-started/creating-your-first-bot#protecting-tokens) from a `.env` file instead of hardcoding it.
ezycord can automatically load the token if a `TOKEN` variable is present in the `.env` file.

### Pycord
```py
import ezycord
import discord

bot = ezycord.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
    bot.run("TOKEN")
```

### Discord.py
```py
import asyncio
import discord
import ezycord


class Bot(ezycord.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def setup_hook(self):
        await super().setup_hook()
        await self.tree.sync()


async def main():
    async with Bot() as bot:
        bot.add_help_command()
        bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
        await bot.start("TOKEN")


if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing
I am always happy to receive contributions. Here is how to do it:
1. Fork this repository
2. Make changes
3. Create a pull request

You can also [create an issue](https://github.com/Timoo12/ezycord/issues/new) if you find any bugs.
