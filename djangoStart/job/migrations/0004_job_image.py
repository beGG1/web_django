# Generated by Django 4.0.3 on 2022-04-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_comment_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='job_images/', verbose_name='Ссылка картинки'),
        ),
    ]
