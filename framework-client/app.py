import requests
import time
import random

def call_adapter():
    count = 0
    while True:
        query = f"get_items_batch_{count}"
        print(f"[framework-client] Sending: {query}")
        try:
            response = requests.post(
                "http://adapter-service:5000/read",
                json={"query": query}
            )
            print(f"[framework-client] Response: {response.json()}")
        except Exception as e:
            print(f"[framework-client] Error: {e}")
        count += 1
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    # Delay to ensure adapter-service is up
    time.sleep(3)
    call_adapter()