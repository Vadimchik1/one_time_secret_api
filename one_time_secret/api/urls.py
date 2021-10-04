from django.urls import path
from api import views

urlpatterns = [
    path('generate/', views.SecretView.as_view()),
    path('secrets/<str:password>', views.SecretDetail.as_view()),
]