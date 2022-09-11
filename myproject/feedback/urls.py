from django.urls import path
from . import views
urlpatterns = [
    path('', views.feedbackView,name="feedback-view"),
]