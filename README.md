# Airbnb NYC Market Analysis — Python + SQL + Power BI

## What this project does

This project analyzes the Airbnb NYC 2019 dataset using:
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL/SQLite
- Power BI (optional dashboard layer)

## 1. Where to put the dataset

Download `AB_NYC_2019.csv` and put it exactly here:

```text
airbnb_nyc_market_analysis/
└── data/
    └── AB_NYC_2019.csv
```

The CSV is intentionally not included in this starter project.

## 2. Install libraries

Open a terminal in the project folder:

```bash
pip install -r requirements.txt
```

## 3. Run the notebook

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/Airbnb_EDA_Complete.ipynb
```

Run cells from top to bottom.

## 4. Or run the Python script

From the project root:

```bash
python src/airbnb_analysis.py
```

## 5. Generated files

The analysis creates:

```text
outputs/
├── charts/
│   ├── listings_by_borough.png
│   ├── room_type_distribution.png
│   ├── average_price_by_borough.png
│   ├── median_price_borough_room_type.png
│   ├── top_neighbourhoods.png
│   ├── price_distribution.png
│   ├── price_boxplot.png
│   ├── price_vs_reviews.png
│   ├── geographic_distribution.png
│   ├── availability_by_room_type.png
│   └── minimum_nights.png
└── cleaned_data/
    ├── airbnb_cleaned.csv
    ├── avg_price_by_borough.csv
    ├── median_price_by_borough_room_type.csv
    └── host_summary.csv
```

## 6. SQL

See `sql/analysis.sql`.

For SQLite, load the cleaned CSV or original CSV into a table named `airbnb`, then run the queries.

## 7. Power BI

Open Power BI Desktop and import:
- `outputs/cleaned_data/airbnb_cleaned.csv`
- or the summary CSVs in `outputs/cleaned_data/`

Suggested dashboard:
1. KPI cards — listings, hosts, average price, median price
2. Listings by borough
3. Average/median price by borough
4. Room type distribution
5. Top neighborhoods
6. Price band distribution
7. Geographic map using latitude/longitude
8. Availability by room type

## Important analytical limitation

`availability_365` means days a listing was available in the dataset's availability field. It is NOT the same as booked nights or occupancy rate. Do not present it as actual occupancy unless you introduce additional booking data and explain your assumptions.

Also, correlation between price and reviews does not establish causation.