# Generated by Django 4.2.1 on 2024-04-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizhnii', '0003_alter_interestingplacesmodel_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]