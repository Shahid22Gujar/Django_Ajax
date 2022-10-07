from django.db import models

# Create your models here.
class CustomUser(models.Model):
    user_id=models.AutoField(primary_key=True)  
    name=models.CharField(max_length=200,blank=False, verbose_name="Name")
    phone=models.CharField(max_length=12,blank=False, verbose_name="Phone")
    name=models.CharField(max_length=200,blank=False, verbose_name="Name")

    def __str__(self) -> str:
        return self.name
