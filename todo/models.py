from django.db import models

# Create your models here.
# inherit django's base model class
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    # django creates the id PK field

    # override django's built in attribute naming convention 
    def __str__(self):
        return self.name