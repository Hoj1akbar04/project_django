from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogOutView, ForgetPasswordView, ResetPasswordView, TermsOfServiceView


urlpatterns = [
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/logout/", UserLogOutView.as_view(), name="logout"),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/<str:uidb64>/', ResetPasswordView.as_view(), name='reset_password'),
    path('terms_of_service/', TermsOfServiceView.as_view(), name='terms_of_service'),
]
