import sqlite3 as sq

#Movies table: movieId, title, year, genres
#Ratings table: userId, movieId, rating
#Users table: userId, avg_rating, num_ratings

# One connection for all tables
conn = sq.connect("D:/Repos/Movie_recommender/Databases/Movies.db")
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
movies = pd.read_csv('D:/Repos/Movie_recommender/Data_sets/movies.csv')
ratings = pd.read_csv('D:/Repos/Movie_recommender/Data_sets/ratings.csv')
tags = pd.read_csv('D:/Repos/Movie_recommender/Data_sets/tags.csv')

# Extract year if you haven't already
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)')
movies['year'] = pd.to_numeric(movies['year'])

# Now insert into database
conn = sq.connect("D:/Repos/Movie_recommender/Databases/Movies.db")
movies.to_sql('movies', conn, if_exists='replace', index=False)

ratings = ratings.drop('timestamp', axis = 1)
conn = sq.connect("D:/Repos/Movie_recommender/Databases/Movies.db")
ratings.to_sql('ratings', conn, if_exists='replace', index=False)

tags = tags.drop('timestamp', axis = 1)
conn = sq.connect("D:/Repos/Movie_recommender/Databases/Movies.db")
tags.to_sql('tags', conn, if_exists='replace', index=False)

users = ratings.groupby('userId')['rating'].agg(['count','mean'])
users.columns = ['num_ratings','avg_ratings']
users.to_sql('users', conn, if_exists='replace', index=False)

conn.close()