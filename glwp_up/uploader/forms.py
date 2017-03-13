import os
from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_file']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProjectForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.get_num_of_projects() >= settings.MAX_NUM_OF_PROJECT and self.user.get_username() != 'admin':
            raise forms.ValidationError(_('User has already too many projects uploaded. Max number of uploaded projects'
                                        ' is %d.' % settings.MAX_NUM_OF_PROJECT))
        try:
            file = self.cleaned_data['proj_file']
            if file:
                destination = settings.UPLOADED_DIR
                print 'destination:'
                print os.path.join(destination, file.name)
                print os.path.isfile(os.path.join(destination, file.name))
                if os.path.isfile(os.path.join(destination, file.name)):
                    raise forms.ValidationError(_('A file with the name "'+file.name+'" already exists. Please, '
                                                'rename your file and try again.'))

                file_type = file.content_type.split('/')[-1]
                if file_type in settings.TASK_UPLOAD_FILE_TYPES:
                    if file._size > settings.TASK_UPLOAD_FILE_MAX_SIZE:
                        raise forms.ValidationError(_('Please keep file size under %s. Current file size %s') %
                                                    (filesizeformat(settings.TASK_UPLOAD_FILE_MAX_SIZE),
                                                     filesizeformat(file._size)))
                else:
                    raise forms.ValidationError(_('File type not supported.'))
        except KeyError:
            raise forms.ValidationError(_('No file selected.'))
