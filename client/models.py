from django.db import models

# Create your models here.

# Create your models here.
class Client(models.Model):
    FIO = models.CharField('ФИО', max_length=150)
    phone = models.CharField('Номер телефона', max_length=11)
    count_orders = models.IntegerField('Количество заказов')
    date_of_registration = models.DateTimeField('Дата регистрации на сервисе')

    def __str__(self):
        return self.FIO+ " "+self.phone

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
