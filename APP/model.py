from sqlalchemy import Column, Integer, String  
from sqlalchemy.types import Date, Float 
from Database import Base 



class Spotify(Base):
    __tablename__ = "Spotify"

    index = Column(Integer, primary_key=True, index=True)
    track_number = Column(String)
    album = Column(String)
    acousticness = Column(Float)
    danceability = Column(Float)
    energy = Column(Float)
    instrumentalness = Column(Float)
    speechiness = Column(Float)
    tempo = Column(Float)
    popularity = Column(Integer)
    liveness = Column(Float)
    loudness = Column(Float)
    valence = Column(Float)
    uri = Column(String(255), index = True)
    name = Column(String(255), index = True)
    id = Column(String(255), index = True)


