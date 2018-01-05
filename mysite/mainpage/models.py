from django.conf import settings
from django.db import models

# Create your models here.
class Currency(models.Model):
    symbol = models.CharField(max_length = 5)
    name = models.CharField(max_length = 10)
    icon_absolute_link = models.CharField(max_length = 255)
    icon_relative_link = models.CharField(max_length = 255)

class UserLogin(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    login_ip = models.CharField(max_length = 255)
    browser_info = models.CharField(max_length = 255)
    cookies = models.CharField(max_length = 255)

class Account(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_location = models.CharField(max_length = 255)
    last_password_modified_time = models.DateTimeField()
    last_login_ip = models.CharField(max_length = 255)
    last_login_ip_location = models.CharField(max_length = 255)
    total_buy_sell_deposit_withdraw = models.IntegerField()
    phone_number = models.CharField(max_length = 255)
    national_id_proof = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)

class BankAccount(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bank_account_number = models.CharField(max_length = 255)
    user_fullname_as_in_bank = models.CharField(max_length = 255)
    ifsc_code = models.CharField(max_length = 255)
    name_of_the_bank = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    swift_code = models.CharField(max_length = 255)
    iban = models.CharField(max_length = 255)

class PriceHistory(models.Model):
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(True)

class Order(models.Model):
    value = models.FloatField()
    type = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255)
    timestamp = models.DateTimeField(True)
