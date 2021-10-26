from djongo import models

# Create your models here.
class ISCO(models.Model):
    id = models.ObjectIdField()
    Group = models.TextField()
    Name = models.TextField()
    Description = models.TextField()

class JobAnalysis(models.Model):
    id = models.ObjectIdField()
    Career = models.TextField()
    HardSkill = models.TextField()
    SoftSkill = models.TextField()
    Personality = models.TextField()