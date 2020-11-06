from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    unit_cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'feed'

class Diet(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    consumption_rate = models.IntegerField(blank=True, null=True)

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'diet'


class Animal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cell_number = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    purchase_year = models.IntegerField(blank=True, null=True)
    home_country = models.CharField(max_length=100, blank=True, null=True)
    world_part = models.CharField(max_length=100, blank=True, null=True)
    climate = models.CharField(max_length=100, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    feed_quantity = models.IntegerField(blank=True, null=True)

    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    class Meta:
        db_table = 'animal'

    def __str__(self):
        return self.name + ' "' + self.nickname + '"'


class PeriodHistory(models.Model):
    date = models.DateField(blank=True, null=True)
    tickets_sold = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'period_history'


class Ticket(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ticket'

class SalesHistory(models.Model):
    date = models.DateField(blank=True, null=True)

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sales_history'


class User(models.Model):
    name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'
