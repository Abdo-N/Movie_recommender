"""
Central place for file paths used across the project.

Paths are computed relative to the project root, so the scripts work
regardless of where the repo is cloned to or which OS you're on.
"""

import os

# scripts/config.py -> project root is one level up
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(PROJECT_ROOT, "Data_sets")
DB_DIR = os.path.join(PROJECT_ROOT, "Databases")

MOVIES_CSV = os.path.join(DATA_DIR, "movies.csv")
RATINGS_CSV = os.path.join(DATA_DIR, "ratings.csv")
TAGS_CSV = os.path.join(DATA_DIR, "tags.csv")

DB_PATH = os.path.join(DB_DIR, "Movies.db")

# Make sure the Databases folder exists before anything tries to write to it
os.makedirs(DB_DIR, exist_ok=True)
