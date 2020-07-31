import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgres://jnylyxpa:ShMf82A3cMtTc6SaKSgN3Vqpr_Mytz_3@ruby.db.elephantsql.com:5432/jnylyxpa"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()