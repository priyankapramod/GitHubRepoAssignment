from django import forms
from .models import User,Trip, Destination
from django.forms.extras import SelectDateWidget


class UserCreateForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "xyz@gmail.com"
            })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True)
    )
    confirm_pwd = forms.CharField(
        widget=forms.PasswordInput(render_value=True)
    )
    class Meta:
         model = User
         fields =  (
             'name',
             'email',
             'password',
             'confirm_pwd'
         )
    # add validation here
    def clean(self):
        print('3. in clean')
        cleaned = self.cleaned_data
        print(cleaned)
        if cleaned['password'] != cleaned['confirm_pwd']:
            print("working")
            raise forms.ValidationError("passwords don't match")
        if len(cleaned['password']) < 8:
            raise  forms.ValidationError("password should be atleast 8 characters")




class LoginForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User


        fields = (
            'email',
            'password'
        )
    def clean(self):
        print("1")
        cleaned = self.cleaned_data
        print(cleaned)

        # get information from db

        # get email address ///r to  the  email entered in browser.
        user = User.objects.get(email=cleaned['email'])
        print(user.email, user.password)



        my_email = user.email
        my_password = user.password


        # compare information from db to information entered.
        if my_email != cleaned['email']:
            print("working1")
            raise forms.ValidationError("no such email found. Please register.")
        print(my_password, 1)
        print(cleaned['password'])

        if my_password != cleaned['password']:
            print("working2")
            raise forms.ValidationError("enter correct password.")



class TripPlanner(forms.ModelForm):
    date_from = forms.DateField(widget=SelectDateWidget())
    date_to = forms.DateField(widget=SelectDateWidget())


    class Meta:
        model = Trip
        fields = (
            'description',
            'date_from',
            'date_to',
        )
    def clean(self):
        date_from = self.cleaned_data.get("date_from")
        date_to = self.cleaned_data.get("date_to")
        if date_to < date_from:
            raise forms.ValidationError("End date should be greater than start date.")


class DestinationForm(forms.ModelForm):
    destination_name = forms.CharField()


    class Meta:
        model = Destination
        fields = (
            'destination_name',
        )
    def clean(self):
        cleaned = self.cleaned_data