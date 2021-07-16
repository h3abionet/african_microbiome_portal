from django.urls import path
from django.views.generic import TemplateView

from . import views, live_search

urlpatterns = [
    #  path('', views.front_main, name="index"),
    # Code controlled pages
    path("search/", views.search_form, name="search"),
    # path("search2/", live_search.search, name="live_search"),
    path("results/", views.results, name="results"),
    path("results_sample/", views.results_sample, name="results_sample"),
    #  path('summary/', views.summary, name="summary"),
    # path("upload/", views.upload_file, name="upload"),
    #  path('download/', views.results_download, name="download"),
    # Mostly statics pages
    path("about/", TemplateView.as_view(template_name="about.html")),
    path("test/", TemplateView.as_view(template_name="test.html")),
    path(
        "contributor/", TemplateView.as_view(template_name="contributors.html")
    ),
    path("resource/", TemplateView.as_view(template_name="resouces.html")),
    path("help/", TemplateView.as_view(template_name="help.html")),
    path(
        "publication/", TemplateView.as_view(template_name="publications.html")
    ),
    # path('contributors/', views.contributors, name="contributors"),
]
