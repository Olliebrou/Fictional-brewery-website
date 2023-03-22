from django.db import models

# Create your models here.


class Beer(models.Model):
    """
            A Django model representing a beer product object.

            :param beer_name: Name of the beer, up to 50 characters.
            :type beer_name: str
            :param abv: Alcohol by volume percentage of the beer.
            :type abv: float
            :param ibu: International Bitterness Units of the beer.
            :type ibu: int
            :param style: Style of the beer, up to 100 characters.
            :type style: str
            :param price: Price of the beer in Rands.
            :type price: int, optional
            :param desc: Description of the beer.
            :type desc: str, optional
            :param image: Image of the beer.
            :type image: str, optional

            :return: A Beer object.
            :rtype: Beer

            :Methods:
                `__str__(self):` Returns the name of the beer as a string.
            """
    beer_name = models.CharField(max_length=50)
    abv = models.FloatField()
    ibu = models.IntegerField()
    style = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.TextField(default="Description")
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.beer_name
