# Generated by Django 4.2.5 on 2023-10-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='username',
        ),
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default=None, max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]