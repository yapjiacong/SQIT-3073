import requests
import json
from datetime import datetime
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

# API Endpoint: https://apikijangportal.bnm.gov.my

# Get the current date
current_date = datetime.now()

# Define the endpoint URL with the start year and month and the current year and month
start_year = 2023
start_month = 1
current_year = current_date.year
current_month = current_date.month

# Create a list to store the data for each month
data_list = []

# Loop through the months from the start date to the current date
while start_year <= current_year or (start_year == current_year and start_month <= current_month):
    # Define the endpoint URL for the current month
    endpoint_url = f"https://api.bnm.gov.my/public/fx-turn-over/year/{start_year}/month/{start_month:02}"

    # Define the header parameters
    headers = {
        "Accept": "application/vnd.BNM.API.v1+json"
    }

    # Make a GET request to the API
    try:
        response = requests.get(endpoint_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the JSON response
        data = json.loads(response.text)

        # Append the data to the list
        data_list.append(data)
    except requests.exceptions.RequestException as e:
        print(f"Error in API request: {e}")
        break

    # Move to the next month
    if start_month == 12:
        start_year += 1
        start_month = 1
    else:
        start_month += 1

# Extracted Json data
pprint(data_list)
json_data = data_list

# Extract the 'data' part for time series
data_list = [item['data'] for item in json_data]

# Flatten the list of dictionaries
flat_data_list = [entry for sublist in data_list for entry in sublist]

# Create a DataFrame
df = pd.DataFrame(flat_data_list)

# Convert 'date' column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Sort the DataFrame by 'date' in ascending order
df.sort_values(by='date', inplace=True)

# Set 'date' column as the index
df.set_index('date', inplace=True)

# Print DataFrame
print(df)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['your_column_name'], label='Your Column Name')
plt.title('FX Turn Over Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()
