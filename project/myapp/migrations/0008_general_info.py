# Generated by Django 3.2.7 on 2021-11-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_election_candidate_master_place_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='general_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1500)),
                ('g_type', models.CharField(max_length=150)),
                ('path', models.CharField(max_length=250)),
            ],
        ),
    ]
