import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "outputs" / "cleaned_data" / "airbnb_cleaned.csv"
db_path = BASE_DIR / "outputs" / "airbnb.db"

df = pd.read_csv(csv_path)
conn = sqlite3.connect(db_path)
df.to_sql("airbnb", conn, if_exists="replace", index=False)

print(f"SQLite database created: {db_path}")
print(f"Rows loaded: {len(df):,}")
conn.close()