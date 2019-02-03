from django.views.generic import ListView, DetailView
from .models import News
from utils.paginate import paginate


class NewsListView(ListView):
    model = News

    def get_context_data(self, **kwargs):
        news = self.get_queryset()
        tags = []
        for n in news:
            if n.tags:
                tags.extend([tag.strip() for tag in n.tags.split(',')])
        context = paginate(news, 10, self.request, {'news': news}, var_name='news')
        context['tags'] = list(set(tags))
        return context

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        if tag:
            return News.objects.filter(tags__contains=tag)
        return News.objects.all()


class NewsDetailView(DetailView):
    model = News
    template_name = 'academy_news/news_detail.html'
