# Generated by Django 2.2.10 on 2020-07-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_tag_main_tag_for_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='scopes', through='articles.Article_Tag', to='articles.Article'),
        ),
    ]
