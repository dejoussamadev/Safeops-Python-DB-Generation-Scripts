import requests
import random
import time
from faker import Faker

fake = Faker()

BASE_URL = "http://localhost:3000/auth"  # ✅ Replace with your API URL
REGISTER_ENDPOINT = "/register"
password = "Hassen1234!"

def generate_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = fake.user_name()
    email = fake.unique.email()
    company = fake.company()

    return {
        "companyName": company,
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "username": username,
        "password": password,
        "confirmPassword": password,
        "country_id": random.randint(1, 249),
        "timezone_id": random.randint(1, 424),
	"role": "ADMIN"
    }

def create_users(count=20):
    for i in range(count):
        user = generate_user()
        response = requests.post(f"{BASE_URL}{REGISTER_ENDPOINT}", json=user)
        print(f"[{i+1}] {user['email']} → {response.status_code} | {response.text}")
        time.sleep(0.2)

if __name__ == "__main__":
    print("👤 Creating 20 users with real-looking data...")
    create_users(20)
    print("✅ Done.")
