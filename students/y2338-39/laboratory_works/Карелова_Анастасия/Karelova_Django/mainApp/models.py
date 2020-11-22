from django.db import models

TypesForLawyer = (
    ('a', 'Advice'),
    ('c', 'Crash'),
    ('d', 'Divorce'),
)

TypesForStatus = (
    ('f', 'Free'),
    ('b', 'Busy'),
)

TypesForDeal = (
    ('r', 'Resolved'),
    ('n', 'Not resolved')
)


class Lawyer(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=1, choices=TypesForLawyer)
    passport = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=45)
    passport = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)


class CurrentClient(models.Model):
    name = models.CharField(max_length=45)
    passport = models.BigIntegerField()
    phone = models.BigIntegerField()


class Deal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    date_opened = models.DateField()
    date_closed = models.DateField(null=True, blank=True)
    status_lawyer = models.CharField(max_length=1, choices=TypesForStatus)


class Meeting(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    date = models.DateField()
    status_deal = models.CharField(max_length=1, choices=TypesForDeal)


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    pay_sum = models.IntegerField()
    date = models.DateField(null=True, blank=True)
