# Generated by Django 4.2 on 2023-04-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_topic',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.topic', verbose_name='topic'),
        ),
    ]