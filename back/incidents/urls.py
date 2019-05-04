from incidents import views
from django.urls import path

urlpatterns = [
    path('subscribe', views.SubscriberView.as_view()),
]
