from django.shortcuts import render, get_object_or_404
from.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()[:6]
    context = {
        'projects':projects
    }
    return render(request, 'index.html', context)

def project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project':project
    }
    return render(request, 'project.html', context)