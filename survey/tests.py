from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase
from .views import home, user_profile
from .models import Profile, Survey, Design
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.core import mail


class HomeTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_home_view_status_code(self):
            url = reverse('home')
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
            view = resolve('/')
            self.assertEquals(view.func, home)

    def test_mysurveys_code(self):
            url = reverse('user_profile', kwargs={'user': 'mikev2'})
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

    def test_mysurveys_url_resolves_mysurveys_view(self):
            view = resolve('/u/mikev2/')
            self.assertEquals(view.func, user_profile)


'''    def setUp(self):
        self.study = Study.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_studies_page(self):
        study_url = reverse('all_studies', kwargs={'pk': self.study.pk})
        self.assertContains(self.response, 'href="{0}"'.format(study_url))


class StudiesTests(TestCase):
    def setUp(self):
        Study.objects.create(name='Test Study', description='A study on webframeworks - a test.')

    def test_studies_success_status_code(self):
    	url = reverse('all_studies', kwargs={'pk': 1})
    	#print(url)
    	response = self.client.get(url)
    	self.assertEquals(response.status_code, 200)

    def test_studies_fail_status_code(self):
    	url = reverse('all_studies', kwargs={'pk': 99})
    	print(url)
    	response = self.client.get(url)
    	self.assertEquals(response.status_code, 404)

    def test_studiesurl_resolves_studies_view(self):
    	view = resolve('/studies/1/')
    	self.assertEquals(view.func, all_studies)	

    def test_board_topics_view_contains_link_back_to_homepage(self):
        url = reverse('all_studies', kwargs={'pk': 1})
        response = self.client.get(url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_board_topics_view_contains_navigation_links(self):
        studies_url = reverse('all_studies', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_survey_url = reverse('new_survey', kwargs={'pk': 1})

        response = self.client.get(studies_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_survey_url))

class NewSurveyTests(TestCase):

    def setUp(self):
        Study.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')  # <- included this line here

    def test_csrf(self):
        url = reverse('new_survey', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')    

    def test_new_survey_valid_data(self):
        url = reverse('new_survey', kwargs={'pk': 1})
        data = {
            'name': 'Test title',
            'description': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Survey.objects.exists())
        #self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        

        url = reverse('new_survey', kwargs={'pk': 1})
        #print(url)
        response = self.client.post(url, {})
        print("HELLO")
        print(response)
        self.assertEquals(response.status_code, 200)
'''

