from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#from models import UserProfiles
USER_TYPE = (('STUDENT', 'Student'), ('BUSINESS', 'Business'), ('TOURIST','Tourist'))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    account_type = forms.CharField(label="Choose Account Type", widget=forms.RadioSelect(choices= USER_TYPE))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def save (self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # user_acc = User.objects.get (username=username)
            # user_pk = user_acc.pk
            # user_acc_profile = UserProfiles.objects.get (user_id=user_pk)
            # user_acc_profile.usertype = account_type
            # user_acc_profile.save()


        return user

# class RegForm(UserCreationForm):
#
#     class Meta:
#         model = UserProfiles
#         fields = ('username',
#         'user',
#         'description',
#         'usertype',
#         'password1',
#         'password2')
#         def save (self, commit=True):
#             user = super(RegistrationForm, self).save(commit=False)
#             user.description = self.cleaned_data['description']
#             user.usertype= self.cleaned_data['usertype']
#
#             if commit:
#                 user.save()
#
#             return user
