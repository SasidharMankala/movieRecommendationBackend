from fastapi import APIRouter, HTTPException
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_KEY = os.getenv('BEARER_KEY')


router = APIRouter()

@router.get("/movieDetails/{movieID}")
def movieDetails(movieID: int):
    url = f'https://api.themoviedb.org/3/movie/{movieID}'
    params = {
        "append_to_response": "videos,credits",
        "language": "en-US"
    }
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_KEY}"
    }
    try:
        res = requests.get(url, headers=headers, params=params)
        response = res.json()

        movie_ID = response['id']
        moviePoster = f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
        movieTitle = response['original_title']
        releaseYear = response['release_date'].split('-')
        rating = round((response['vote_average']/2),2)
        movieDescription = response['overview']
        cast = response['credits']['cast']
        video = response['videos']['results'][0]['key']
        trailer = f'https://www.youtube.com/watch?v={video}'
        castNames = []
        for i in cast:
            castNames.append(i['name'])
        director = response['credits']['crew']
        directors = [p["name"] for p in director if p.get("job") == "Director"]

        
        result = {
            'movieID':movie_ID,
            'moviePoster':moviePoster,
            'movieTitle':movieTitle,
            'releaseYear':releaseYear[0],
            'trailer':trailer,
            'rating':rating,
            'movieDescription':movieDescription,
            'cast':castNames,
            'director':directors
        }
        

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

