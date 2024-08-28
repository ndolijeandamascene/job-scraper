import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
URL = 'https://www.indeed.com/jobs?q=software+developer&l='

# Send a GET request to the website
response = requests.get(URL)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job listings on the page
jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

# Lists to store job data
job_titles = []
company_names = []
locations = []
summaries = []

# Loop through the job listings and extract data
for job in jobs:
    title = job.find('a', class_='jobtitle').text.strip()
    company = job.find('span', class_='company').text.strip()
    location = job.find('span', class_='location').text.strip()
    summary = job.find('div', class_='summary').text.strip()

    job_titles.append(title)
    company_names.append(company)
    locations.append(location)
    summaries.append(summary)

# Create a DataFrame to store the extracted data
jobs_df = pd.DataFrame({
    'Job Title': job_titles,
    'Company': company_names,
    'Location': locations,
    'Summary': summaries
})

# Save the DataFrame to a CSV file
jobs_df.to_csv('jobs.csv', index=False)

print('Job data has been successfully saved to jobs.csv')