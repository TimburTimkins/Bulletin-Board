from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# class User(models.Model):
#     name = models.CharField(max_length = 50)
#
#     def __str__(self):
#         return f'{self.name.title()}'


class Ppost(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('carry', 'ДД'),
        ('trader', 'Торговцы'),
        ('guild', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('blacksmith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('caster', 'Мастера заклинаний'),
    )
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length=10, choices=TYPE, default='tank')
    text = RichTextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title.title()}: {self.category}, {self.text}'

    def get_absolute_url(self):
        return reverse('boarddetail', args=[str(self.id)])


class Rresponce(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models. ForeignKey(Ppost, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
