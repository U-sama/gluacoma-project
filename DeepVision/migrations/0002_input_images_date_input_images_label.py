# Generated by Django 4.1.4 on 2022-12-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DeepVision", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="input_images",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="input_images",
            name="label",
            field=models.CharField(max_length=50, null=True),
        ),
    ]