from django.shortcuts import render, get_object_or_404

from .models import Team, RoboSprintInfo, RoboSprintProject


def main(request):
    project_info = get_object_or_404(RoboSprintInfo, pk=1)
    info = project_info.title
    teams = Team.objects.all()
    context = {
        'info': info,
        'teams': teams
    }
    return render(request, 'robosprint/main.html', context)


def project_about(request):
    about = get_object_or_404(RoboSprintInfo, pk=1).about
    context = {'object': about}
    return render(request, 'robosprint/project.html', context)


def project_platform(request):
    platform = get_object_or_404(RoboSprintProject, pk=1).platform
    context = {'object': platform}
    return render(request, 'robosprint/project.html', context)


def project_model(request):
    platform = get_object_or_404(RoboSprintProject, pk=1).model_requirements
    context = {'object': platform}
    return render(request, 'robosprint/project.html', context)


def project_route(request):
    platform = get_object_or_404(RoboSprintProject, pk=1).route_requirements
    context = {'object': platform}
    return render(request, 'robosprint/project.html', context)


def team_register(request):
    pass
