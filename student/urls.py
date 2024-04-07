from django.urls import path
from .views import StudentListView, UserDetailView, UserRegisterView, UserLoginView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path('student/<int:id>/', UserDetailView.as_view(), name='student-detail'),
    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login')
]
