import requests
import random
import time
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# 🔧 Configuration
BASE_URL = "http://localhost:3000"
CREATE_AGENT_ENDPOINT = "/users"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0YmFyYmFyYSIsImNvbXBhbnkiOnsiaWQiOjEsIm5hbWUiOiJXYWx0ZXJzLCBIb2JicyBhbmQgQ2FzdGlsbG8iLCJwaWN0dXJlIjoiIn0sImVtYWlsIjoibXVycmF5YW5kcmV3QGV4YW1wbGUuY29tIiwic3ViIjoxLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDcwNjkxODIsImV4cCI6MTc0NzA3Mjc4Mn0.T1QUcZEOuhkWosxh4OXe_p3Ro2By1brOLFLdcuZw3F0"  # 🔐 Replace with your actual token
PASSWORD = "Agent1234!"    # Shared password for all agents

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

def generate_agent_data(company_id):
    birth_date = fake.date_of_birth(minimum_age=22, maximum_age=45)
    expiry_date = (datetime.now() + timedelta(days=365 * 5 + random.randint(0, 730))).date()

    gender = random.choice(["MALE", "FEMALE"])
    first_name = fake.first_name_female() if gender == "FEMALE" else fake.first_name_male()
    last_name = fake.last_name()

    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    username = f"{first_name.lower()}{random.randint(1000, 9999)}"

    return {
        "companyId": str(company_id),
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "username": username,
        "password": PASSWORD,
        "confirmPassword": PASSWORD,
        "country_id": str(random.randint(1, 249)),
        "timezone_id": str(random.randint(1, 424)),
        "date_birth": birth_date.isoformat(),
        "gender": gender,
        "expired_at": expiry_date.isoformat()
    }

def create_agent(agent_data):
    response = requests.post(
        f"{BASE_URL}{CREATE_AGENT_ENDPOINT}",
        files={k: (None, v) for k, v in agent_data.items()},
        headers=HEADERS
    )
    print(f"👤 Created {agent_data['username']} → Status: {response.status_code}")

def main():
    total = 0
    for company_id in range(1, 21):  # Company IDs 1 to 20
        agent_count = random.randint(120, 200)
        print(f"\n🏢 Creating {agent_count} agents for Company {company_id}...")
        for _ in range(agent_count):
            data = generate_agent_data(company_id)
            create_agent(data)
            total += 1
            time.sleep(0.05)  # ⏱️ Optional delay
    print(f"\n✅ Done! Created {total} agents total.")

if __name__ == "__main__":
    main()
