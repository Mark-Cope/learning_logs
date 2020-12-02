from django.shortcuts import render, redirect
from .models import Topic
from .forms import Topic
# Create your views here.
def index(request):
    """The homr page for learning log."""
    return render(request, 'learning_logs/index.html')



def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics':topics}

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):

    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}

    return render(request, 'learning_logs/topics.html', context)

def new_topic(request):
    if request.method !='POST':
        form = EntryForm()
    else:
        form = EntryForm(data=tequest.POST)

        if form.is_valid():

            
            form.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

#Get is to read data. Post is to send data