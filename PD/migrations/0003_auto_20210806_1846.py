# Generated by Django 3.2 on 2021-08-06 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PD', '0002_auto_20210806_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Disease',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='FirstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='LastName',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='MedsStarted',
            new_name='medsstarted',
        ),
    ]