from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    class Meta:
        db_table="Student"

    def __str__(self):
        return self.firstname + ' '+self.lastname


class Employer(models.Model):
    Name = models.CharField( max_length=50)
    Position = models.CharField( max_length=50)
    age = models.IntegerField()
    State_date = models.DateField()
    Salary = models.IntegerField()

    class Meta:
        db_table = "Employer"

    def __str__(self):
        return self.Name



class flow(models.Model):

    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    Businessemail = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    Jobtitle = models.CharField(max_length=50)


    class Meta:
        db_table = "flow"

    def __str__(self):
        return self.firstname+' '+ self.lastname



class venue(models.Model):

    venuename = models.CharField( max_length=66)
    Address = models.CharField( max_length=60)
    Zip = models.IntegerField()
    Contact_number = models.IntegerField()
    webaddress = models.CharField(max_length=90)
    Emailaddress = models.CharField(max_length=59)


    class Meta:
        db_table = "venue"

    def __str__(self):
        return self.venuename + ' ' + self.Address