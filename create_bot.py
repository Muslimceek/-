from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = '7023231242:AAGcgJ7IJZ9OQ35Y7XD3Cqa2Ra5Nh4pGpEY'
bot_address = '@MuslimFitnnes_bot'
master_id = '1788817433'

storage = MemoryStorage()

bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)

client_commands = ['/start', '/help', 'Преподаватели', 'Тренировки', 'Режим работы',
                   'Контакты', '/moderate']