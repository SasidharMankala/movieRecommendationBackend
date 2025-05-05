from fastapi import APIRouter, HTTPException
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_KEY = os.getenv('BEARER_KEY')


router = APIRouter()

@router.get("/recommend/{movieID}")
def recommend(movieID: int):
    url = f"https://api.themoviedb.org/3/movie/{movieID}/recommendations?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_KEY}"
    }

    try:
        res = requests.get(url, headers=headers)
        response = res.json()
        result = response["results"]
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
