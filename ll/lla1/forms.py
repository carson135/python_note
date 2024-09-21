from django import forms
from .models import Topic, Entry, Media

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        labels = {'name': ''}   
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control', 
                                                 'rows': 27,
                                                 'placeholder': 'Enter your note here...',
                                                 'style': 'resize: vertical;'})}

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'description', 'image', 'video']

