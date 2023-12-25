import logging

from colorama import Fore

import ezycord
from ezycord import log

# overwrite colors for specific log levels
# this can be done with strings or with colorama
colors = {
    logging.DEBUG: "blue",
    logging.INFO: Fore.MAGENTA,
}

# call this function before creating the bot
ezycord.set_log(
    log_format=ezycord.LogFormat.default,
    colors=colors,
    webhook_url="WEBHOOK_URL",  # Replace with your webhook URL
)

log.debug("This is a debug message")
log.info("This is an info message")

ezycord.custom_log("CUSTOM", "This is a message with a custom log level")

bot = ezycord.Bot()

if __name__ == "__main__":
    # Load all cogs with a custom log style
    bot.load_cogs("cogs", log=ezycord.CogLog.default, log_color="green")
    bot.run("TOKEN")  # Replace with your bot token
