from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

#from django.contrib.auth.models import User

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """the home page for learning log"""
    # users = User.objects.all()
    # for user in users:
    #     print(user.username)
    #     print(user.password)
    #     print(user.id)
    return render(request, 'lla1/index.html')


@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.filter(owner=request.user.id).order_by('date_created')
    context = {'topics': topics}
    return render(request, 'lla1/topics.html', context)

def topic(request, topic_id):
    """show a single topic and its entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
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

