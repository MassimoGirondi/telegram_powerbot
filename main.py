import logging
from pprint import pprint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, MessageFilter
import actions
import config
from functools import partial


#logging.basicConfig(level=logging.DEBUG,
#                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=config.log_name,
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=config.log_level)
logger = logging.getLogger(__name__)
handler = logging.handlers.RotatingFileHandler(config.log_name, maxBytes=1024, backupCount=1, delay=0)
logger.addHandler(handler)



def start(update, context):
    if len(config.authorized):
        update.message.reply_text(f"Hi {update.message.from_user.username}!\nYour user ID is {update.message.from_user.id}.\n")
    else:
        update.message.reply_text(f"Hi {update.message.from_user.username}!\nYour user ID is {update.message.from_user.id}.\nThis bot is running without user restriction!")

def echo(update, context):
    update.message.reply_text(update.message.text)



# The list of actions that the bot supports
handlers =  {
        "halt": actions.halt,
        "wake": actions.wol,
        "suspend": actions.suspend,
        "ping": actions.ping,
        "uptime" : actions.uptime
        }

class UserFilter(MessageFilter):
    def filter(self,message):
        if(len(config.authorized)):
            return str(message.from_user.id) in config.authorized
        else:
            return True



def main():
    updater = Updater(config.token, use_context=True)
    userFilter=UserFilter() 

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    
    dp.add_handler(CommandHandler("start", start,userFilter))
    
    for k,v in handlers.items():
        # Let's create a partial function call (it's ugly but it works ;))
        f = partial(lambda u,c,foo: u.message.reply_text(foo(),quote=True),foo=v)
        dp.add_handler(CommandHandler(k,
            f,
            userFilter))

    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command & userFilter, echo))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
