from django import forms
from .models import Topic, Entry, Media

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        labels = {'name': 'Add a new topic'}   
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your topic here...'})}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'priority', 'text']
        labels = {'title': 'Title', 'priority': 'Priority', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control flex-grow-1',                                                 
                                                 #'rows': 25,                                                 
                                                 'placeholder': 'Enter your note here...',
                                                 'style': 'resize: vertical; height: 100%;'}),
                   'title': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your title here...'}),
                   'priority': forms.NumberInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your priority here...',
                                                   'min': 0,
                                                   'max': 100})}

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'description', 'image', 'video']

