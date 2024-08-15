from aiogram import Router
from aiogram.types import Message
from datetime import datetime

from utils.news import get_latest_news
from utils.tg_users import create_new_tg_user, get_all_tg_users
from bot import main


router: Router = Router()


@router.message()
async def latest_news(message: Message):

    if str(message.text) == "/start":
        
        #creating new user
        user_data = {
            "full_name": f"{message.from_user.full_name}",
            "username": f"{"" if message.from_user.username==None else message.from_user.username}",
            "telegram_id": f"{message.from_user.id}",
        }
        await create_new_tg_user(user_id=message.from_user.id, data=user_data)

        text = f"""
                    Доброго времени суток {message.from_user.full_name}!
                    
                    Это бот для рассылок новостей от Apple. Для получения последних новостей введите команду /latest."""
        await message.reply(text)


    elif str(message.text) == "/latest":
        response_text = "Последние новости:\n\n"
        news = await get_latest_news()
        
        for new in news:
            result = ""
            title = str(new['title'])
            author = str(new['author'])
            news_text = str(new['text'])
            
            # Преобразование строки created_at в datetime объект и форматирование
            created_at = new['created_at']
            created_at = datetime.fromisoformat(created_at)  # Преобразуем ISO-строку в datetime объект
            created_at_formatted = created_at.strftime('%H:%M %d-%m-%Y')
            
            # Построение результата
            if author:
                result += f"{title} (by {author})\n"
            else:
                result += f"{title}\n"

            result += f"{news_text}\n{created_at_formatted}\n\n"

            # Добавляем результат к общему тексту ответа
            response_text += result

        await message.reply(text=response_text)

    else:
        pass
