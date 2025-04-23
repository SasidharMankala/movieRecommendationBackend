from fastapi import APIRouter, HTTPException, Query
import requests
import json


router = APIRouter()

@router.get("/loadmore")
def loadmore(page: int = Query(2, ge=1)):
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"}

    params = {
        "language": "en-US",
         "page": page,
    }
    try:
        response = requests.get(url, headers=headers, params=params)
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
