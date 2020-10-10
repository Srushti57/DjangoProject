from django.db import models

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=30)
    expiry_date_time = models.DateField()

    def __str__(self):
        return self.company_name