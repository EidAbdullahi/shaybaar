from django import forms
from .models import Contact,Application



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact','subject','comment')
        

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name','nationality', 'email', 'contact','qualifications','cv')   