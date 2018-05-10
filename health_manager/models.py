from django.db import models
import datetime
# Create your models here.
class Weight(models.Model):
    lb= models.DecimalField(max_digits=5,decimal_places=2)
    datetime = models.DateTimeField()
    def __str__(self):
        return self.datetime.strftime("%Y-%m-%d")+'\tweight:'+str(self.lb)
