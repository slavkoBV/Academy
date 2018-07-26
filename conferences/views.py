from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Conference

from utils.paginate import paginate


def conference_list(request):
    conferences = Conference.objects.all()
    context = paginate(conferences, 2, request, {'conferences': conferences}, var_name='conferences')
    return render(request, 'conference_app/conference_list.html', context)


def conference_detail(request, id, slug):
    conference = get_object_or_404(Conference, pk=id)
    thesises = conference.thesis_set.all()

    if request.GET.get('section'):
        thesises = thesises.filter(section=request.GET.get('section'))
    return render(request, 'conference_app/conference_detail.html', {'conference': conference,
                                                                     'thesises': thesises})
