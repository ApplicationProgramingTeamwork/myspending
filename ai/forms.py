# forms.py
from django import forms


class PhotoUploadForm(forms.Form):
    photo = forms.FileField(required=False)
