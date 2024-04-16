from django import forms
from .models import ChatMessage

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['file']
