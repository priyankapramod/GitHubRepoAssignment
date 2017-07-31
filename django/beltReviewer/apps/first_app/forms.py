from django import forms
from .models import User, Login, Books


class UserCreateForm(forms.ModelForm):
    name = forms.CharField()
    alias = forms.CharField()
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
             'alias',
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
        # if len(cleaned['pwd']) < 8:
        #     raise  forms.ValidationError("password should be atleast 8 characters")




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

class AddBooksAndReviews(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    review = forms.CharField(
        widget=forms.Textarea()
    )
    rating = forms.CharField(
        widget=forms.NumberInput()
    )
    class Meta:
        model = Books
        fields = (
            'title',
            'author',
            'review',
            'rating',
        )
    def clean(self):
        cleaned = self.cleaned_data


# class BookUserForm(forms.ModelForm):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=User.objects.all())
#
#     class Meta:
#         model = Books
#         fields = (
#             'title',
#             'author',
#             'review',
#             'rating',
#         )
#     def clean(self):
#         cleaned = self.cleaned_data
#
#




