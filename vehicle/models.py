from django.db import models
from owner.models import Owner
# Create your models here.

# Create your models here.
class Vehicle(models.Model):

    model = models.CharField('Модель', max_length=50)
    type = models.CharField('Тип техники', max_length=11)
    description = models.CharField('Описание', max_length=150)
    rating = models.IntegerField('Рейтинг', null=True)
    year_of_production = models.CharField('Год выпуска', max_length=4)
    #timetable = models.CharField('Бронирование', max_length=1)
    count_jobs_done = models.IntegerField('Количество выполненых заказов')
    date_of_registration = models.DateTimeField('Дата регистрации на сервисе')
    owner_id = models.ForeignKey(Owner, on_delete= models.CASCADE)
    images = models.ImageField(blank=True)


    def __str__(self):
        return self.model + " " + self.type

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"

class PostImage(models.Model):
    post = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
    LastInsertId = (Vehicle.objects.last()).id+1
    images = models.FileField(upload_to=f'images_{LastInsertId}/')

    def __str__(self):
        return self.post.model
