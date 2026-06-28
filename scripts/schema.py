import sqlite3 as sq
from config import DB_PATH, MOVIES_CSV, RATINGS_CSV, TAGS_CSV

#Movies table: movieId, title, year, genres
#Ratings table: userId, movieId, rating
#Users table: userId, avg_rating, num_ratings

# One connection for all tables
conn = sq.connect(DB_PATH)
cursor = conn.cursor()

# Create movies table with data types and primary key
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT,
    year INTEGER,
    genres TEXT
)
""")

# Create ratings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL
)
""")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    userId INTEGER PRIMARY KEY,
    avg_rating REAL,
    num_ratings INTEGER
)
""")

conn.commit()  # Save the changes

import pandas as pd
# Load data from CSVs
movies = pd.read_csv(MOVIES_CSV)
ratings = pd.read_csv(RATINGS_CSV)
tags = pd.read_csv(TAGS_CSV)

# Extract year if you haven't already
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)')
movies['year'] = pd.to_numeric(movies['year'])

# Now insert into database
conn = sq.connect(DB_PATH)
movies.to_sql('movies', conn, if_exists='replace', index=False)

ratings = ratings.drop('timestamp', axis = 1)
conn = sq.connect(DB_PATH)
ratings.to_sql('ratings', conn, if_exists='replace', index=False)

tags = tags.drop('timestamp', axis = 1)
conn = sq.connect(DB_PATH)
tags.to_sql('tags', conn, if_exists='replace', index=False)

users = ratings.groupby('userId')['rating'].agg(['count','mean'])
users.columns = ['num_ratings','avg_ratings']
users.to_sql('users', conn, if_exists='replace', index=False)

conn.close()