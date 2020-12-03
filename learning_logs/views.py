from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
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
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

#Get is to read data. Post is to send data
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=tpoic_id)
    if request.method !='POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic= topic
            new_entry.save()
            form.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'form': form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, edit_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form= EntryForm(instance= entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry':entry, 'topic': topic, 'form': form}
    return render(request,'learning_logs/edit_entry.html', context)
    