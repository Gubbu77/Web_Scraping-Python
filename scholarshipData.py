from bs4 import BeautifulSoup
import requests
from main import scholarship_link

file = "code.txt"


html_content = requests.get(scholarship_link).text
soup = BeautifulSoup(html_content, 'lxml')

university_name = soup.find( class_ = "schoolMobile_heading__2kYBg m-0 p-0").text
print(university_name, "\n")

scholarship_card = soup.find_all('div', class_ = 'scholarship_card-content__2XurL')


with  open(file, 'a') as f :
    for scholar in scholarship_card:

        scholarship_name =  scholar.find('a', id = 'scholarship_card-link__3pX9Q')
        scholarship_type =  scholar.find('h3', class_ = 'scholarship_card-text__2pxiu')
        description_card = soup.find_all('div', class_ = 'scholarship_card-body__Ap80X')

        print(scholarship_name.text)
        print(scholarship_type.text)


        for desc in description_card:
            para = desc.p.text
            list = []
            list.append(para)
            print(list)

        print('')
        




