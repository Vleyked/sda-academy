from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base

USER = "root"
PASSWORD = "root"
HOST = "localhost"
DB = "store"

# Step 1: Create the database engine
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DB}")

# Step 2: Define the database models
Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"

    director_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    surname = Column(String(255))
    rating = Column(Float(3, 1))


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    year = Column(Integer)
    category = Column(String(255))
    director_id = Column(Integer, ForeignKey("directors.director_id"))
    rating = Column(Float(3, 1))


# Step 3: Drop the tables if they exist
Base.metadata.drop_all(engine)

# Step 4: Create the database tables
Base.metadata.create_all(engine)

# Step 5: Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Step 6: Perform database operations
# Inserting records
director1 = Director(name="Christopher", surname="Nolan", rating=9.5)
director2 = Director(name="Quentin", surname="Tarantino", rating=9.7)
director3 = Director(name="Martin", surname="Scorsese", rating=8.7)
session.add_all([director1, director2, director3])
session.commit()

movie1 = Movie(
    title="Inception", year=2010, category="Sci-Fi", director_id=1, rating=8.8
)
movie2 = Movie(
    title="Pulp Fiction", year=1994, category="Crime", director_id=2, rating=8.9
)
movie3 = Movie(
    title="The Departed", year=2006, category="Crime", director_id=3, rating=8.5
)
session.add_all([movie1, movie2, movie3])
session.commit()

# Querying records
directors = session.query(Director).all()
for director in directors:
    print(f"Director: {director.name} {director.surname}, Rating: {director.rating}")

movies = session.query(Movie).all()
for movie in movies:
    print(
        f"Movie: {movie.title}, Year: {movie.year}, Category: {movie.category}, Rating: {movie.rating}"
    )

# Step 7: Close the session
session.close()
