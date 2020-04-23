from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError("User does not exist")

            if not user.check_password:
                raise forms.ValidationError("Incorrect Password")

        return super(UserLoginForm,self).clean(*args,**kwargs)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Login',css_class='btn-primary'))


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Register',css_class='btn-primary'))

    def clean(self,*args,**kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords must match")

        return super(UserRegisterForm,self).clean(*args,**kwargs)