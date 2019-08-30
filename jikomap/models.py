from django.db import models

class Item(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('軽度', max_digits=9, decimal_places=6)


    def __str__(self):
        return str(self.name)
    

    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'


# Create your models here.