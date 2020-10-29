from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default= 1)
    name = models.CharField(max_length=50)
    field_of_activity = models.CharField(max_length=50)
    address = models.TextField()
    information = models.TextField()



class Vacancy (models.Model):
    profession = models.CharField(max_length=100)
    busy_time = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    salary = models.IntegerField()
    information = models.TextField()
    date_of_application = models.DateTimeField(auto_now_add=True)
    id_employer = models.ForeignKey(Employer, unique=False, on_delete=models.DO_NOTHING, default=None)


class Job_seeker (models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.DO_NOTHING)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, default= 1)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Job_seeker.objects.create(user=instance)

    @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    def save_profile(sender, instance, created, **kwargs):
        user = instance
        if created:
            profile = Job_seeker(user=user)
            profile.save()


class Summary(models.Model):
    profession = models.CharField(max_length=100)
    busy_time = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    information = models.TextField(default="information")
    desired_salary = models.IntegerField()
    date_of_application = models.DateTimeField(auto_now_add=True)
    id_job_seeker = models.ForeignKey(Job_seeker, unique=False, on_delete=models.DO_NOTHING, default=None)


class Response (models.Model):
    id_summary = models.ForeignKey(Summary, unique=False, on_delete=models.DO_NOTHING, default=None)
    id_vacancy = models.ForeignKey(Vacancy, unique=False, on_delete=models.DO_NOTHING, default=None)
    total = models.CharField(max_length=50)
    date_of_application = models.DateTimeField(auto_now_add=True)