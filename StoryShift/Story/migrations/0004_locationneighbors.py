# Generated by Django 2.0.4 on 2018-04-25 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Story', '0003_characters'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationNeighbors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=200)),
                ('fromLocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Story.Location')),
                ('toLocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='neighbors_of', to='Story.Location')),
            ],
        ),
    ]