# Generated by Django 5.0.3 on 2024-03-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_student_good_student_student_locker_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=100),
        ),
    ]