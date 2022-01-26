from djongo import models


# Create your models here.

class chatphone_items(models.Model):
    names = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    price = models.IntegerField()
    selled = models.BooleanField(default=False)

    def __str__(self):
        return self.names
