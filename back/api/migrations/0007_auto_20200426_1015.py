# Generated by Django 3.0.5 on 2020-04-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200426_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybooks',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='saved', to='api.Book'),
        ),
    ]
