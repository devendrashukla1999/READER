# Generated by Django 4.0.3 on 2022-05-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_contact_contnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]