from django.db import models

class mode(models.Model):  # Update the class name to `Mode` to match the convention
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)  # Ensure email is unique
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
