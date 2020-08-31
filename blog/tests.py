from django.test import TestCase
from django.urls import resolve
from blog.views import cv


class cvPageTest(TestCase):

    def test_cv_url_resolves_to_cv_view(self):
        found = resolve('/cv')  
        self.assertEqual(found.func,cv)  

def test_cv_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>cv</title>', html)  
        self.assertTrue(html.endswith('</html>'))  