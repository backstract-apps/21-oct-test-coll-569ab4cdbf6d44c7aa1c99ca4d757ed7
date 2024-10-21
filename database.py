from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+psycopg2://postgres.nbtfextgppziibcbgspm:Lakshaysingh@123@aws-0-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=True'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
