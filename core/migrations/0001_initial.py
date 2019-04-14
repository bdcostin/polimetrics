# Generated by Django 2.2 on 2019-04-14 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('party', models.CharField(max_length=32)),
                ('about', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='core/static/img')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.IntegerField(blank=True, null=True)),
                ('positive', models.IntegerField(blank=True, null=True)),
                ('negative', models.IntegerField(blank=True, null=True)),
                ('highest', models.IntegerField(blank=True, null=True)),
                ('lowest', models.IntegerField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Candidate')),
            ],
        ),
    ]
