# Generated by Django 4.0.3 on 2022-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Books_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('Discription', models.TextField()),
                ('image', models.ImageField(upload_to='media/Booksimages')),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
