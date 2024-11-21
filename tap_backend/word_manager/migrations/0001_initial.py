# Generated by Django 5.1.3 on 2024-11-20 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='word_manager.word')),
            ],
        ),
        migrations.CreateModel(
            name='WordList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='word_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='word_manager.wordlist'),
        ),
    ]