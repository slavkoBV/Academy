from django.views.generic import ListView, DetailView
from .models import Project
from utils.paginate import paginate


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects_list.html'

    def get_context_data(self, **kwargs):
        projects = super().get_queryset()
        context = paginate(projects, 10, self.request, {'projects': projects}, var_name='projects')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
