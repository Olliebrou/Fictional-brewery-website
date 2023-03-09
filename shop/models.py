from django.db import models

# Create your models here.


class Beer(models.Model):
    beer_name = models.CharField(max_length=50)
    abv = models.FloatField()
    ibu = models.IntegerField()
    style = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.TextField(default="Description")
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.beer_name
