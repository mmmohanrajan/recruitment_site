from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    key_skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    job_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Employee(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+919999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(unique=True, validators=[phone_regex], max_length=17) 
    email = models.EmailField(max_length=70, unique= True)
    is_accepted = models.NullBooleanField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    experience = models.CharField(max_length=10)
    designation = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, related_name='experience', on_delete=models.CASCADE)


class Education(models.Model):
    degree = models.CharField(max_length=10)
    university = models.CharField(max_length=50)
    year = models.CharField(max_length=100)
    percentage = models.CharField(max_length=5)
    employee = models.ForeignKey(Employee, related_name='education', on_delete=models.CASCADE)