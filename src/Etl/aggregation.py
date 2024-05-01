import os

import pandas as pd
from crate import client
from dotenv import load_dotenv

load_dotenv()


def fetch_data():
    # Connect to CrateDB
    connection = client.connect(os.getenv("HOST_CRATE"), username="crate", password=None, timeout=10)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM etwaterquality LIMIT 10")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        connection.close()


data_fetched = fetch_data()
df_buoy = pd.DataFrame(data_fetched)
print(df_buoy.head())
