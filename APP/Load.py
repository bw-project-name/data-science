import csv
import datetime


import model
from Database import SessionLocal, engine

db = SessionLocal()

model.Base.metadata.create_all(bind=engine)

with open("spotify_music.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = model.Spotify(
            track_number=row["track_number"],
            album=row["album"],
            acousticness=row["acousticness"],
            danceability=row["danceability"],
            energy=row["energy"],
            instrumentalness=row["instrumentalness"],
            speechiness=row["speechiness"],
            tempo=row["tempo"],
            popularity=row["popularity"],
            liveness=row["liveness"],
            loudness=row["loudness"],
            valence=row["valence"],
            uri=row["uri"],
            name=row["name"],
            id=row["id"]
        )
        db.add(db_record)
    db.commit()
db.close()

    