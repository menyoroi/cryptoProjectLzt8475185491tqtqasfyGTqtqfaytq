from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=60, null=False)
    short_name = models.CharField(max_length=10, null=False, unique=True)
    img = models.CharField(max_length=400, null=False)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'Asset {self.id}'


class User(models.Model):
    email = models.CharField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f'User {self.id}'


class UserAdmin(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f'UserAdmin {self.id}'


class UserToken(models.Model):
    email = models.CharField(max_length=200, null=False)
    token = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f'UserToken {self.id}'