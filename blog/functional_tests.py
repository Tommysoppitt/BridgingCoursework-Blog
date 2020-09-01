from selenium import webdriver
from django import forms
import unittest

from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page(self):  
        # Tom visits his new online CV
        self.browser.get('http://tommysoppitt.pythonanywhere.com/cv')

        # He notices the title and header contains the words "Tom Soppitt's CV"
        self.assertIn("Tom Soppitt's CV", self.browser.title)  
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Tom Soppitt's CV", header_text)

        # He wants to add a new skill to the CV
    def test_new_skill_page(self):  
       
        self.browser.get('http://tommysoppitt.pythonanywhere.com/cv/skill_new')
     # He wants to add a new experience to the CV
    def test_new_experience_page(self):  
       
        self.browser.get('http://tommysoppitt.pythonanywhere.com/cv/experience_new')
# He wants to add a new position of responsibility to the CV
    def test_new_responsibility_page(self):  
       
        self.browser.get('http://tommysoppitt.pythonanywhere.com/cv/responsibility_new')
# He wants to add a new hobby to the CV
    def test_new_hobby_page(self):  
       
        self.browser.get('http://tommysoppitt.pythonanywhere.com/cv/hobby_new')


        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  