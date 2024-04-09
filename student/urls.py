from django.urls import path
from .views import StudentListView, UserDetailView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path('student/<int:id>/', UserDetailView.as_view(), name='student-detail'),

]
