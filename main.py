from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes.trending import router as trending
from routes.actors import router as actors
from routes.moviesBypreferences import router as moviePreference
from routes.movieDetails import router as movieDetails
from routes.recommendation import router as recommend
from routes.alreadyWatchedMovies import router as alreadywatched
from routes.loadmoreTrending import router as loadmore
from routes.loadmorePreferences import router as loadmorePref

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js default dev server
        "http://127.0.0.1:3000",
        "https://your-production-domain.com"  # Add your production domain when applicable
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.include_router(trending, prefix="/api/v1", tags=["trending"])
app.include_router(actors, prefix="/api/v1", tags=["actors"])
app.include_router(moviePreference, prefix="/api/v1", tags=["moviePreference"])
app.include_router(movieDetails, prefix="/api/v1", tags=["movieDetails"])
app.include_router(recommend,prefix="/api/v1", tags=["recommend"])
app.include_router(alreadywatched,prefix="/api/v1", tags=["alreadywatched"])
app.include_router(loadmore,prefix="/api/v1", tags=["loadmore"])
app.include_router(loadmorePref,prefix="/api/v1", tags=["loadmorePref"])
