from rest_framework import viewsets
from django.contrib.auth import get_user_model 
from .models import (
    Portfolio, Project, Skill, Experience, Education,
    Contact, SocialLink, Testimonial, Template
)
from .serializers import (
    CustomUserSerializer, PortfolioSerializer, ProjectSerializer, SkillSerializer, 
    ExperienceSerializer, EducationSerializer, ContactSerializer, SocialLinkSerializer, 
    TestimonialSerializer, TemplateSerializer
)

# User ViewSet
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        # Check if user is staff or superuser, and if not, filter out soft-deleted users
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            # View all users if user is staff without superuser
            return queryset.filter(is_staff=True,is_superuser=False)
        elif self.request.user.is_superuser:
            # View all users if user is superuser
            return queryset.all()
        else:
            return queryset.filter(is_deleted=False, is_staff=False, is_superuser=False)
            


# Portfolio ViewSet
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Skill ViewSet
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)

# Experience ViewSet
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)


# Education ViewSet
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)

# Contact ViewSet
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    # Add custom methods
    # IF is_deleted is True, Filter out deleted objects
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)
    

# SocialLink ViewSet
class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

# Testimonial ViewSet
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# Template ViewSet
class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
