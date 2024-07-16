from bs4 import BeautifulSoup
import requests


# getting web data from rows: 
def web_data(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    trs = soup.find_all('tr')

    
    trs_data = []
    # looping through every row
    for x in range(1, len(trs)):
        tds = trs[x].find_all('td')
        trs_data.append(personal_data(tds))
    return trs_data


# get and validate data from each row
def personal_data(tds):
    person = Khoj(tds)
    data = []
    data.append(person.check_name())
    data.append(person.check_website())
    data.append(person.check_designation())
    data.append(person.check_dept())
    data.append(person.check_email())
    data.append(person.check_phone())
    data.append(person.check_office_contact())
    return data


# takes row wise data and processes them to supply valid data
class Khoj():
    def __init__(self,tds):
        self.tds = tds
           
    def check_name(self):
        if self.tds[1].a.text == '':
            return 'Not assigned'
        else:
            return self.tds[1].a.text.strip()

    def check_website(self):
        if self.tds[1].a['href'] == '':
            return 'Not assigned'
        else:
            return self.tds[1].a['href'].strip()
    
    def check_designation(self):
        if self.tds[3].text == '':
	        return 'Not assigned'
        else:
	        return self.tds[3].text.strip()

    def check_dept(self):
        if self.tds[4].text == '':
	        return'Not assigned'
        else:
	         return self.tds[4].text.strip()
    
    def check_email(self):
        if self.tds[5].text == '':
	        return'Not assigned'
        else:
	         return self.tds[5].text.strip()

    def check_phone(self):
        if self.tds[6].text == '':
	        return'Not assigned'
        else:
	         return self.tds[6].text.strip()

    def check_office_contact(self):
        if self.tds[7].text == '':
	        return'Not assigned'
        else:
	         return self.tds[7].text.strip()


# main function
if __name__ == '__main__':
    
    depts = ['cse', 'eee', 'ce', 'me', 'mte', 'ipe', 'gce', 'mse', 'ece', 'ete', 'urp','arch', 'becm', 'cfpe', 'phy', 'chem', 'hum', 'math']
    for dept in depts:
        link = 'https://www.' + dept + '.ruet.ac.bd/teacher_list'
        data = web_data(link)

        # writes the double dimension data in a txt file at cwd for further use
        with open(dept.upper() + "_faculty.txt", "w") as output:
            for row in data:
                output.write(str(row) + '\n')

            output.write('\n\n\n')

            output.write(str(data))
