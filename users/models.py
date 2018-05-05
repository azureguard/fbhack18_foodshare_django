from django.db import models

class UserManager(models.Manager):
    def create_user(self, name, university, address, email, password):
        user = self.create(name = name, university = university, address = address,
                           email = email, password = password)
        return user

class User(models.Model):
    UNI_CHOICES = (('UniMelb', 'University of Melbourne'),
                   ('RMIT','Royal Melbourne Institute of Technology'),
                   ('Monash', 'Monash University'))
    name = models.CharField(max_length= 70)
    univeristy = models.CharField(max_length= 10, choices= UNI_CHOICES)
    address = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 255)
    password = models.CharField(max_length = 50)
    credit = models.IntegerField(default= 100)

    objects = UserManager