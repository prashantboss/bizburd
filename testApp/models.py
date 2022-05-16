from django.db import models

# Create your models here.
class AbstractDateTrackedModel(models.Model):
    created_date = models.DateTimeField(("date created"), auto_now_add=True)
    updated_date = models.DateTimeField(("date modified"), auto_now=True)

    class Meta:
        abstract = True
        
        
class Contact(AbstractDateTrackedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, unique=True)
    address =  models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Group(AbstractDateTrackedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    contacts = models.ManyToManyField(Contact, null=True, blank=True)
    
    def __str__(self):
        return self.name