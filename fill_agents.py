import requests
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

BASE_URL = "http://localhost:8000/api"  # ✅ Change this
CREATE_AGENT_ENDPOINT = "/agents"       # ✅ Change to your actual endpoint

PASSWORD = "Agent2025!Secure"

def generate_agent_data():
    birth_date = fake.date_of_birth(minimum_age=22, maximum_age=45)
    expiry_date = (datetime.now() + timedelta(days=365 * 5 + random.randint(0, 730))).date()

    gender = random.choice(["MALE", "FEMALE"])

    first_name = fake.first_name_female() if gender == "FEMALE" else fake.first_name_male()
    last_name = fake.last_name()

    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    username = f"{first_name.lower()}{random.randint(10, 999)}"

    return {
        "companyId": str(random.randint(1, 10)),
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "username": username,
        "password": PASSWORD,
        "confirmPassword": PASSWORD,
        "country_id": str(random.randint(1, 249)),
        "timezone_id": str(random.randint(1, 424)),
        "dateBirth": birth_date.isoformat(),
        "gender": gender,
        "expired_at": expiry_date.isoformat()
    }

def create_agent(agent_data):
    response = requests.post(
        f"{BASE_URL}{CREATE_AGENT_ENDPOINT}",
        files=agent_data
    )
    print(f"🧑 Created {agent_data['username']} → Status: {response.status_code}")

def main():
    count = 20  # Change if you want more or fewer agents
    for _ in range(count):
        data = generate_agent_data()
        # Convert to (key, value) pairs for multipart/form-data
        form_data = {key: (None, value) for key, value in data.items()}
        create_agent(form_data)

    print("✅ All agents created.")

if __name__ == "__main__":
    main()
