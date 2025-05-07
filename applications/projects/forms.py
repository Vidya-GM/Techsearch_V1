from django.forms import ModelForm
from applications.projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "demo_link", "source_link", "tags"]
