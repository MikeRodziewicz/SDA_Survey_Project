from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import sign_up, survey_thanks, home
from .models import GuestSurvey
from .forms import GuestSurveyForm

# Create your tests here.
class WebsiteTests(TestCase):
    def setUp(self):
        self.person = GuestSurvey.objects.create(guest_name='Jarek', quest_email='jarek@test.com')

    def test_url_home(self):
        url = reverse('website-home')
        self.assertEquals(resolve(url).func, home)

    def test_url_sing_up(self):
        url = reverse('sign_up')
        self.assertEquals(resolve(url).func, sign_up)

    def test_url_survey_thanks(self):
        url = reverse('survey_thanks')
        self.assertEquals(resolve(url).func, survey_thanks)

    def test_view_home(self):
        client = Client()
        response = client.get(reverse('website-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')

    def test_view_sign_up(self):
        client = Client()
        response = client.get(reverse('sign_up'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/survey_sign_up.html')

    def test_view_survey_thanks(self):
        client = Client()
        response = client.get(reverse('survey_thanks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/survey_thanks.html')

    def test_person(self):
        self.assertEquals(self.person.quest_email, 'jarek@test.com')

    def test_index(self):
        res = self.client.get('/')
        self.failUnlessEqual(res.status_code, 200)


