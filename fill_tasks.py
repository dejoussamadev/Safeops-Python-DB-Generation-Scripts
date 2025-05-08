import requests
import random
import time
from faker import Faker

fake = Faker()

BASE_URL = "http://localhost:3000"
CREATE_TASK_ENDPOINT = "/tasks"

def generate_task(service_id, service_category_id):
    return {
        "name": fake.catch_phrase(),
        "description": fake.sentence(),
        "recurrence": random.choice(["ONCE", "MANY"]),
        "task_type_id": random.randint(1, 6),
        "ground_operations": random.sample(range(1, 21), k=random.randint(1, 4)),
        "operation_id": random.randint(1, 6),
        "service_id": service_id,
        "service_category_id": service_category_id
    }

def create_tasks_for_service(service_id, service_category_id, count=4):
    for i in range(count):
        task = generate_task(service_id, service_category_id)
        try:
            response = requests.post(f"{BASE_URL}{CREATE_TASK_ENDPOINT}", json=task)
            print(f"  ↳ Task {i+1} for Service {service_id} → {response.status_code}")
        except Exception as e:
            print(f"❌ Error creating task for Service {service_id}: {e}")
        time.sleep(0.05)

def main():
    print(f"🛠️ Generating 4 tasks for each of 800 services...")

    for service_id in range(1, 801):  # service IDs from 1 to 800
        # You can either randomly assign a category or use a predictable pattern
        service_category_id = random.randint(1, 8)
        print(f"🔧 Service ID {service_id}:")
        create_tasks_for_service(service_id, service_category_id)

    print("✅ Done creating all tasks.")

if __name__ == "__main__":
    main()