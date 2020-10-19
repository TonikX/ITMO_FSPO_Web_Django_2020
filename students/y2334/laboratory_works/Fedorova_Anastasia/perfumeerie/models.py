# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Broker(models.Model):
    broker_id = models.AutoField(primary_key=True)
    broker_name = models.CharField(max_length=45)
    broker_addr = models.CharField(max_length=90, blank=True, null=True)
    broker_dob = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'broker'


class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    buyer_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'buyer'


class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_date = models.DateField()
    deal_sold = models.IntegerField()
    fk_broker = models.ForeignKey(Broker, models.DO_NOTHING)
    fk_product = models.ForeignKey('Product', models.DO_NOTHING)
    fk_buyer = models.ForeignKey(Buyer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'deal'


class DeleteLog(models.Model):
    user_host = models.CharField(max_length=50)
    table_name = models.CharField(max_length=50)
    time_delete = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delete_log'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45)
    product_type = models.CharField(max_length=45)
    product_best_before = models.DateField()
    product_price = models.IntegerField()
    product_in_stock = models.IntegerField()
    fk_seller = models.ForeignKey('Seller', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'seller'


class Supply(models.Model):
    supply_id = models.AutoField(primary_key=True)
    supply_date = models.DateField()
    supply_lot = models.IntegerField()
    supply_piece_price = models.IntegerField()
    fk_product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supply'
