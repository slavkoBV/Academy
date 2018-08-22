import requests
from .models import SearchItem
from django.db.models import Q

STRIP_SYMBOLS = ('+', ',', ';')


def store(request, q):
    """Store queries in database"""
    if not request.session.get('q'):  # save distinct search query in session to
        request.session['q'] = []  # reduce number of database storing operations
    if len(q) > 2:
        if q not in request.session['q']:
            request.session['q'].append(q)
            term = SearchItem()
            term.q = q
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                client_ip = x_forwarded_for.split(',')[0]
            else:
                client_ip = request.META.get('REMOTE_ADDR')
            term.ip_address = client_ip
            clients = SearchItem.objects.values('ip_address').filter(ip_address__contains=client_ip)
            if len(clients) == 0:
                try:
                    # Get geo data about IP from 2IP.ua API
                    url = 'http://api.2ip.ua/geo.json?ip=' + client_ip
                    geo_response = requests.get(url).json()
                    term.IP_location = geo_response['country'] + ', ' + geo_response['city']
                except requests.RequestException:
                    pass
            else:
                location = SearchItem.objects.values('IP_location').filter(ip_address=client_ip)
                term.IP_location = location[0]['IP_location']
            term.save()


def search_objects(search_text, object_list, search_params, sort_param):
    """Return results of searching"""

    words = prepare_words(search_text)
    results = object_list.model.objects.none()  # create empty queryset to chain results of search
    for word in words:
        results = results | object_list.filter(Q(**{'{}__icontains'.format(search_params[0]): word}) |
                                               Q(**{'{}__icontains'.format(search_params[1]): word}))
    if sort_param:
        return results.distinct().order_by(sort_param)
    return results.distinct()


def prepare_words(search_text):
    """Prepare word for searching engine, remove strip_symbols"""
    for common in STRIP_SYMBOLS:
        if common in search_text:
            search_text = search_text.replace(common, ' ')
    words = search_text.split()
    return words[0:5]
