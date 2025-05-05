from fastapi import APIRouter, HTTPException
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_KEY = os.getenv('BEARER_KEY')



router = APIRouter()

@router.get("/trending")
def trending():
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
    "accept": "application/json",
    "include_adult": 'true',
    "Authorization": f"Bearer {BEARER_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        responseJson = response.json()
        result = responseJson["results"]
        finalResponse = []
        for i in result:
            movieId = i["id"]
            movieTitle = i["title"]
            moviePoster = i["poster_path"]
            res = {"movieId":movieId,"movieTitle":movieTitle, "moviePoster": f"https://image.tmdb.org/t/p/w500{moviePoster}"}
            finalResponse.append(res)
        return finalResponse

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
