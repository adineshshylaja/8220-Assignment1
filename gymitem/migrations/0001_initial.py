# Generated by Django 2.2 on 2021-02-01 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gymitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gymitem_name', models.CharField(max_length=100)),
                ('Gymitem_id', models.CharField(blank=True, max_length=100)),
                ('Gymitem_description', models.TextField()),
                ('Gymitem_category', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]