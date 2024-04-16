from django.urls import path
from .views import CourseView, TeacherView, AboutView, ContactView

urlpatterns = [
    path('course/', CourseView.as_view(), name='courses'),
    path('teacher/', TeacherView.as_view(), name='teachers'),
    path('about/', AboutView.as_view(), name='about'),
    path('connect/', ContactView.as_view(), name='contact')
]