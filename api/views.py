from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import RegisterSerializer

from rest_framework import viewsets, permissions
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, MappingSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get_queryset(self):
        """Only return patients of the authenticated user"""
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Ensure patient is linked to the logged-in user"""
        serializer.save(user=self.request.user)

# Doctor Management APIs
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()  # Add this line
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Assign the authenticated user to the doctor record"""
        serializer.save(user=self.request.user)

# Patient-Doctor Mapping APIs
class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()  # Add this line
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]