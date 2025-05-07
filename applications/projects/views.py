from django.shortcuts import render, redirect
from django.http import HttpResponse
from applications.projects.models import Project, Tag, Review
from applications.projects.forms import ProjectForm

# Create your views here.


#---------Only a text as output with HttpResponse ------
# def projects(request):
#     return HttpResponse('Here are our products')

#-------- render a template with text -------
# def projects(request):
#    return render(request, "projects/projects.html")

#------ A variable with template ---------


# def projects(request):
#     msg = "Hello, you are on projects page"
#     num = 10
#     context = {"message": msg, "page": num, "projects": projectsList}
#     # return render(request, "projects/projects.html", {"message": msg})
#     return render(request, "projects/projects.html", context)

# -------- single project --------


# def project(request, pk):
#     projectObj = None
#     for i in projectsList:
#         if i["id"] == pk:
#             projectObj = i
#     return render(request, "projects/single-project.html", {"projectid": projectObj})

def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects} # key is used in templates
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, "projects/single-project.html", {"project_obj": projectObj, "tags": tags})

def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)

# projects/project_form.html same template is used for creating and updating project

def updateProject(request, pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        #print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, "projects/delete_object_template.html", context)