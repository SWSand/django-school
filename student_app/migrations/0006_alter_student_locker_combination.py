# Generated by Django 5.0.3 on 2024-03-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_alter_student_good_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='00-00-00', max_length=255),
        ),
    ]
