from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    content = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))


    def clean_email(self, *args, **kwargs):
    	email = self.cleaned_data.get('email')
    	print(email)
    	if email.endswith(".edu"):
    		raise forms.ValidationError("No good, not edu") 
    	return email