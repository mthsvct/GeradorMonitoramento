from distutils.command.upload import upload
from unicodedata import name
from django import forms

class UploadFile(forms.Form):
    arq = forms.FileField()