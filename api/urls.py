from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, PatientViewSet, DoctorViewSet, MappingViewSet
#from .views import frontend_view

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename="patient")  # Add basename
router.register(r'doctors', DoctorViewSet, basename="doctor")  # Add basename
router.register(r'mappings', MappingViewSet, basename="mapping")  # Add basename

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),  # Include ViewSets routes
#    path('index/', frontend_view, name='index'),
]
