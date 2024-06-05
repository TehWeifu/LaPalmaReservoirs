import pandas as pd
from crate import client


def fetch_data() -> list:
    connection = client.connect('http://crate.lapalma.fpmislata.es', username="crate", password=None, timeout=10,
                                schema='mtopeniot')
    cursor = connection.cursor()

    query = ("SELECT "
             "entity_id, temperature, ph, turbidity, conductivity, nivel_agua, dateobserved, location_centroid "
             "FROM etcalidadagua")

    try:
        cursor.execute(query)
        # Fetch all with column names
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        connection.close()


def load_to_csv(aggregated_data: pd.DataFrame):
    aggregated_data.to_csv("./crate-dump.csv", index=False)


data_fetched = fetch_data()

df_buoy = pd.DataFrame(
    data_fetched,
    columns=["entity_id", "temperature", "ph", "turbidity", "conductivity", "nivel_agua", "dateobserved",
             "location_centroid"]
)

df_buoy["dateobserved"] = pd.to_datetime(df_buoy["dateobserved"], unit="ms")
df_buoy['latitude'] = df_buoy['location_centroid'].apply(lambda x: x[0] if x is not None else None)
df_buoy['longitude'] = df_buoy['location_centroid'].apply(lambda x: x[1] if x is not None else None)
df_buoy.drop(columns=["location_centroid"], inplace=True)

load_to_csv(df_buoy)
