from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
#from database import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3
import pandas
from pandas import read_csv, DataFrame
import os
from dotenv import load_dotenv


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine('sqlite://', echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = sqlite3.connect('Spotify.db')
dataframe = pandas.read_csv("spotify_music.csv", sep=',')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS spotify')
dataframe.to_sql('spotify', con=conn)

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS spotify(
    album text,
    track_number int,
    id varchar(30),
    name text,
    uri varchar(30),
    loudness float,
    speechiness float,
    tempo float,
    valence float,
    popularity int)
    """)
conn.commit()



class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True, index=True)
    Artist = Column(String(255), index=True)
    Songs = Column(String)
    Albums = Column(String)

