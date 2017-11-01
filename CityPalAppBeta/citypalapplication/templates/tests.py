from django.test import TestCase

import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Question

class CreateAccount(TestCase):

    username = 'testuser'
    password = 'Password123'
    email = 'user@test.com'
    first_name = 'Mister'
    last_name = 'Test'

    def setUp(self):
        user = User.objects.CreateAccount(self.username)
        user.email = self.email
        user.first_name = self.first_name
        user.last_name = self.last_name
        user.set_password(self.password)
        user.save()

    # def registerUser(self):
    #
    # def userLogIn(self):
    #     user =
    #
    # def userLogOut(self):
    #     user =
    #
    # def registerInvalidUser(self):
    #     user =
    #
    # def failedUserLogInAttempt(self):
    #     user =
