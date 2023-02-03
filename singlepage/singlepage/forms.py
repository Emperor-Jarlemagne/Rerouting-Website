from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label="Name")
    email_address = forms.EmailField(max_length = 150, label="E-mail")
    subject = forms.CharField(max_length=100, label="Subject")
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
    
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
