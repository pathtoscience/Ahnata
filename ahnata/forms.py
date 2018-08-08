from django.contrib.auth.models import User
from django import forms
from .models import Boutique, Article

"""class BoutiqForm(forms.ModelForm):
    nom = forms.CharField(max_length=25)
    class Meta:
    	model = Boutique
    	fields = ['nom','stock_gerant','categorie','date_create']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom','prix','description','categorie','article_logo','date_ajout']	"""
				

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class ContactForm(forms.Form):

    sujet = forms.CharField(max_length=100)
    emailAdress = forms.EmailField(label=u"Email")
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)




						
			
	

