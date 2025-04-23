import requests

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&with_genres=28,16,35"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTYwMzg1ZGIyM2QyZDgwNzQ1OTQyYjVmNzhjYWU0NCIsIm5iZiI6MTc0NDA2NzA5NC43MTgwMDAyLCJzdWIiOiI2N2Y0NWExNmUxZDVjMjNjNmVkOTljYjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Gdjnpa_sBv59ZawY1mglwIXPHI287hhzOWc4FjPTRUw"
}

response = requests.get(url, headers=headers)

print(response.text)