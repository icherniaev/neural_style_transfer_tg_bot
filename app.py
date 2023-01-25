import asyncio
import logging


from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_other_handlers


from style_transfer.processing import stylize
from environs import Env

'''env = Env()
env.read_env()'''

# Initialize logger
logger = logging.getLogger(__name__)

# Function for regestering all handlers
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)
    
# Function for loading the bot
async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')
    
    # Print the info about starting the bot
    logger.info('Starting bot')
    
    # Load configuration in config variable
    config: Config = load_config()
    
    # Initialize bot and dispatcher
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp: Dispatcher = Dispatcher(bot)
    
    # Register all handlers
    register_all_handlers(dp)
    
    # Load polling
    try:
        await dp.start_polling()
    finally:
        await bot.close()
        
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')