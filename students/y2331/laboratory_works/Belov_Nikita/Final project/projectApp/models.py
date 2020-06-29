from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

# Create your models here.


class ExtendedUserModel(AbstractUser):
    password = models.CharField('password', max_length=128)
    last_login = models.DateTimeField('last login', blank=True, null=True)
    first_name = models.CharField('first name', max_length=50, blank=False, null=False)
    last_name = models.CharField('last name', max_length=50, blank=False, null=False)
    jobs = (('', '---'), ('CPT', 'captain'), ('SLR', 'sailor'), ('ACC', 'accountant'))
    job_type = models.CharField(choices=jobs, default='sailor', blank=False, null=False, max_length=20)
    b_day = models.DateField(null=False, blank=False, default='1970-01-03')
    hire_date = models.DateField(null=False, blank=False, default='1970-01-03')

    fieldsets = ('Custom fields set', {'fields': ('username', 'first_name', 'job_type')})
    search_field = ('username', 'first_name', 'job_type')

    class Meta:
        permissions =[
            ("add_voyage", "You can add voyage as a captain"),
            ("see_ship_info", "You can see info about ship"),
            ("see_award", "You can see awards"),
            ("see_fish_op", "You have access to stock operations"),
            ("edit_ship_info", "You have access to ship operations"),
            ("edit_crews", "You have access to crew management")
        ]

    def __str__(self):
        job = {}
        if self.job_type == 'CPT':
            job = 'captain'
        elif self.job_type == 'SLR':
            job = 'sailor'
        else: job = ''

        return str(self.first_name + " " + self.last_name + "(" + job + ")")


class Trawlers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    prodDate = models.DateField(null=False, blank=False, default='1970-01-03')

    def __str__(self):
        return self.name


class Voyage(models.Model):
    id = models.AutoField(primary_key=True)
    tId = models.ForeignKey(Trawlers, on_delete=models.CASCADE)
    startDate = models.DateField(null=False, blank=False, default='1970-01-03')
    endDate = models.DateField(null=False, blank=False, default='1970-01-03')
    fishQty = models.IntegerField(null=False, blank=False)


class FishOperation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=False, blank=False, default='1970-01-03')
    price = models.IntegerField()


class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    uId = models.ForeignKey(ExtendedUserModel, on_delete=models.CASCADE)
    awardSize = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False, default='1970-01-03')


class Crews(models.Model):
    tId = models.ForeignKey(Trawlers, on_delete=models.CASCADE)
    uId = models.OneToOneField(ExtendedUserModel, on_delete=models.CASCADE, unique=True)