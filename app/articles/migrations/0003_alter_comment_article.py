# Generated by Django 3.2.3 on 2021-06-03 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="articles.article",
            ),
        ),
    ]
