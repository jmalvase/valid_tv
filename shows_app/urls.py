from django.urls import path
from . import views
urlpatterns=[
    path('', views.shows),
    path('new', views.new_show_page),
    path('create_show', views.create_show),
    path('<int:show_id>', views.read_show),
    path('<int:show_id>/edit', views.edit_show),
    path('<int:show_id>/update', views.update_show),
    path('<int:show_id>/destroy', views.destroy)
]