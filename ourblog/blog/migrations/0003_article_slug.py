# Generated by Django 3.1.4 on 2021-07-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]