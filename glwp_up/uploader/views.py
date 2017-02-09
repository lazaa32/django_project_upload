from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ProjectForm
from .models import Project


def upload_file(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            f.extract()

            return render_to_response('uploader/list.html', {'projects': projects})
    else:
        form = ProjectForm(request.user)

    return render_to_response('uploader/upload.html', {'form': form}, context_instance=RequestContext(request))


def index(request):
    return HttpResponse("GISlab.web uploader works!")
