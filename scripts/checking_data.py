import pandas as pd

movies = pd.read_csv('D:/Repos/Movie_recommender/Data_sets/movies.csv') #moveID, title, genres
ratings = pd.read_csv('D:/Repos/Movie_recommender/Data_sets/ratings.csv') #userID, movieID, rating, timestamp
tags = pd.read_csv('D:/Repos/Movie_recommender/Data_sets/tags.csv') #userID, moveID, tag, timestamp

#print(movies.head())
#print(tags.info())
#print(ratings.info())

#No duplicates
#No null values (but some have no genres and no tags or ratings)


#Finding the highest-rated movies 
avg_ratings = ratings.groupby('movieId').agg({
    'rating': ['mean', 'count']
}).reset_index()
avg_ratings.columns = ['movieId', 'avg_rating', 'num_ratings']
movies_with_ratings = movies.merge(avg_ratings, on='movieId')
popular_movies = movies_with_ratings[movies_with_ratings['num_ratings'] >= 50]
top_movies = popular_movies.sort_values('avg_rating', ascending=False)

#Finding most active users
user_ratings = ratings.groupby('userId')['rating'].agg(['count','mean'])
user_ratings.columns = ['number of ratings','avg rating']
user_ratings = user_ratings[user_ratings['number of ratings'] >= 100]
user_ratings = user_ratings.sort_values('number of ratings', ascending=False)

#Exploring genre distribution
genres = []
for genre_string in movies['genres']:
    genres.extend(genre_string.split('|'))

from collections import Counter

genre_counts = Counter(genres)
genre_df = pd.DataFrame(genre_counts.items(), columns=['genre', 'count'])

#extracting year from title
movies['year'] = movies['title'].str.extract(r'(\d{4})')
movies['year'] = pd.to_numeric(movies['year'])
#print(movies[['title', 'year','genres']].head(20))

#correlation between year and rating
movies_with_ratings = movies.merge(avg_ratings, on='movieId')
#print(movies_with_ratings[['year', 'avg_rating']].corr())

#what data looks like now
print(movies.head())
print(ratings.head())
