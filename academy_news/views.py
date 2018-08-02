from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
from utils.paginate import paginate


class NewsListView(ListView):
    model = News

    def get_context_data(self, **kwargs):
        news = super().get_queryset()
        context = paginate(news, 2, self.request, {'news': news}, var_name='news')
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'academy_news/news_detail.html'
