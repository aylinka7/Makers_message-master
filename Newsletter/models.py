from django.db import models
from django.conf import settings



class Subscriber(models.Model):
    name = models.TextField(verbose_name='Имя', max_length=50, db_index=True, blank=False)
    surname = models.TextField(verbose_name='Фамилия', max_length=50, db_index=True, blank=False)
    date_birth = models.DateField(verbose_name='Дата рождения', max_length=25, blank=True)
    number = models.CharField(verbose_name='Номер телефона', max_length=15)
    e_mail = models.EmailField(verbose_name='E-Mail', max_length=250, db_index=True, blank=False)
    course_id = models.CharField(verbose_name='Группа', max_length=250, blank=True, db_index=True)