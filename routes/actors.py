from fastapi import APIRouter, HTTPException
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_KEY = os.getenv('BEARER_KEY')



router = APIRouter()

@router.get("/actors")
def actors():

    url = "https://api.themoviedb.org/3/person/popular"
    headers = {
        "Authorization": f"Bearer {BEARER_KEY}",
        "Accept": "application/json"
    }

 

    response = requests.get(url, headers=headers)
    result = response.json()
    data = result["results"]

    actorsFull = [
        person for person in data
        if person.get("known_for_department") == "Acting"
    ]

    actor = []

    for i in actorsFull:
        id = i["id"]
        name = i['name']
        gender = i['gender']
        f = {"id":id, "name": name, "gender":gender}
        actor.append(f)
    
 
    return actor

