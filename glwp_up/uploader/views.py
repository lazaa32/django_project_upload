import os
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.core.servers.basehttp import FileWrapper
from .forms import ProjectForm
from .models import Project


def upload_file(request):
    if request.method == 'POST':
        form = ProjectForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            f.extract()

            return redirect('/uploader/projects')
    else:
        form = ProjectForm(request.user)

    return render_to_response('uploader/upload.html', {'form': form}, context_instance=RequestContext(request))


def project_list(request):
    projects = Project.objects.all()
    return render_to_response('uploader/list.html', {'projects': projects})


def download(request, file_name):
    file_path = settings.MEDIA_ROOT + file_name.strip('media')
    file_wrapper = FileWrapper(file(file_path,'rb'))
    response = HttpResponse(file_wrapper)
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    return response


def index(request):
    return HttpResponse("GISlab.web projects uploader works!")
