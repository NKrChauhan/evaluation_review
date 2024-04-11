from django.urls import path
from .views.guidelines import GuidelineListView, GuidelineDetailView


urlpatterns = [
    path('', GuidelineListView.as_view(), name='guidelines-list'),
    path('<int:pk>/', GuidelineDetailView.as_view(), name='guideline-detail'),
]
