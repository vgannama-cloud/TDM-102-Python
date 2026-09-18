# Project 6: Flights and Ice Cream Ratings, Grouped Aggregation in pandas

**Course:** TDM 102

## Overview
Grouped aggregation and value binning in pandas across flight and ice cream ratings datasets, computing average airtime between specific routes, binning ratings into descriptive tiers, and bucketing flight times into parts of the day.

## Techniques
- `groupby()` aggregation combined with filtering to specific routes
- Quantile-based binning (`pd.qcut`) and manual binning (`pd.cut`)
- Two dimensional `groupby().unstack()` tables
- Finding the most frequent category (`idxmax`)

## Key Finding
Found average flight airtime between specific origin-destination pairs, binned ice cream ratings into descriptive tiers, and identified the busiest time-of-day window for both departures and arrivals in the 1997 flight data.

## Data
- `2006.csv`, `1997.csv` (flights): not included, large, from the ASA Data Expo 2009 dataset
- `products.csv` (ice cream ratings): small, safe to include in `data/`
