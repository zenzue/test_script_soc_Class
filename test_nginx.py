import requests
import concurrent.futures

url = input("Enter your server: ")

concurrent_requests = 10
total_requests = 100

def send_request(url):
    try:
        respond = requests.get(url)
        return respond.status_code
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(f"Sending {total_requests} requests to {url} with {concurrent_requests} concurrent requests.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        results = list(executor.map(send_request, [url] * total_requests))
    
    successful_responses = sum(1 for result in results if result == 200)
    print(f"Successful responses: {successful_responses}/{total_requests}")