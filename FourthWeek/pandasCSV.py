from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name('world_cup_2026_matches.csv')
df = pd.read_csv(csv_path)
new_df = df.dropna()
print(new_df)
print(new_df.head(10))
print(new_df.tail(10))
print(new_df.info())