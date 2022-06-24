from django.test import TestCase
from blog.forms import *

class CommentFormtest(TestCase):

    def Formfiels(self):
        
         self.assertTrue(form.fields['author'].label == 'author')
         self.assertTrue(form.fields['body'].label == 'author')
