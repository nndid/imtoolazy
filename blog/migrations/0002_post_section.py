# Generated by Django 4.2 on 2023-04-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('section1', 'Section 1'), ('section2', 'Section 2')], max_length=50, null=True),
        ),
    ]
