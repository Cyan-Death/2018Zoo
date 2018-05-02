# Generated by Django 2.0.4 on 2018-05-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Story', '0006_auto_20180501_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationneighbors',
            name='direction',
            field=models.CharField(blank=True, choices=[('n', 'North'), ('s', 'South'), ('e', 'East'), ('w', 'West')], help_text='Select a Driection', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='locationneighbors',
            name='fromLocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fromLocation', to='Story.Location'),
        ),
        migrations.AlterField(
            model_name='locationneighbors',
            name='toLocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toLocation', to='Story.Location'),
        ),
    ]
