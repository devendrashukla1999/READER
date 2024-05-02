# Generated by Django 4.0.3 on 2022-05-05 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnum', models.PositiveBigIntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('pimg', models.ImageField(default='static/default/default.jpg', upload_to='mdedia/profilepics')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]