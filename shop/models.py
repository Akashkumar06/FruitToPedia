from django.db import models
# Create your models here.
class Team(models.Model):
    product_id = models.AutoField
    person_name = models.CharField(max_length=50)
    person_des = models.CharField(max_length=500)
    person_role = models.CharField(max_length=50, default="")
    person_picture = models.ImageField(upload_to='imeges', default="")
    linkinsta=models.URLField(max_length=500,default="")
    linklinked=models.URLField(max_length=500,default="")
    linkgit=models.URLField(max_length=500,default="")
  
   

    def __str__(self):
        return self.person_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    fullname= models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    msg = models.CharField(max_length=500)


    def __str__(self):
        return self.fullname