from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_full_name(self):
        full_name = super(User, self).get_full_name()
        return full_name or self.username

    def __unicode__(self):
        return self.username


class Project(models.Model):
    name = models.TextField("project", primary_key=True)
    size = models.IntegerField()
    user = models.ForeignKey(User)
    update_date = models.DateTimeField("publish date")
    expire_date = models.DateTimeField("expiration date")

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size
