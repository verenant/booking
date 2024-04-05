# Create your models here.
from django.db import models
from client.models import Client
from owner.models import Owner


# Create your models here.
class Feedback_owner(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    text = models.CharField('Текст отзыва', max_length=500)
    rating = models.IntegerField("Оценка")
    date_of_publication = models.DateTimeField('Дата публикации на сервисе')


    def __str__(self):
        return self.rating + " " + self.date_of_publication

    class Meta:
        verbose_name = "Отзыв_о_владельце"
        verbose_name_plural = "Отзывы_о_владельце"
