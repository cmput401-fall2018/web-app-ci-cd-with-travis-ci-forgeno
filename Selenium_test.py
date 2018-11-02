from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    selenium = webdriver.Chrome()
    selenium.get('http://162.246.157.221:8000')

    name = selenium.find_element_by_id('name')
    about = selenium.find_element_by_id('about')
    education = selenium.find_element_by_id('education')
    skills = selenium.find_element_by_id('skills')
    work = selenium.find_element_by_id('work')
    contact = selenium.find_element_by_id('contact')
    
    assert name.text == "Ivan Ma"
    assert about.text == "4th year Computer Science Student"
    assert education.text == "University of Alberta 2014-2019"
    assert skills.text == "Java, Python, C"
    assert work.text == "Unemployed"
    assert contact.text == "ima@ualberta.ca"