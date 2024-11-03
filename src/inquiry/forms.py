from django import forms


class InquiryForm(forms.Form):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    inquiry_subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    inquiry_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    cc_myself = forms.BooleanField(required=False)
    