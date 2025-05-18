# fill_stations.py

import requests
import random

API_URL = "http://localhost:3000/stations"
COMPANY_ID_RANGE = range(1, 21)  # 1 to 20
AIRPORT_ID_RANGE = range(1, 1001)  # 1 to 1000


BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0YmFyYmFyYSIsImNvbXBhbnkiOnsiaWQiOjEsIm5hbWUiOiJXYWx0ZXJzLCBIb2JicyBhbmQgQ2FzdGlsbG8iLCJwaWN0dXJlIjoiIn0sImVtYWlsIjoibXVycmF5YW5kcmV3QGV4YW1wbGUuY29tIiwic3ViIjoxLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDc0MDQ2MTEsImV4cCI6MTc0NzQwODIxMX0.FbH3xpaC_VKvXRTWdm1ivBHlKvWeXIUYIZDw36RxLig"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

def generate_station_data(company_id, used_airports):
    while True:
        airport_id = random.randint(1, 1000)
        if airport_id not in used_airports:
            used_airports.add(airport_id)
            return {
                "company_id": company_id,
                "airport_id": airport_id
            }

def main():
    for company_id in COMPANY_ID_RANGE:
        num_stations = random.randint(4, 6)
        used_airports = set()
        print(f"Creating {num_stations} stations for company {company_id}")
        
        for _ in range(num_stations):
            data = generate_station_data(company_id, used_airports)
            response = requests.post(API_URL, json=data, headers=HEADERS)
            if response.status_code == 201:
                print(f"✔ Station created: {data}")
            else:
                print(f"✖ Failed to create station: {data} | Status: {response.status_code} | Response: {response.text}")

if __name__ == "__main__":
    main()
