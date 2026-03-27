import random
import time
import csv

def generate_data():
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "value"])

        while True:
            value = random.randint(10, 100)

            # Inject anomaly
            if random.random() < 0.05:
                value = random.randint(150, 300)

            writer.writerow([time.time(), value])
            file.flush()

            time.sleep(1)

if __name__ == "__main__":
    generate_data()