'''
This script extracts data about space startups from spacebandits.io

I'm thinking about applying for job at a space company. 
It would be great to have a list and compare them (or even perform some analysis).
Let's automate the boring extraction.
'''
from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests


spacebandits = 'https://www.spacebandits.io/startups'
def space_csv():
	# Export company's name, description and url to csv
	res = requests.get(spacebandits)
	res.raise_for_status
	soup = BeautifulSoup(res.text, 'lxml')
	company_url = soup.select('a.home-startups-link-block')

	with open('datasets/space_startups.csv', 'w') as file:
		file.write('"url", "name", "description"\n')
		for company in company_url:
			url = 'https://www.spacebandits.io'+company['href']
			name = company.contents[0].contents[2].contents[0].string
			desc = company.contents[0].contents[2].contents[1].string
			file.write('"{}", "{}", "{}"\n'.format(url, name, desc))

def extract_info(url):
	# Extract full details of each company from url
	res = requests.get(url)
	res.raise_for_status
	soup = BeautifulSoup(res.text, 'lxml')

	industry_tag = soup.find('div', 'startup-industry-tag')
	country_flag = industry_tag.next_sibling
	info = soup.find_all('li', 'list-item-51')

	url = 'https://www.spacebandits.io'+soup.find('a', 'w--current')['href']
	name = soup.find('h1', 'startup-page-heading-name').string
	description = soup.find('h2', 'heading-15').string
	website = soup.find('a', 'button-startup-website-link')['href']
	mission = soup.find('p', 'startup-mission').string
	industry = industry_tag.string
	country = country_flag['src'].split('-')[-2]
	year_founded = info[0].string
	funding_type = info[1].string
	total_funding = info[2].string		
	employees = info[3].string
	print('Extraction from {} successful'.format(url))
	return (name, country, website, industry, description, mission, employees, year_founded, funding_type, total_funding, url)

def fetch_urls():
	# Fetch the url for each company
	print('Fetching Company URLs')
	res = requests.get(spacebandits)
	res.raise_for_status
	soup = BeautifulSoup(res.text, 'lxml')

	print('Soup made')
	url_tag = soup.find_all('a', 'home-startups-link-block', limit=10)		# Remove the limit parameter to truly find_all
	urls = []
	print('Got the tags')

	for tag in url_tag:
		urls.append('https://www.spacebandits.io'+tag['href'])
	print('Got the url. Now exiting fetch')
	return urls

def space_xl():
	# Save full company details into 'spacebandits.xlsx'
	print('Create Workbook and sheet')
	wb = Workbook(write_only=True)
	ws = wb.create_sheet('Space companies', 0)
	ws.append(('name', 'country', 'website', 'industry', 'description', 'mission', 'employees', 'year_founded', 'funding_type', 'total_funding', 'url'))

	print('Go and fetch URLs')
	for url in fetch_urls():
		print('Go and extract info from', url)
		ws.append(extract_info(url))

	wb.save('datasets/spacebandits.xlsx')
	print('spacebandits.xlsx successfully saved in datasets')

space_csv()
