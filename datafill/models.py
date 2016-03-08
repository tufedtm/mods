# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from choices import MAGAZINES_CHOICES, YEAR_CHOICES, MONTH_CHOICES


class CreatedUpdated(models.Model):
    created = models.DateTimeField('Запись создана', auto_now_add=True)
    updated = models.DateTimeField('Запись обновлена', auto_now=True)

    class Meta:
        abstract = True


class Magazine(CreatedUpdated):
    title = models.CharField('Название', choices=MAGAZINES_CHOICES, default='IM', max_length=50)
    number = models.PositiveSmallIntegerField('Номер')
    public_year = models.PositiveSmallIntegerField('Год выхода', choices=YEAR_CHOICES, default=datetime.now().year)
    public_month = models.PositiveSmallIntegerField('Месяц выхода', choices=MONTH_CHOICES, default=datetime.now().month)
    cover = models.ImageField('Обложка', upload_to='magazine/cover')

    def __unicode__(self):
        return '%s %s' % (self.get_title_display(), self.number)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'


class Game(CreatedUpdated):
    title = models.CharField('Название', max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Patch(CreatedUpdated):
    magazine = models.ForeignKey(Magazine)
    game = models.ForeignKey(Game, verbose_name='Название игры')
    version = models.CharField('Версия', max_length=10)
    description = models.TextField('Описание')

    def __unicode__(self):
        return '%s %s' % (self.game, self.version)

    class Meta:
        ordering = ['title']
        verbose_name = 'Патч'
        verbose_name_plural = 'Патчи'
