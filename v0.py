from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.cse.ruet.ac.bd/teacher_list').text

soup = BeautifulSoup(source, 'lxml')

trs = soup.find_all('tr')
#print(trs[1])
#print('\n')
print(trs[-1])

tds = trs[2].find_all('td')


# name = tds[1].a.text
# website = tds[1].a['href']
# designation = tds[3].text
# dept = tds[4].text
#email = tds[5].text
# phone = tds[6].text
# office_contact = tds[7].text

if tds[1].a.text == '':
	name = 'Not assigned'
else:
	name = tds[1].a.text.strip()


if tds[1].a['href'] == '':
	website = 'Not assigned'
else:
	website = tds[1].a['href'].strip()


if tds[3].text == '':
	designation = 'Not assigned'
else:
	designation = tds[3].text.strip()


if tds[4].text == '':
	dept = 'Not assigned'
else:
	dept = tds[4].text.strip()


if tds[5].text == '':
	email = 'Not assigned'
else:
	email = tds[5].text.strip()


if tds[6].text == '':
	phone = 'Not assigned'
else:
	phone = tds[6].text.strip()


if tds[7].text == '':
	office_contact = 'Not assigned'
else:
	office_contact = tds[7].text.strip()


#print(name, website, designation, dept, email, phone, office_contact)