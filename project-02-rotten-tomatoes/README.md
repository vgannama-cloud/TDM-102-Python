# Project 2: Rotten Tomatoes Movie Ratings in pandas

**Course:** TDM 102

## Overview
Exploratory analysis of a Rotten Tomatoes movie dataset in pandas, covering rating distribution, director and studio counts, genre matching, cleaning inconsistent rating labels, and cross tabulating rating against critical reception.

## Techniques
- `value_counts()` and line plots of category distributions
- Genre substring matching (`str.contains`)
- Fixing malformed category labels (`.loc` assignment)
- `pd.crosstab()` for rating vs tomatometer status
- Looking up specific rows by title

## Key Finding
Cleaned inconsistent rating labels, then cross tabulated MPAA rating against Tomatometer status to see how rating relates to critical reception, and looked up individual well known movies for comparison.

## Data
- `rotten_tomatoes_movies.csv`: a few MB, safe to include in `data/`
