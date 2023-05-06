import requests
import time

# Separate the URL into two parts: base URL and address
base_url = "https://api.foxe.vip/api/merkle/"
address = ""
url = f"{base_url}{address}"

def fetch_data(url, max_retries=5000, retry_delay=1):
    """
    Fetch data from the specified API URL.

    Args:
        url (str): The URL to fetch data from.
        max_retries (int, optional): The maximum number of retries for connection errors and gateway errors. Defaults to 5000.
        retry_delay (int, optional): The delay between retries in seconds. Defaults to 1.

    Returns:
        dict: The JSON data fetched from the API, or None if the request failed.
    """
    retries = 0

    while retries <= max_retries:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()
            elif response.status_code in [502, 504]:
                print(f"Error {response.status_code}: Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            elif response.status_code == 404:
                print("Error 404: Resource not found. Check the API URL and try again.")
                return None
            else:
                print(f"Error: Unable to fetch data from API. Status code: {response.status_code}")
                return None
        except requests.exceptions.ConnectionError as e:
            retries += 1
            print(f"ConnectionError: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

    print("Max retries exceeded. Failed to fetch data from API.")
    return None

if __name__ == "__main__":
    data = fetch_data(url)

    if data:
        print("Data successfully fetched from API:")
        print(data)
    else:
        print("Failed to fetch data from API.")
