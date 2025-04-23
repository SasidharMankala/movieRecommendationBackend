from fastapi import APIRouter, HTTPException
import requests
import json


router = APIRouter()

@router.get("/recommend/{movieID}")
def recommend(movieID: int):
    url = f"https://api.themoviedb.org/3/movie/{movieID}/recommendations?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"
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
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
