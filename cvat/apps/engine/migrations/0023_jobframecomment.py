# Generated by Django 2.2.8 on 2020-03-14 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0022_auto_20191004_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobFrameComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='engine.Job')),
            ],
        ),
    ]