'''
This script extracts data about quantum computing startups from https://quantumcomputingreport.com/privatestartup/
'''
from bs4 import BeautifulSoup
import requests

def q_csv():
	# Export all company's details to a csv
	print('Start q_csv')
	res = requests.get('https://quantumcomputingreport.com/privatestartup')
	res.raise_for_status
	soup = BeautifulSoup(res.text, 'lxml')

	table = soup.find('tbody', 'row-hover')
	rows = table.find_all('tr')
	# find_all are used often because of empty children

	with open('datasets/q_startups.csv', 'w') as file:
		file.write('"name", "segment", "country", "website", "description"\n')
		for r in rows:
			data = r.find_all('td')

			website = data[0].find('a')['href']
			name = data[0].find('a').string
			segment = data[3].string
			country = data[2].string
			description = data[1].string

			file.write('"{}", "{}", "{}", "{}", "{}"\n'.format(name, segment, country, website, description))
	print('End')
	return

q_csv()