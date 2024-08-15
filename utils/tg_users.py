import requests
import json



async def create_new_tg_user(user_id:int, data:dict) -> dict:
    url = f'http://127.0.0.1:8000/api/tgusers/'
    
    #checking if the user exists
    r = requests.get(url=url)
    tg_users = json.loads(r.content)
    tg_users:list[dict]
    for tg_user in tg_users:
        if int(tg_user["telegram_id"]) == user_id:
            return "User already exists"
        else:
            pass

    #if user doesn't exists than create new user
    r = requests.post(url=url, json=data)
    return r.json()


async def get_all_tg_users() -> dict:
    url = f'http://127.0.0.1:8000/api/tgusers/'
    r = requests.get(url=url)
    data = json.loads(r.content)
    data:list[dict]
    return data


async def post_request(route:str, data:dict) -> dict:
    url = f'http://127.0.0.1:8000/{route}/'
    r = requests.post(url=url, json=data)
    return r.json()
