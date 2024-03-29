# Generated by Django 5.0.3 on 2024-03-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0007_alter_student_locker_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
