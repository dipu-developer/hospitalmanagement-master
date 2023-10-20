from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
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
    # assignedDoctorId = models.PositiveIntegerField(null=True)
    aadhar = models.BigIntegerField(null=True,default=000000000000)

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
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
