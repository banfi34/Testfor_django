# Generated by Django 4.1.5 on 2023-01-24 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=30, verbose_name='page name')),
                ('page_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('web', models.URLField(blank=True, null=True, verbose_name='website page')),
                ('auth_users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
