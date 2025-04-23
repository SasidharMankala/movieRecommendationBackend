from fastapi import APIRouter, HTTPException
import requests
import json


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
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"
    }
    try:
        res = requests.get(url, headers=headers, params=params)
        response = res.json()

        movie_ID = response['id']
        moviePoster = f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
        movieTitle = response['original_title']
        releaseYear = response['release_date'].split('-')
        rating = round((response['vote_average']/2),2)
        print(round(rating, 2))
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
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

