import requests
import json



async def get_latest_news():
    response = requests.get('http://127.0.0.1:8000/api/news/latest3')
    data = json.loads(response.content)
    data : list[dict]
    return data
