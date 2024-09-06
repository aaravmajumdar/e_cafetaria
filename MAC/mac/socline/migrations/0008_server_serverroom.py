# Generated by Django 5.0.1 on 2024-02-28 01:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socline', '0007_remove_serverroom_post_remove_serverroom_parent_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('serverno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('slug', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='ServerRoom',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socline.serverroom')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socline.server')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
