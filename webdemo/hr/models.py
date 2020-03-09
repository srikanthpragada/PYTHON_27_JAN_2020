from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.IntegerField()

    def  __str__(self):
        return self.title + "," + str(self.price)
