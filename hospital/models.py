from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    hospitalName = models.CharField(max_length=20,null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    ) 
    BLOOD_CHOICES = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
        ('OTHER', 'OTHER'),
    )
    LANGUAGE_CHOICES = (
        ('HINDI', 'HINDI'),
        ('ENGLISH', 'ENGLISH'),
        ('MARATHI', 'MARATHI'),
        ('OTHER', 'OTHER'),
    )
     
    state_list = (
        ('Gujrat', 'Gujrat'),
        ('Maharashtra', 'Maharashtra'),
        ('Goa', 'Goa'),
        ('Bihar', 'Bihar'),
        ('Rajasthan', 'Rajasthan'),
        ('OTHER', 'OTHER'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    address_nd = models.CharField(max_length=40,null=True)
    mobile = models.CharField(max_length=20,null=False)
    mobile_nd = models.CharField(max_length=20,null=True)
    email= models.EmailField(null= True)
    aadhar = models.IntegerField(null=True)

    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)

    state= models.CharField(max_length=30,choices=state_list,default='Gujrat')
    city=models.CharField(max_length=200,null=True)
    pincode = models.IntegerField(null=True,default=000000)

    bloodGroup= models.CharField(max_length=10,choices=BLOOD_CHOICES,default='A+')
    dob     = models.DateField(null=True)
    gender  = models.CharField(max_length=6, choices=GENDER_CHOICES,default='Male')
    language  = models.CharField(max_length=15, choices=LANGUAGE_CHOICES,default='HINDI')
    
    motherName= models.CharField(max_length=200,null=True)
    fatherName= models.CharField(max_length=200,null=True)

    symptoms = models.CharField(max_length=100,null=False)
    allergy = models.CharField(max_length=100,null=True)
    pastMediacalRec = models.CharField(max_length=100,null=True)

    time= models.DateTimeField(default=datetime.now(), blank=True)
    hobby= models.TextField(null= True)
    other = models.TextField(null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


