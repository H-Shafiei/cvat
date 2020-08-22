import json
from cvat.apps.engine.models import *
from django.db.models import *

task_ids = [17, 18, 19, 20, 28, 29, 30, 31, 32]

labeled_shapes = LabeledShape.objects.filter(label=OuterRef('pk')).values('label')
total_shapes = labeled_shapes.annotate(count=Count('pk')).values('count')

labels = Label.objects.filter(task__in=task_ids).annotate(
    shapes_count=Subquery(total_shapes)).filter(shapes_count__gte=1).values('name').annotate(
    count=Sum('shapes_count')).order_by('-count')

labels_data = []
for label in labels:
    labels_data.append({"label": label['name'], "count": int(label['count'])})

with open('label-data.json', 'w', encoding='utf-8') as f:
    json.dump(labels_data, f, ensure_ascii=False)
