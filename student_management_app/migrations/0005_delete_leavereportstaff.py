# Generated by Django 3.2.18 on 2023-05-14 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_delete_leavereportstudent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
    ]
