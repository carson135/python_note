from django.shortcuts import render

from .models import Topic

def index(request):
    """the home page for learning log"""
    return render(request, 'lla1/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_created')
    context = {'topics': topics}
    return render(request, 'lla1/topics.html', context)

def topic(request, topic_id):
    """show a single topic and its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'lla1/topic.html', context)

