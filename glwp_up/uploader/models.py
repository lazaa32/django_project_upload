import os
import uuid
import zipfile
import tarfile
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


def expire():
    return timezone.now() + timedelta(days=14)

# def get_file_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (uuid.uuid4(), ext)
#     return os.path.join(settings.UPLOADED_DIR, filename)


class User(AbstractUser):
    num_of_projects = models.IntegerField(default=0)

    def increase(self):
        self.num_of_projects += 1
        self.save()

    def decrease(self):
        self.num_of_projects -= 1
        self.save()

    def get_num_of_projects(self):
        return self.num_of_projects


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    proj_name = models.CharField(default='ProjectName', max_length=40, verbose_name='Project name')
    proj_file = models.FileField(null=True, upload_to=settings.UPLOADED_DIR, verbose_name='Project file')
    upload_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=expire)

    def get_name(self):
        return self.name

    def extract(self):
        if self.proj_file.name.endswith('.zip'):
            zip_ref = zipfile.ZipFile(self.proj_file.file)
            zip_ref.extractall(os.path.join(settings.UNZIPPED_DIR, self.proj_name))
            zip_ref.close()
        elif self.proj_file.name.endswith('.gz'):
            tar_ref = tarfile.open(fileobj=self.proj_file.file)
            tar_ref.extractall(os.path.join(settings.UNZIPPED_DIR, self.proj_name))
            tar_ref.close()
        else:
            raise IOError('Unable to extract file.')

    def save(self, *args, **kwargs):
        self.user.increase()
        super(Project, self).save(*args, **kwargs)

    def delete(self, using=None):
        self.user.decrease()
        super(Project, self).delete(using)