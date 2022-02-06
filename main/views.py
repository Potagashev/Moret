from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import SignUpUserForm, LoginUserForm
from main.models import Project, Task


# если не авторизован, редирект на авторизацию
@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    template_name = 'main/index.html'

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.user = User.objects.get(username=request.user)
        task.save()

    for task in tasks:
        if request.POST.get(str(task.id)) == 'on':
            task.delete()
    tasks = Task.objects.filter(user=request.user)

    return render(request, template_name, {'projects': projects, 'tasks': tasks})


def index_with_project(request, project_id):
    tasks = Task.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    project = get_object_or_404(Project, pk=project_id)
    template_name = 'main/index_with_project.html'

    if str(project_id) in request.GET:
        project.delete()
        template_name = 'main/index.html'
        return render(request, template_name, {'projects': projects, 'tasks': tasks})

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.user = User.objects.get(username=request.user)
        task.save()
        # return HttpResponseRedirect(reverse("index"))

    for task in tasks:
        if request.POST.get(str(task.id)) == 'on':
            task.delete()
    tasks = Task.objects.filter(user=request.user)

    return render(request, template_name, {'project': project, 'projects': projects, 'tasks': tasks})


def project_editing(request, project_id):
    tasks = Task.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    template_name = 'main/project_editing.html'
    project = get_object_or_404(Project, pk=project_id)
    # sub_tasks = Project.objects.get(child_projects)

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.user = User.objects.get(username=request.user)
        task.save()

    if 'edit_project' in request.POST:
        project.name = request.POST.get("name")
        project.description = request.POST.get("description")
        project.deadline = request.POST.get("deadline")
        project.save()
        return render(request, 'main/index_with_project.html',
                      {'project': project, 'projects': projects, 'tasks': tasks})

    if 'done_btn' in request.POST:
        print('dddd')
        subproject = Project()
        subproject.name = request.POST.get('subproject_name')
        subproject.description = request.POST.get('subproject_description')
        subproject.deadline = request.POST.get('subproject_deadline')
        subproject.user = User.objects.get(username=request.user)
        subproject.parent_project = project
        subproject.save()

    for task in tasks:
        if request.POST.get(str(task.id)) == 'on':
            task.delete()
    tasks = Task.objects.filter(user=request.user)

    return render(request, template_name, {'project': project, 'projects': projects, 'tasks': tasks})


def project_creating(request):
    tasks = Task.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    template_name = 'main/project_editing.html'

    if 'add_task_btn' in request.POST:
        task = Task()
        task.text = request.POST.get("add_task_input")
        task.user = User.objects.get(username=request.user)
        task.save()

    if 'create_project' in request.POST:
        newProject = Project()
        newProject.user = User.objects.get(username=request.user)
        newProject.name = request.POST.get("name")
        newProject.description = request.POST.get("description")
        newProject.deadline = request.POST.get("deadline")
        newProject.save()

    for task in tasks:
        if request.POST.get(str(task.id)) == 'on':
            task.delete()
    tasks = Task.objects.filter(user=request.user)

    return render(request, template_name, {'projects': projects, 'tasks': tasks})


class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'main/account/sign_up.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/account/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')