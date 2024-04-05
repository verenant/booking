# Create your models here.
from django.db import models

from client.models import Client
from vehicle.models import Vehicle

# Create your models here.
class Feedback_vehicle(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    text = models.CharField('Текст отзыва', max_length=500)
    rating = models.IntegerField("Оценка")
    date_of_publication = models.DateTimeField('Дата публикации на сервисе')


    def __str__(self):
        return self.rating + " " + self.date_of_publication

    class Meta:
        verbose_name = "Отзыв_о_технике"
        verbose_name_plural = "Отзывы_о_технике"

# class Client(Client):
#     pass