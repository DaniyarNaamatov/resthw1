# Generated by Django 4.0.5 on 2022-06-24 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movies",
                to="movie_app.director",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="movie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="movie_app.movie",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                default=1,
                null=True,
            ),
        ),
    ]
