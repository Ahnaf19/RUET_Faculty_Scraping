from bs4 import BeautifulSoup
import requests

class Khoj():
    def __init__(self,tds):
        self.tds = tds
           
    def check_name(self):
        if self.tds[1].a.text == '':
            #print('Not assigned')
            return 'Not assigned'
        else:
            #print(self.tds[1].a.text)
            return self.tds[1].a.text.strip()

    def check_website(self):
        if self.tds[1].a['href'] == '':
            #print('Not assigned')
            return 'Not assigned'
        else:
            #print(self.tds[1].a['href'])
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


def web_data(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    trs = soup.find_all('tr')
    tds = trs[2].find_all('td')
    return tds


def personal_data(link):
    a = Khoj(web_data(link))
    data = []
    data.append(a.check_name())
    data.append(a.check_website())
    data.append(a.check_designation())
    data.append(a.check_dept())
    data.append(a.check_email())
    data.append(a.check_phone())
    data.append(a.check_office_contact())
    return data

if __name__ == '__main__':
    
    link = 'https://www.cse.ruet.ac.bd/teacher_list'
    data = personal_data(link)
    for x in data:
        print(x)
