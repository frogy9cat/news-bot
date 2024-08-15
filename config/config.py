from dataclasses import dataclass

from .base import getenv


from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")


@dataclass
class TelegramBotConfig:
    token: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment valriables
    # load_dotenv()

    return Config(tg_bot=TelegramBotConfig(token=getenv("BOT_TOKEN")))
