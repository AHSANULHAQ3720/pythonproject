import requests
import pandas as pd
from pandas import json_normalize
from APIdocs import api_token

api_url = "https://national-freight-lines.uc.r.appspot.com/api/reports/shipmentsWithInvoicesArray"
api_token = api_token

per_page = 50
all_data = []

# Fetch the first page to get the total number of pages
response = requests.get(api_url, params={"api_token": api_token, "page": 1, "per_page": per_page})
# total_pages = response.json().get('last_page', 1)
total_pages = 3081

# Fetch data in chunks
for page in range(1, total_pages + 1):
    response = requests.get(api_url, params={"api_token": api_token, "page": page, "per_page": per_page})
    if response.status_code == 200:
        data = response.json()
        all_data.extend(data.get('data', []))
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
        break

# Create a DataFrame from all the collected data
df_shipments = pd.json_normalize(all_data, 'invoices', ['shipment_id'])

# Convert 'shipment_id' to integer type
df_shipments['shipment_id'] = df_shipments['shipment_id'].astype(int)

# Save the DataFrame to Excel or CSV
df_shipments.to_excel("output.xlsx", index=False)  # Change the filename as needed
# Alternatively, you can save to CSV
# df_shipments.to_csv("output.csv", index=False)  # Change the filename as needed

print("Data has been successfully saved to Excel/CSV.")
