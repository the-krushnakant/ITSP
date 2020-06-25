from django.db import models

# Create your models here.
class Team(models.Model):
    team_id=models.CharField(max_length=10 , unique=True)
    team_name=models.CharField(max_length=40)
    member1=models.CharField(max_length=50)
    member2=models.CharField(max_length=50)
    member3=models.CharField(max_length=50)
    member4=models.CharField(max_length=50)

    def __str__(self):
        return self.team_id 