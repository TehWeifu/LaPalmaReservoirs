import pandas as pd

df = pd.read_csv("./crate-raw.csv", index_col="dateobserved", parse_dates=True)

df['temperature'] = df['temperature'].clip(0, 100)

# Extract the series of entity ids and drop
series_entity_ids = df['entity_id']
df.drop(columns='entity_id', inplace=True)

df = df.resample('h').mean()
df = df.interpolate()

print(df)
