# Movie Recommender System 🎬

A small project built to practice **pandas, SQL, and git** by putting together a movie recommendation system on top of the MovieLens dataset.

## How it works

1. **Load & explore** — `checking_data.py` loads the raw MovieLens CSVs with pandas, checks for nulls/duplicates, and explores the data: highest-rated movies, most active users, genre distribution, and the correlation between release year and rating.
2. **Build the database** — `schema.py` creates a SQLite database with `movies`, `ratings`, `users`, and `tags` tables, then loads the cleaned CSVs into it (extracting release year out of the movie title along the way, and pre-computing each user's rating count/average).
3. **Recommend** — `Main.py` is the actual recommender: it asks for a movie you liked, then queries the database for the recommendation logic below.

## Recommendation logic

1. You type in a movie title (partial matches work — typing "Toy Story" will catch all the sequels too).
2. The script finds every user who rated that movie **4 stars or higher**.
3. It looks at what *else* those users rated 4+ stars.
4. It returns the top 10 of those movies, ranked by average rating, as your recommendations.

In short: people who liked this also liked these.

## Dataset

Built on the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/) from GroupLens Research — about 100,000 ratings across thousands of movies. The raw CSVs and the generated SQLite database aren't included in this repo (see `.gitignore`); download the dataset yourself to run it.

## Running it

1. Download the MovieLens 100K dataset and place `movies.csv`, `ratings.csv`, and `tags.csv` somewhere accessible.
2. Update the file paths in `schema.py` (and `checking_data.py`, if you want the EDA too) to point to your dataset and where you want the SQLite database created — they're currently hardcoded to a local path.
3. Run the schema script once to build the database:
   ```bash
   python scripts/schema.py
   ```
4. Get recommendations:
   ```bash
   python scripts/Main.py
   ```
   ```
   What movie did you enjoy recently: Toy Story
   Movies matching your search:
   Toy Story (1995)
   Toy Story 2 (1999)
   ...
   Because you enjoyed these, you might also like:
   ...
   ```

## What's next

- Parameterize file paths (config file or CLI args) instead of hardcoded paths
- Move the recommendation query into a proper `.sql` file rather than an f-string
- Weight recommendations by number of ratings, not just average rating, to avoid niche movies with one 5-star rating outranking genuinely popular ones
