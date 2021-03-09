from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=&cboWorkExp1=0').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    time_posted = job.find('span', class_='sim-posted').span.text
    if 'few' in time_posted:

        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')


        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        Time Posted: {time_posted}
        ''')

        print(' ')