from django import forms

class UploadFile(forms.Form):
    arq = forms.FileField()