# Generated by Django 4.2.7 on 2023-12-14 17:03

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ppost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хилы'), ('carry', 'ДД'), ('trader', 'Торговцы'), ('guild', 'Гилдмастеры'), ('quest', 'Квестгиверы'), ('blacksmith', 'Кузнецы'), ('tanner', 'Кожевники'), ('potion', 'Зельевары'), ('caster', 'Мастера заклинаний')], default='tank', max_length=10)),
                ('text', ckeditor.fields.RichTextField()),
                ('date_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rresponce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.ppost')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
