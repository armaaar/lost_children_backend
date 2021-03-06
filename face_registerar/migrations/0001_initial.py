# Generated by Django 3.2.5 on 2021-07-19 10:38

from django.db import migrations, models
import face_registerar.models.kid_image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KidImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=face_registerar.models.kid_image.kid_image_update_path)),
                ('date_time', models.DateTimeField(verbose_name='date the image was uploaded in')),
            ],
        ),
    ]
