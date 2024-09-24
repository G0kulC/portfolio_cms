from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PortfolioViewSet, ProjectViewSet, SkillViewSet, 
    ExperienceViewSet, EducationViewSet, ContactViewSet, SocialLinkViewSet, 
    TestimonialViewSet, TemplateViewSet
)

# Create a router and register the viewsets with it
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'social-links', SocialLinkViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'templates', TemplateViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
