from django.contrib.auth import authenticate
from django.forms import DateTimeInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, help_text='Enter user name ',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text='Your password must contain atleast 8 characters',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(help_text='Your password must match with above password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)

        return super(SignInForm, self).clean(*args, **kwargs)



class Profile(forms.ModelForm):
    gender_choices = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    age = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=20, required =True, widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select)

    class Meta:
        model = Accounts
        fields = ['name', 'age', 'gender']


class BooksProfile(forms.ModelForm):
    bookname = forms.CharField(max_length=20, required =True, widget=forms.TextInput(attrs={'class':'form-control'}))
    issuedate = forms.DateTimeField(label='Issue date',
                                    required=False,
                                    input_formats=["%m/%d/%Y %H:%M %p"],
                                    widget=DateTimeInput(format="%m/%d/%Y %H:%M %p",
                             attrs = {'placeholder': 'YYYY-mm-dd HH:mm:ss'})
                                    )

    class Meta:
        model = Books
        fields = ['bookname', 'issuedate']


class Songs_data_enter(forms.ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'