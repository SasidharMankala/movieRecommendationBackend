from fastapi import APIRouter, HTTPException
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_KEY = os.getenv('BEARER_KEY')


router = APIRouter()

@router.get("/alreadywatched/{movieIDs}")
def movieDetails(movieIDs: str):

    movieList = movieIDs.split(",")

    try:
        watchedMovies = []

        for  i in movieList:

            url = f'https://api.themoviedb.org/3/movie/{i}'
            params = {
                "language": "en-US"
            }
            
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {BEARER_KEY}"
            }
            response = requests.get(url, headers=headers, params=params)
            movie = response.json()
            movieId = movie["id"]
            movieTitle = movie["title"]
            moviePoster = movie["poster_path"]
            res = {"movieId":movieId,"movieTitle":movieTitle, "moviePoster": f"https://image.tmdb.org/t/p/w500{moviePoster}"}
            watchedMovies.append(res)
        
        return watchedMovies
    

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
