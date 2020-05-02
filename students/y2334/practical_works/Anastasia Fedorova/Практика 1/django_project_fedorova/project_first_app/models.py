from django.db import models


# Create your models here.
class Deus(models.Model):  # class owner
    first_name = models.CharField(max_length=88)
    last_name = models.CharField(max_length=88)
    date_of_birth = models.DateField()


class Machina(models.Model):  # class car
    car_made = models.CharField(max_length=88)
    car_model = models.CharField(max_length=88)
    colour = models.CharField(max_length=88)
    govnum = models.CharField(max_length=8)


class ExMachina(models.Model):  # class ownership
    ownership_opened = models.DateField()
    ownership_closed = models.DateField()
    owner = models.ForeignKey('Deus', on_delete=models.CASCADE)
    car = models.ForeignKey('Machina', on_delete=models.CASCADE)


class License(models.Model):  # class driver's license
    license_no = models.IntegerField(default=9031993)
    issue_date = models.DateField(auto_now_add=True)
    extypes = (
        ('A', 'A'),
        ('A1', 'A1'),
        ('B', 'B'),
        ('B1', 'B1'),
        ('BE', 'BE'),
        ('C', 'C'),
        ('C1', 'C1'),
        ('CE', 'CE'),
        ('C1E', 'C1E'),
        ('D', 'D'),
        ('D1', 'D1'),
        ('DE', 'DE'),
        ('D1E', 'D1E'),
        ('M', 'M'),
        ('Tm', 'Tm'),
        ('Tb', 'Tb')
    )
    license_type = models.CharField(max_length=3, choices=extypes)
    driver = models.ForeignKey('Deus', on_delete=models.CASCADE)
