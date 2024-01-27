from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
    last_name = models.CharField(max_length=50, verbose_name = 'Last Name')
    email = models.EmailField()
    phone_number = models.CharField(max_length = 12, verbose_name = 'Phone No')
    instrument_type = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.first_name


