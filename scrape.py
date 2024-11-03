import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.purdue.edu/ehps/police/statistics-policies/daily-crime-log-archives/102824-daily-crime-log.php'

r = requests.get(url)


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    
save_html(r.content, 'google_com')
soup = BeautifulSoup(r.content, 'html.parser')
    
html = open_html('google_com')

crimes = soup.select('tr td')
i = 0

csv_file_name = 'crimes_report.csv'

header = ["Nature", "Case Number", "Date/Time Occurred", "Date/Time Reported", "General Location", "Disposition"]

i = 0

with open(csv_file_name, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    line = []
    for crime in crimes:
        if (i % 6 == 0) and i != 0:  # Ensure we write after the first group of 6
            writer.writerow(line)
            line = []  # Reset the list for the next group

        if crime.contents:
            line.append(crime.contents[0])
        else:
            line.append(" ")

        i += 1  # Increment i
        
        print(line)

        
