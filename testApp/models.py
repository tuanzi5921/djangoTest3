from django.db import models

# Create your models here.

class User(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=30)
        age = models.IntegerField()
        city = models.CharField(default='shanghai',max_length=80)

        def __str__(self):
                return 'User<id=%s,name=%s,age=%s>'%(self.id,
                                                     self.name,
                                                     self.age)
