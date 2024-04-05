from django.db import models

# Create your models here.

# Create your models here.
class Owner(models.Model):
    FIO = models.CharField('ФИО', max_length=150)
    phone = models.CharField('Номер телефона', max_length=11)
    count_jobs_done = models.IntegerField('Количество выполненых заказов')
    date_of_registration = models.DateTimeField('Дата регистрации на сервисе')
    #vehicle_id = models.ForeignKey(Vehicle, on_delete= models.CASCADE)

    def __str__(self):
        return self.FIO+ " "+self.phone

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"
