from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name', 'proj_file']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProjectForm, self).__init__(*args, **kwargs)

    def clean(self):
        file = self.cleaned_data['proj_file']
        try:
            if file:
                file_type = file.content_type.split('/')[-1]

                if file_type in settings.TASK_UPLOAD_FILE_TYPES:
                    if file._size > settings.TASK_UPLOAD_FILE_MAX_SIZE:
                        raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') %
                                                    (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
                else:
                    raise forms.ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass
