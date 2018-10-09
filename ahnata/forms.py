from django.contrib.auth.models import User
from django import forms
from .models import Boutique, Articles, Post


class signUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']
class ContactForm(forms.Form):

    sujet = forms.CharField(max_length=100, label="objet", required=True)
    emailAdress = forms.EmailField(label=u"Email", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Message")
    
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('titre', 'texte',)


						
			
	

