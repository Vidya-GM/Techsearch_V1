from django.shortcuts import render
from django.http import HttpResponse
from applications.projects.models import Project, Tag, Review

# Create your views here.


#---------Only a text as output with HttpResponse ------
# def projects(request):
#     return HttpResponse('Here are our products')

#-------- render a template with text -------
# def projects(request):
#    return render(request, "projects/projects.html")

#------ A variable with template ---------

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


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
