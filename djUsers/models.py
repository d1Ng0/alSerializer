from django.db import models

class UserModel(models.Model):
    """
    Model class for USERS on the SQLITE db
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return "{} {} {} {}".format(self.name,self.surname, self.phone, self.address)