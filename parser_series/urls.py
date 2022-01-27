from django.urls import path
from . import views

app_name = "parse"
urlpatterns = [
    path('series/', views.SeriesView.as_view(), name='series_view'),
    path('parser/', views.ParserSeriesView.as_view(), name="parser"),
    path('series/<int:id>/', views.SeriesDetailView.as_view()),
]
