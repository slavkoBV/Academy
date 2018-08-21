from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Conference
from .forms import ThesisFilterForm
from search.search import search_objects
from search.forms import SearchForm
from utils.paginate import paginate

thesis_message_dict = {('1',): 'доповідь',
                       ('2', '3', '4'): 'доповіді',
                       ('0', '5', '6', '7', '8', '9'): 'доповідей'}


def conference_list(request):
    conferences = Conference.objects.all()
    context = paginate(conferences, 5, request, {'conferences': conferences}, var_name='conferences')
    return render(request, 'conference_app/conference_list.html', context)


def conference_detail(request, id, slug):
    participant_message_dict = {('1',): 'учасник',
                                ('2', '3', '4'): 'учасники',
                                ('0', '5', '6', '7', '8', '9'): 'учасників'}
    conference = get_object_or_404(Conference, pk=id)
    thesis_message = ''
    participant_message = ''
    if len(conference.get_number_of_thesises()) == 2 and conference.get_number_of_thesises().startswith('1'):
        thesis_message = 'доповідей'
    else:
        for i in thesis_message_dict.keys():
            if conference.get_number_of_thesises()[-1] in i:
                thesis_message = thesis_message_dict[i]
    if len(conference.get_number_of_participants()) == 2 and conference.get_number_of_participants().startswith('1'):
        participant_message = 'учасників'
    else:
        for i in participant_message_dict.keys():
            if conference.get_number_of_participants()[-1] in i:
                participant_message = participant_message_dict[i]
    context = {'conference': conference, 'thesis_message': thesis_message, 'participant_message': participant_message}
    return render(request, 'conference_app/conference_detail.html', context)


def thesis_list(request, id, slug):
    conference = get_object_or_404(Conference, pk=id)
    theses = conference.thesis_set.all()
    form = ThesisFilterForm()
    search_form = SearchForm(search_text='Прізвище автора або назва статті')
    sort_param = None
    q = request.GET.get('q', '')
    thesis_message = ''
    if q:
        search_params = ('title', 'author__participant__user__lastname')
        theses = search_objects(q, theses, search_params, sort_param)

        number_of_search_result = len(theses)
        if number_of_search_result == 2 and str(number_of_search_result).startswith('1'):
            thesis_message = 'доповідей'
        else:
            for i in thesis_message_dict.keys():
                if str(number_of_search_result)[-1] in i:
                    thesis_message = thesis_message_dict[i]
    if request.GET.get('section'):
        form = ThesisFilterForm(request.GET)
        if form.is_valid():
            if request.GET.get('section') != 'all':
                theses = theses.filter(section=request.GET.get('section'))
    context = paginate(theses, 3, request, {'theses': theses}, var_name='theses')
    context['conference'] = conference
    context['form'] = form
    context['search_form'] = search_form
    context['q'] = q
    context['thesis_message'] = thesis_message
    return render(request, 'conference_app/thesis_list.html', context)
