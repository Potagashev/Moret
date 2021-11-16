from django.shortcuts import render
from django.views import generic

from main.models import Project, Task


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.all()


# def index(request):
#     projects = Project.objects.all()
#     tasks = Task.objects.all()
#
#     return render(request, 'main/index.html', {projects: 'projects', tasks: 'tasks'})


def index_with_project(request):
    return render(request, 'main/index_with_project.html')
