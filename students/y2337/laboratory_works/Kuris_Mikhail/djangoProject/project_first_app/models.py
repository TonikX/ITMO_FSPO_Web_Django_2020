from django.db import models


class Organizations(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    surname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class Items(models.Model):
    title = models.CharField(max_length=255)
    sort = models.CharField(max_length=255)
    variety = models.IntegerField()
    prise = models.FloatField()
    organizations = models.ForeignKey(Organizations, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Fair(models.Model):
    fair_title = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.fair_title


class Results(models.Model):
    TYPE_CHOICES = (
        ('Оптовик', 'Оптовик'),
        ('Частное лицо', 'Частное лицо'),
        ('Учреждение', 'Учреждение')
    )
    item = models.OneToOneField(Items, on_delete=models.CASCADE, primary_key=True)
    organizations = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    fair = models.ForeignKey(Fair, on_delete=models.CASCADE)
    sell_variety = models.IntegerField()
    sell_prise = models.FloatField()
    buyer = models.CharField(max_length=255, choices=TYPE_CHOICES)