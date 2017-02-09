import zipfile
import tarfile
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):

    def get_full_name(self):
        full_name = super(User, self).get_full_name()
        return full_name or self.username

    def __unicode__(self):
        return self.username


def expire():
    return timezone.now() + timedelta(days=14)


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    proj_name = models.CharField(default='ProjectName', max_length=40, verbose_name='Project name')
    proj_file = models.FileField(null=True, upload_to='./uploaded_projects', verbose_name='Project file')
    upload_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=expire)

    def get_name(self):
        return self.name

    def extract(self):
        print self.proj_file.name
        print self.proj_file.file
        if self.proj_file.name.endswith('.zip'):
            zip_ref = zipfile.ZipFile(self.proj_file.file)
            zip_ref.extractall('./media/unzipped_projects')
            zip_ref.close()
        elif self.proj_file.name.endswith('.gz'):
            tar_ref = tarfile.open(fileobj=self.proj_file.file)
            tar_ref.extractall('./media/unzipped_projects')
            tar_ref.close()
        else:
            raise IOError('Unable to extract file.')

