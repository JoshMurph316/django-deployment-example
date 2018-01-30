from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=35, unique=True)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)
