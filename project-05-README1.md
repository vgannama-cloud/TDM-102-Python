# Project 5: pandas vs Polars, Flight and Baseball Data

**Course:** TDM 102

## Overview
Comparing `pandas` and `polars` for reading and filtering large datasets, timing CSV load speed on flight and baseball records, then using polars regex-based column selection to explore flight delay fields.

## Techniques
- Timing `read_csv` performance (`time` module) between pandas and polars
- Column selection and filtering in both libraries side by side
- Polars regex column selection (`pl.col("^pattern$")`)
- Type casting and derived columns in polars (`with_columns`)

## Key Finding
Benchmarked pandas against polars on large flight and baseball CSVs, filtered Indianapolis-origin flights, and used regex column selection to isolate delay-related fields before computing an absolute arrival time difference.

## Data
- `1987.csv`, `2005.csv` (flights), `AllstarFull.csv` (Lahman baseball): flight files not included, large, from the ASA Data Expo 2009 dataset; baseball file safe to include if small
