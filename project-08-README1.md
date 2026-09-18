# Project 8: Taylor Swift Discography and YouTube Channels, Custom Functions in pandas

**Course:** TDM 102

## Overview
Writing reusable custom functions in pandas applied to a Taylor Swift discography dataset and a top YouTube channels dataset, covering duration conversion, album classification, and cleaning malformed numeric strings.

## Techniques
- Custom functions to filter by energy threshold and by album name
- Nested and nested-classification functions using nested `if`/`elif`
- Cleaning numeric strings with stray commas (`str.replace`, `pd.to_numeric`)
- Finding the top row within a group (`idxmax`)

## Key Finding
Built a reusable function to classify albums as short, medium, or long by total duration, and a function to find the top YouTuber by subscriber count within a given genre, applied to Gaming and Music categories.

## Data
- `taylor_swift_discography_updated.csv`, `most_subscribed_youtube_channels.csv`: small, safe to include in `data/`
