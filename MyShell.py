import os
os.environ.setdefault('DJANGO_SETTING_MODULE','learning_log.settings')

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all()

for topic in topics:
    print('Topic ID:', topic.id, 'Topic:', topic)

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)


#Bring all the related entries in to play
entries = t.entry_set.all()

for entry in entries:
    print(entry)
    