#Getting abbreviations and phrases from https://www.webopedia.com/reference/text-abbreviations/


from bs4 import BeautifulSoup
import requests
import csv

# Make a request to the webpage
url = 'https://www.webopedia.com/reference/text-abbreviations/'
response = requests.get(url)
html = response.text

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Open a CSV file for writing
with open('table_data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Abbreviations', 'Full Forms']) # replace with actual headers

    # Find all the table rows (`tr` tags)
    rows = soup.find_all('tr')

    # Iterate over the rows and write the text of each cell (`td` tag) to the CSV
    for row in rows:
        cells = row.find_all('td')
        cell_values = [cell.text for cell in cells]
        writer.writerow(cell_values)
