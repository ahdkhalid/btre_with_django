from django.urls import path

from . import views
#for listing app
urlpatterns=[
    path('', views.index, name="listings"),
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search")
]