import os

from crate import client
from dotenv import load_dotenv

load_dotenv()

# Connect to CrateDB
connection = client.connect(os.getenv("HOST_CRATE"), username="crate", password=None, timeout=10)
cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM etwaterquality LIMIT 10")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("An error occurred:", e)
finally:
    cursor.close()
    connection.close()
