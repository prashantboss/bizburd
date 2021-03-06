# Generated by Django 3.2 on 2022-05-11 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('contact_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testApp.contact')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
