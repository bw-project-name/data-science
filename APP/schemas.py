from pydantic import BaseModel



class Spotify(BaseModel):
    album: str
    track_number: int 
    id: str
    name: str
    acousticness: float
    danceability: float
    energy: float
    instrumentalness: float
    loudness: float
    liveness: float
    speechiness: float
    tempo: float
    valence: float
    popularity: int
    uri: str


    

    class Config:
        orm_mode = True