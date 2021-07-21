from django.urls import path
from . import views

urlpatterns=[
    path("",views.blog_index, name="blog_index"),
    path("<int:pk>/" , views.blog_detail, name="blog_detail"),
    path("<category>/" , views.blog_category, name="blog_category"),
]

'''
from django.urls import path
from . import views

urlpatterns=[
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail")
]
'''