import pandas as pd
import sqlite3 as sq
from config import DB_PATH

conn = sq.connect(DB_PATH)
cursor = conn.cursor()

user_input = input("What movie did you enjoy recently: ")
recommendations = "You might also like: "

def find_movie_ID () -> int:
    movie_ID_query = f"SELECT movieId FROM movies WHERE title LIKE '%{user_input}%'"
    movie_ID = pd.read_sql(movie_ID_query, conn) #contains sequels and similar titles
    return movie_ID.loc[0, 'movieId']  # This gets the actual integer value

def find_similar_ID () -> str:
    result = ""
    movie_ID_query = f"SELECT title FROM movies WHERE movieId IN (SELECT movieId FROM movies WHERE title LIKE '%{user_input}%')"
    movie_titles = pd.read_sql(movie_ID_query, conn) #contains sequels and similar titles
    for i in movie_titles.index:
        result += movie_titles.loc[i, "title"] + "\n"
    return result


movie_id = find_movie_ID()  # Call once and store

movies_query = f"""
SELECT movies.title, movies.movieId, AVG(ratings.rating) as avg_rating, COUNT(*) as num_ratings 
FROM ratings 
JOIN movies ON ratings.movieId = movies.movieId
WHERE ratings.userId IN (
    SELECT userId FROM ratings 
    WHERE movieId = {movie_id} AND rating >= 4) 
AND ratings.rating >= 4 
AND ratings.movieId != {movie_id}
GROUP BY ratings.movieId
ORDER BY avg_rating DESC 
LIMIT 10
"""

recommendations = "Movies matching your search:\n"
recommendations += find_similar_ID()
recommendations += "\nBecause you enjoyed these, you might also like:\n"
recommendations_df = pd.read_sql(movies_query, conn)

for i in recommendations_df.index:
    recommendations += recommendations_df.loc[i, "title"] + "\n"

print(recommendations)

"""1. User inputs movie name
2. algorithm finds users that have rated the movie highly (4+ stars)
3. Then checks: What other movies did the users rate highly?
4. Returns: Those movies as recommendations"""