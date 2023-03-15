from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    latest_project_list = Project.objects.order_by('-published_on')[:5]
    context = {
        'latest_project_list': latest_project_list
    }
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})

def members(request, project_id):
    return HttpResponse(f"You're looking at the members of project #{project_id} ")

def partake(request, project_id):
    return HttpResponse(f"You're planning to partake in project #{project_id}")