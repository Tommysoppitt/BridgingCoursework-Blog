from django.test import TestCase
from django.urls import resolve
from blog.views import cv
from blog.views import skill_new
from blog.views import hobby_new
from blog.views import responsibility_new
from blog.views import experience_new
from django.test import TestCase
from .forms import SkillForm
from django.http import HttpResponse
from django.http import HttpRequest

class cvPageTest(TestCase):

    def test_cv_url_resolves_to_cv_view(self):
        found = resolve('/cv')  
        self.assertEqual(found.func,cv)  

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv(request)  
        html = response.content.decode('utf8')  
     
        self.assertIn("Tom Soppitt's CV", html)  
        self.assertTrue(html.endswith('</html>'))  

       
    def test_new_skill_url_resolves_to_new_skill_view(self):
        found = resolve('/cv/skill_new')  
        self.assertEqual(found.func,skill_new)  

    def test_new_skill_page_returns_correct_html(self):
        request = HttpRequest()  
        response = skill_new(request)  
        html = response.content.decode('utf8')  
       
        self.assertIn('<h2>New post</h2>', html)  
        
    def test_new_responsibility_url_resolves_to_new_responsibility_view(self):
        found = resolve('/cv/responsibility_new')  
        self.assertEqual(found.func,responsibility_new)  

    def test_new_responsibility_page_returns_correct_html(self):
        request = HttpRequest()  
        response = responsibility_new(request)  
        html = response.content.decode('utf8')  
     
        self.assertIn('<h2>New post</h2>', html)  
      
    
    def test_new_experience_url_resolves_to_new_experience_view(self):
        found = resolve('/cv/experience_new')  
        self.assertEqual(found.func,experience_new)  

    def test_new_experience_page_returns_correct_html(self):
        request = HttpRequest()  
        response = experience_new(request)  
        html = response.content.decode('utf8')  
        self.assertIn('<h2>New post</h2>', html)  

    def test_new_hobby_url_resolves_to_new_hobby_view(self):
        found = resolve('/cv/hobby_new')  
        self.assertEqual(found.func,hobby_new)  

    def test_new_hobby_page_returns_correct_html(self):
        request = HttpRequest()  
        response = hobby_new(request)  
        html = response.content.decode('utf8')  
        self.assertIn('<h2>New post</h2>', html)  