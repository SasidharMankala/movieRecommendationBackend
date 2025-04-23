from fastapi import APIRouter, HTTPException
import requests
import json


router = APIRouter()

@router.get("/alreadywatched/{movieIDs}")
def movieDetails(movieIDs: str):
    # print(movieIDs)
    movieList = movieIDs.split(",")
    print(movieList)

    try:
        watchedMovies = []

        for  i in movieList:
            print(i)

            url = f'https://api.themoviedb.org/3/movie/{i}'
            params = {
                "language": "en-US"
            }
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"
            }
            response = requests.get(url, headers=headers, params=params)
            movie = response.json()
            movieId = movie["id"]
            movieTitle = movie["title"]
            moviePoster = movie["poster_path"]
            res = {"movieId":movieId,"movieTitle":movieTitle, "moviePoster": f"https://image.tmdb.org/t/p/w500{moviePoster}"}
            print(res)
            watchedMovies.append(res)
        
        return watchedMovies
    

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
