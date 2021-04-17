from django.db import models


class ApacheLog(models.Model):
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True,verbose_name = 'ip адрес')
    data_time = models.DateTimeField(verbose_name='Дата')
    method = models.CharField(max_length=10,verbose_name='Метод')
    url = models.URLField(verbose_name='URL')
    status_code = models.IntegerField(verbose_name='Код ответа')
    size = models.IntegerField(verbose_name='Размер')

    class Meta:
        verbose_name_plural = 'Записи лога'
        verbose_name = 'Запись лога'
        ordering = ['-data_time']

# Create your models here.
