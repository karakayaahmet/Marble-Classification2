# Generated by Django 4.1 on 2022-12-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marble", "0007_alter_image_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resimler",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="media")),
                ("title", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Image",
        ),
    ]
