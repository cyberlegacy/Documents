from django.test import TestCase
from django.urls import reverse
from .models import SignupRequest
from .forms import SignupForm
import json

class JapaneseClassAppViewsTests(TestCase):

    def test_index_view_status_code(self):
        response = self.client.get(reverse('japanese_class_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'japanese_class_app/index.html')

    def test_signup_page_view_status_code(self):
        response = self.client.get(reverse('japanese_class_app:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'japanese_class_app/signup.html')
        self.assertIsInstance(response.context['form'], SignupForm)

class SignupRequestModelTests(TestCase):

    def test_create_signup_request(self):
        request = SignupRequest.objects.create(
            full_name="Test User",
            email="test@example.com",
            affiliation="student",
            self_assessed_level="beginner",
            preferred_class_level="beginner"
        )
        self.assertEqual(str(request), "Test User - test@example.com")

class SignupFormTests(TestCase):

    def test_valid_form(self):
        data = {
            'full_name': "Test User",
            'email': "test@example.com",
            'affiliation': "student",
            'self_assessed_level': "beginner",
            'preferred_class_level': "beginner"
        }
        form = SignupForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_email(self):
        data = {
            'full_name': "Test User",
            # 'email': "test@example.com", # Missing email
            'affiliation': "student",
            'self_assessed_level': "beginner",
            'preferred_class_level': "beginner"
        }
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_other_affiliation_requires_details(self):
        data = {
            'full_name': "Test User",
            'email': "test@example.com",
            'affiliation': "other", # 'other' selected
            'other_affiliation_details': "", # But no details
            'self_assessed_level': "beginner",
            'preferred_class_level': "beginner"
        }
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('other_affiliation_details', form.errors)

class ApiSignupViewTests(TestCase):

    def test_api_signup_success(self):
        data = {
            'full_name': "API User",
            'email': "api@example.com",
            'affiliation': "staff_researcher",
            'self_assessed_level': "intermediate",
            'preferred_class_level': "intermediate",
            'previous_experience': "Some experience",
            'learning_goals': "Speak fluently"
        }
        response = self.client.post(
            reverse('japanese_class_app:api_signup'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['status'], 'success')
        self.assertTrue(SignupRequest.objects.filter(email="api@example.com").exists())

    def test_api_signup_validation_error(self):
        data = {
            'full_name': "API User Bad",
            # Missing email
            'affiliation': "student",
            'self_assessed_level': "beginner",
            'preferred_class_level': "beginner"
        }
        response = self.client.post(
            reverse('japanese_class_app:api_signup'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertIn('email', response.json()['errors'])

    def test_api_signup_duplicate_email(self):
        SignupRequest.objects.create(
            full_name="Existing User",
            email="duplicate@example.com",
            affiliation="student",
            self_assessed_level="beginner",
            preferred_class_level="beginner"
        )
        data = {
            'full_name': "New User",
            'email': "duplicate@example.com", # Duplicate email
            'affiliation': "other",
            'other_affiliation_details': "External researcher",
            'self_assessed_level': "advanced",
            'preferred_class_level': "advanced"
        }
        response = self.client.post(
            reverse('japanese_class_app:api_signup'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertIn('email', response.json()['errors'])
        self.assertIn('already exists', response.json()['errors']['email'][0])
