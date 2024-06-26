# Generated by Django 4.2.6 on 2023-10-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroapp', '0003_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='suggestions',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='feedback',
            table='feedback_table',
        ),
    ]
