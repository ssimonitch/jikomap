from django.db import models

class Customer(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('説明', max_length=50)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '事故発生場所'
        verbose_name_plural = '事故発生場所'


# Create your models here.
