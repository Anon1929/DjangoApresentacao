from projects.models import *
from blog.models import *
from django.test import TestCase

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title='teste',description='teste2',technology='teste3',image='project1')
    
    def test_labels(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
        field_label = project._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')
        
        field_label = project._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')
        
        field_label = project._meta.get_field('technology').verbose_name
        self.assertEquals(field_label, 'technology')
    
class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='teste')
    
    def test_labels(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
