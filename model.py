import random
import time
import csv
import os

FILE = "data.csv"

def generate_data():
    # Create file with header if not exists
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "value"])

    while True:
        value = random.randint(20, 80)

        # Inject anomaly
        if random.random() < 0.05:
            value = random.randint(150, 300)

        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.time(), value])

        time.sleep(1)

if __name__ == "__main__":
    generate_data()