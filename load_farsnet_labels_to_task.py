from cvat.apps.engine.models import Label, Task
import json
import random

TASK_ID = '6'
LABEL_SIZE = 5000

task = Task.objects.get(pk=TASK_ID)

label_l = []

with open('farsnet-words-list.json') as f:
    label_list = json.load(f)
    label_list.sort(key = len)
    label_l = []
    for label in label_list:
        label_l.append(Label(task=task, name=label))

Label.objects.filter(task=task).delete()
Label.objects.bulk_create(random.sample(label_l, LABEL_SIZE))
