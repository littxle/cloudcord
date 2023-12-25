import logging

from colorama import Fore

import cloudcord
from cloudcord import log

# overwrite colors for specific log levels
# this can be done with strings or with colorama
colors = {
    logging.DEBUG: "blue",
    logging.INFO: Fore.MAGENTA,
}

# call this function before creating the bot
cloudcord.set_log(
    log_format=cloudcord.LogFormat.default,
    colors=colors,
    webhook_url="WEBHOOK_URL",  # Replace with your webhook URL
)

log.debug("This is a debug message")
log.info("This is an info message")

cloudcord.custom_log("CUSTOM", "This is a message with a custom log level")

bot = cloudcord.Bot()

if __name__ == "__main__":
    # Load all cogs with a custom log style
    bot.load_cogs("cogs", log=cloudcord.CogLog.default, log_color="green")
    bot.run("TOKEN")  # Replace with your bot token
