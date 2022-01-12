from datetime import datetime

from django.shortcuts import render, get_object_or_404

from main.models import Project, Task


def index(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    template_name = 'main/index.html'

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.save()

    return render(request, template_name, {'projects': projects, 'tasks': tasks})


def index_with_project(request, project_id):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    project = get_object_or_404(Project, pk=project_id)
    template_name = 'main/index_with_project.html'

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.save()
        # return HttpResponseRedirect(reverse("index"))

    # короче идея в чем
    # надо при отметке чекбокса вызывать скрипт, который будет прятать его
    # и менять ему атрибут checked на true
    # и при следующем сабмите переберем все задачи и при значении
    # true этого атрибута эта задача будет удалена
    for task in tasks:
        if request.POST.get(task.text) == 'on':
            task.delete()
            print('task deleted')
    tasks = Task.objects.all()

    return render(request, template_name, {'project': project, 'projects': projects, 'tasks': tasks})


def project_editing(request, project_id):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    template_name = 'main/project_editing.html'
    project = get_object_or_404(Project, pk=project_id)
    # sub_tasks = Project.objects.get(child_projects)

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.save()

    if 'edit_project' in request.POST:
        project.name = request.POST.get("name")
        project.description = request.POST.get("description")
        if request.POST.get("deadline") == '':
            project.deadline = None
        else:
            project.deadline = request.POST.get("deadline")
        project.save()
        return render(request, 'main/index_with_project.html',
                      {'project': project, 'projects': projects, 'tasks': tasks})

    if 'done_btn' in request.POST:
        new_project = Project()
        new_project.name = request.POST.get('subproject_name')
        new_project.description = request.POST.get('subproject_description')
        new_project.deadline = request.POST.get('subproject_deadline')
        new_project.parent_project = project
        new_project.save()

    return render(request, template_name, {'project': project, 'projects': projects, 'tasks': tasks})


def project_creating(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    template_name = 'main/project_editing.html'

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.save()

    if 'create_project' in request.POST:
        if request.POST.get("name") != '':
            newProject = Project()
            newProject.name = request.POST.get("name")
            newProject.description = request.POST.get("description")
            if request.POST.get("deadline") == '':
                newProject.deadline = None
            else:
                newProject.deadline = request.POST.get("deadline")
            newProject.save()

    return render(request, template_name, {'projects': projects, 'tasks': tasks})
