from django.db import models

# Create your models here.

# addition

class Wizard(models.Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):

        return f'{self.name}, a {self.status} {self.type}'

    @classmethod
    def create(cls, name, type, status):

        wiz = Wizard(name=name, type=type, status=status)

        wiz.save()

        return wiz

    def to_json(self):
        return {
            "name": self.name,
            "type": self.type,
            "status": self.status
        }