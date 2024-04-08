from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)




class CountryGDP(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=4)
    year=models.CharField(max_length=5)
    value=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
     return self.name
    


class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    img = models.ImageField(upload_to='images/', default=None)
    
#cascading dropdown
class Country(models.Model):
   name=models.CharField(max_length=50)
   def __str__(self):
      return self.name
class City(models.Model):
   country=models.ForeignKey(Country,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)
   def __str__(self):
      return self.name
   
class Person(models.Model):
   name=models.CharField(max_length=50)
   country=models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True)
   city=models.ForeignKey(City,on_delete=models.SET_NULL,blank=True,null=True)
   def __str__(self):
      return self.name


class InputInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
      return self.name
    
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    bio=models.CharField(max_length=50)
    def __str__(self):
      return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
      return self.name