from django.shortcuts import render
from django.views.generic import DetailView
from .models import Conference

from utils.paginate import paginate


def conference_list(request):
    conferences = Conference.objects.all()
    context = paginate(conferences, 2, request, {'conferences': conferences}, var_name='conferences' )
    return render(request, 'conference_app/conference_list.html', context)


class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conference_app/conference_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
