from fastapi import APIRouter, HTTPException
import requests
import json


router = APIRouter()

@router.get("/trending")
def trending():
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
    "accept": "application/json",
    "include_adult": 'true',
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"}

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
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
