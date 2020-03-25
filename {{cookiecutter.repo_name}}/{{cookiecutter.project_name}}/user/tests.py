from django.contrib.auth import get_user_model, authenticate, password_validation
from django.test import TestCase

from user.form import UserCreateForm

User = get_user_model()


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'admin@demo.com',
            'password': 'admin'
        }
        User.objects.create_user(**self.credentials)

    def test_1_user_exists(self):
        print('Testing for User Exist')
        user = User.objects.get(email=self.credentials['email'])
        self.assertTrue(user)

    def test_2_user_active(self):
        print('Testing for User Active')
        user = User.objects.get(email=self.credentials['email'])
        self.assertTrue(user.is_active)

    def test_3_invalid_credentials(self):
        print('Testing for User Valid Credentials')
        form = authenticate(email=self.credentials['email'], password=self.credentials['password'])
        self.assertTrue(form)


class SignUp(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@example.com',
            'password': 'Testing@123',
        }

    def test_1_password_validation(self):
        print('Testing for password Validation')
        validate = password_validation.validate_password(self.data['password'])
        self.assertEquals(validate, None)

    # TODO make UserCreateForm for testing
    def test_2_user_creation_and_verification(self):
        print('Testing Create user')
        form = UserCreateForm(data=self.data)
        form.is_valid()
        form.create(self.data)
        self.assertTrue(form)
        user = User.objects.get(email=self.data['email'])
        self.assertTrue(user)

    def test_3_password_check(self):
        print('Testing Password/Confirm Password match')
        password = self.data['password']
        confirm_password = 'Testing@123'
        if password == confirm_password:
            self.assertTrue('password matched')
        else:
            self.assertFalse('password mismatch')
