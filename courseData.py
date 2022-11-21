from bs4 import BeautifulSoup
import requests
from main import course_link

file = "code.txt"

html_content = requests.get(course_link).text
soup = BeautifulSoup(html_content, 'lxml')

university_name = soup.find( class_ = "schoolMobile_heading__2kYBg m-0 p-0").text
course_card = soup.find_all('div', class_ = 'subcourses_courseBox__3deGG')

with  open(file, 'a') as f :
    f.write(university_name + "\n" + "\n")

    for course in course_card:
        course_name = course.find('span', class_ = 'subcourses_h-title__sLV10').text
        course_fee = course.find('h3', class_ = 'subcourses_c-desc__Dzhnk').text
        course_duration = course.find_all('h3', class_ = 'subcourses_c-desc__Dzhnk')

        durray = []
        durray.append(course_duration)

        for duration in durray:
            f.write(course_name + " | " + str(course_fee) + " | " + str(duration[1].text) + "\n")
            