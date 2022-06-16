
from django.urls import path

from aa_app import views

urlpatterns = [
    path('', views.home,name='home'),
    path('student_register',views.student_add,name='student_register'),
    path('student_views',views.student_view,name='student_views'),
]