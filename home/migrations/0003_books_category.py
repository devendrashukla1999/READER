# Generated by Django 4.0.3 on 2022-04-25 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
