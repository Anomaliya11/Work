# Generated by Django 4.1.6 on 2023-02-16 09:55

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('page_num', models.PositiveBigIntegerField()),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'published',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Wrong', regex='^.*em$')], verbose_name='Имя автора')),
                ('age', models.PositiveBigIntegerField(verbose_name='Возраст автора')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта автора')),
                ('lit_type', models.CharField(choices=[('a', 'foreign'), ('b', 'domestic'), ('c', 'other')], default='a', max_length=1, verbose_name='Тип литературы')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['id'],
                'unique_together': {('name', 'age')},
            },
        ),
    ]
