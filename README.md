# API Data Fetcher

This Python script fetches data from the specified API URL and prints the JSON data to the console. It handles common errors, such as 502 Bad Gateway, 504 Gateway Timeout, and ConnectionError, by retrying the request with a delay.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository or download the script.
2. Install the required library using pip: pip install requests


## Usage

1. Open the `api_data_fetcher.py` script in a text editor.
2. Modify the `base_url` and `address` variables to match the desired API endpoint and address.
3. Save the script and run it using the command: python api_data_fetcher.py


The script will fetch the data from the API and print it to the console. If an error is encountered, the script will retry the request up to the specified maximum number of retries.

## Configuration

You can adjust the `max_retries` and `retry_delay` parameters in the `fetch_data` function to control the behavior of the retry mechanism.
