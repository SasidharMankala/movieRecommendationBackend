from fastapi import APIRouter, HTTPException, Query, Request
import requests
import json


router = APIRouter()

@router.post("/loadmorePref")
async def loadmore(request: Request, page: int = Query(2, ge=1)):
    res = await request.json()
    GENRE_ID = res["selected_genres"]
    actor = res["selected_actors"]
    ACTORS_ID = "|".join(actor.split(","))
    # print(ACTORS_ID)
    try:
        url = 'https://api.themoviedb.org/3/discover/movie'
        params = {
            'include_adult':'false',
            'include_video':'false',
            'language': 'en-US',
            'sort_by': 'popularity.desc',
            'with_genres': GENRE_ID,
            'page': page
        }
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"
        }

        totalMovies = []

    
        response = requests.get(url, headers=headers, params=params)
        res = response.json()
        for movie in res["results"]:
            det = {"movieId": movie["id"],"movieTitle":movie["original_title"], "moviePoster":f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"}
            totalMovies.append(det)
        
        params = {
            'include_adult':'false',
            'include_video':'false',
            'language': 'en-US',
            'sort_by': 'popularity.desc',
            'with_cast': ACTORS_ID,
            'page': 1
        }

        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        results = resp.json().get("results", [])
        # print(results)
        # Extract only id, title, and poster_path
        movies = [
            {"id": m["id"], "title": m["title"], "poster": m["poster_path"]}
            for m in results
        ]
        for movie in results:
            det = {"movieId": movie["id"],"movieTitle":movie["original_title"], "moviePoster":f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"}
            totalMovies.append(det)


        return totalMovies

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))