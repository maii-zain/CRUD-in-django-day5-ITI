from django.db import models

class Emp(models.Model):
    emp_name=models.CharField( max_length=50)
    salary=models.IntegerField()
    title=models.CharField( max_length=50)
    team=models.ForeignKey( "Team", on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.emp_name
    
class Team(models.Model):
    name=models.CharField( max_length=15)
    manager=models.ForeignKey(Emp,on_delete=models.CASCADE,related_name="team_manager")
    def __str__(self):
        return self.name
   
    

# Create your models here.
