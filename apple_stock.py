import requests
from bs4 import BeautifulSoup

def get_apple_stock_data():
    # Define the URL
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    
    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make a request to the website with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table with historical data
    table = soup.find('table', class_='W(100%) M(0)')
    
    # Check if table is found
    if not table:
        print("Unable to find the historical data table.")
        return
    
    # Extract the rows from the table
    rows = table.findAll('tr')
    
    # Iterate over the rows and extract the date and close price
    for row in rows[1:]:  # Skip the header row
        columns = row.findAll('td')
        if len(columns) > 4:  # Ensure there are enough columns to extract data
            date = columns[0].text
            close_price = columns[4].text
            print(f'Date: {date}, Close Price: {close_price}')

if __name__ == "__main__":
    get_apple_stock_data()