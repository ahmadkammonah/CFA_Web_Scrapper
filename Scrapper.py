# Imports
import requests
from bs4 import BeautifulSoup

# Function to convert data to CSV
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Industry', 'Business Name', 'Investment Required'])
        writer.writerows(data)

# Function to scrape data
def scrape_data(url, start_page=1, end_page=18):
    data = []
    for page in range(start_page, end_page + 1):
        # Constructing URL for each page
        page_url = f"{url}/page/{page}/#franchise-cards"
        
        # Fetching url
        response = requests.get(page_url)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        try:
            # Find the elements with the specified class
            Industrys = soup.find_all('span', class_='content-franchise-card-breadcrumb')
            BusinessNames = soup.find_all('h1', class_='content-franchise-card-title')
            InvestmentsRequired = soup.find_all('span', class_='content-franchise-card-value')
            
            for i in range(len(Industrys)):
              #Industrys[i] = Industrys[i].text
              #BusinessNames[i] = BusinessNames[i].text
              #InvestmentsRequired[i] = InvestmentsRequired[i].text
              
              data.append([(Industrys[i].text).strip(), (BusinessNames[i].text).strip(), (InvestmentsRequired[i].text).strip()])
        except Exception as e:
            print(f"Error on page {page}: {e}")

    return data

# Send a GET request to the URL
base_url = "https://cfa.ca/lookforafranchise/listings"

# Call Function to Scrape Data
franchise_data = scrape_data(base_url)

# Save to CSV
csv_filename = "franchise_data.csv"
save_to_csv(franchise_data, csv_filename)
