import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:toor@localhost/online_movie_rating"
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))

    def __repr__(self):
        return self.title


movies = session.query(Movie).filter(Movie.title == "Dude where is my car?").all()

print(movies)
