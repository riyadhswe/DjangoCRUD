from django.urls import path
from App import views

urlpatterns = [
    path('', views.index_views, name="index"),
    path('student/', views.student_views, name="student"),
    path('student_info/<int:studentid>', views.studentinfo_views, name="student_info"),
]
