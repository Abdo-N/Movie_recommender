import pandas as pd
import sqlite3 as sq

conn = sq.connect("D:/Repos/Movie_recommender/Databases/Movies.db")
cursor = conn.cursor()

statement = pd.read_sql_query(open('D:/Repos/Movie_recommender/SQL/Qeury.SQL').read(), conn)
print(statement.to_string())
