from django.test import TestCase
from django.urls import reverse

from projects.views import *
from blog.views import *

class ProjectsViewtest(TestCase):
    def test_view_url_index(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    def index_correct_template(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_index.html')
        
    
class BlogViewtest(TestCase):

    def test_view_blog_index(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
    
    def index_correct_template(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_index.html')