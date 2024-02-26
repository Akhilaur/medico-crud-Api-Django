from django.db import models

    

# Create your models here.
class medicalmedicines(models.Model):
    medicine_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    date = models.DateField(blank=True,  null=True,) 
    amount = models.IntegerField()
    

    
    class Meta:
        db_table='medicalmedicines'

   
    

    
    #def __str__(self) :
    #     return self.medicine_name
    
# class medicine_details_Test(models.Model):
#     medicine_details_Test = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.medicine_details_Test






