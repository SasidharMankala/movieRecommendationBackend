from fastapi import APIRouter, HTTPException
import requests
import json


router = APIRouter()

@router.get("/actors")
def actors():

    url = "https://api.themoviedb.org/3/person/popular"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw",
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

