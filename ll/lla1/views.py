from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
import random

#from django.contrib.auth.models import User

from .models import Topic, Entry, Media
from .forms import TopicForm, EntryForm, MediaForm

def index(request):
    """the home page for learning log"""
    # users = User.objects.all()
    # for user in users:
    #     print(user.username)
    #     print(user.password)
    #     print(user.id)
    #media = Media.objects.all()
    #return render(request, 'lla1/index.html')
    staticFileName = 'audio/' + str(random.randint(1,1000) % 3) + '.mp3' # Generate a random number between 1 and 100    
    selectedEntry = Entry.objects.get(title='Be Genuine')
    return render(request, 'lla1/index.html', {'staticFileName': staticFileName,
                                               'selectedEntry': selectedEntry})


@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.filter(owner=request.user.id).order_by('-priority')
    context = {'topics': topics}
    return render(request, 'lla1/topics.html', context)

def gallery(request):
    """show all media items"""
    items = Media.objects.all().order_by('-uploaded_at').filter(title__contains = 'hype')
    context = {'items': items}
    return render(request, 'lla1/gallery.html', context)

def topic(request, topic_id):
    """show a single topic and its entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-priority')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'lla1/topic.html', context)

def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('lla1:topics')

    # for blank or invalid form, show the form again with/without error message 
    context = {'form': form}
    return render(request, 'lla1/new_topic.html', context)

def new_entry(request, topic_id):
    """add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:   
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('lla1:topic', topic_id=topic_id)

    # for blank or invalid form, show the form again with/without error message 
    context = {'topic': topic, 'form': form}
    return render(request, 'lla1/new_entry.html', context)  

def edit_entry(request, entry_id):
    """edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)        
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lla1:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'lla1/edit_entry.html', context)

# def media_list(request):
    

def upload_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lla1:index')
    else:
        form = MediaForm()
    return render(request, 'lla1/upload_media.html', {'form': form})




