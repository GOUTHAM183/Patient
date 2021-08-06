from django.urls import path
from . import views
from .views import (
    PatientListView,
    PatientDeleteView,
    PatientDetailView,
    PatientUpdateView,
    PatientCreateView,
)

urlpatterns = [
    path("", PatientListView.as_view(), name="home"),
    path("patient/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
    path("patient/<int:pk>/update/", PatientUpdateView.as_view(), name="patient-update"),
    path("patient/<int:pk>/delete/", PatientDeleteView.as_view(), name="patient-delete"),
    path("patient/new/", PatientCreateView.as_view(), name="patient-create"),
    path("search/", views.search, name="search"),
]