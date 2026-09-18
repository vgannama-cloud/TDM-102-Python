# Project 3: Video Games and Google Play Store, Grouped Aggregation

**Course:** TDM 102

## Overview
Grouped aggregation and data cleaning in pandas across a video game sales dataset and a Google Play Store apps dataset, computing average scores by genre, cleaning malformed numeric columns, and deriving a rating-per-review metric.

## Techniques
- `groupby()` with mean, sum, and count aggregations
- Deriving boolean columns from thresholds
- Cleaning numeric strings with stray characters (`str.replace`, `astype`)
- Standardizing category labels (`str.upper`)

## Key Finding
Found average critic score by genre and total sales by console, then cleaned the Google Play Store review counts (removing malformed entries) to compute a rating-per-review ratio for each app.

## Data
- `vgchartz-2024.csv`, `googleplaystore.csv`: check file sizes before including
