# Project 4: Titanic Passenger Data, Lists, Subsetting and Categoricals in pandas

**Course:** TDM 102

## Overview
Introductory pandas data wrangling using the Titanic passenger dataset, covering Python lists vs pandas Series, boolean subsetting, recoding survival into categorical labels, and grouping passengers into age brackets.

## Techniques
- Converting DataFrame columns to plain Python lists and comparing types
- Boolean indexing and combined filter conditions
- `pd.Categorical` for recoding numeric survival codes into labels
- String concatenation across columns
- Manual age bucketing and `pd.crosstab()`

## Key Finding
Recoded survival status into readable categories combined with sex, then grouped passengers into age brackets (Children, Young, Adult, Old) and cross tabulated age group against the combined survival and sex status.

## Data
- `titanic.csv`: small, safe to include in `data/`
