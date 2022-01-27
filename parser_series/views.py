from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, DetailView
from . import models, forms, parser

class SeriesView(ListView):
    template_name = 'series_list.html'

    def get_queryset(self):
        return models.Series.objects.all()

class ParserSeriesView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm
    success_url = '/series/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserSeriesView, self).post(request, *args, **kwargs)

class SeriesDetailView(DetailView):
    template_name = 'series_detail.html'

    def get_object(self, **kwargs):
        series_id = self.kwargs.get('id')
        return get_object_or_404(models.Series, id=series_id)
