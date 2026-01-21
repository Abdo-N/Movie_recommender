import pandas as pd
import sqlite3 as sq

conn = sq.connect("D:/Repos/Movie_recommender/Databases/Movies.db")
cursor = conn.cursor()

user_input = input("What movie have you enjoyed recently: ")
#statement = pd.read_sql_query(open('D:/Repos/Movie_recommender/SQL/Qeury.SQL').read(), conn)

def find_movie_ID () -> int:
    movie_ID_query = f"SELECT movieId FROM movies WHERE title LIKE '%{user_input}%'"
    movie_ID = pd.read_sql(movie_ID_query, conn) #contains sequels and similar titles
    return movie_ID.loc[0, 'movieId']  # This gets the actual integer value

def find_users ()
users_query = f"""SELECT movie-recommendations
                FROM ratings
                WHERE userId IN (
                -- subquery: users who liked the input movie
                SELECT userId 
                FROM ratings 
                WHERE movieId = {find_movie_ID} AND rating >= 4) AND rating >= 4"""
    


print(find_movie_ID())
print(find_users())

"""1. User inputs movie name
2. algorithm finds users that have rated the movie highly (4+ stars)
3. Then checks: What other movies did the users rate highly?
4. Returns: Those movies as recommendations"""