import requests
import random
import time
from faker import Faker

fake = Faker()

BASE_URL = "http://localhost:3000"  # 🔁 Update with your API base
CREATE_SERVICE_ENDPOINT = "/services"   # 🔁 Update this if needed

def generate_service(company_id):
    return {
        "name": fake.bs().title(),
        "comment": fake.sentence(),
        "company_id": company_id,
        "service_category_id": random.randint(1, 8),
        "operations": random.sample(range(1, 7), k=random.randint(1, 3))  # 1 to 3 ops
    }

def create_services_for_company(company_id, count=40):
    for i in range(count):
        service = generate_service(company_id)
        try:
            response = requests.post(f"{BASE_URL}{CREATE_SERVICE_ENDPOINT}", json=service)
            print(f"  ↳ Service {i+1} for Company {company_id} → {response.status_code}")
            time.sleep(0.1)
        except Exception as e:
            print(f"❌ Failed to create service for company {company_id}: {e}")

def main():
    print("🚀 Creating 40 services for each company (ID 1 to 20)...")

    for company_id in range(1, 21):
        print(f"\n🏢 Company ID {company_id}:")
        create_services_for_company(company_id, 40)

    print("\n✅ All services created.")

if __name__ == "__main__":
    main()

