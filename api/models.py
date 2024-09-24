from datetime import datetime
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class DeletedQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)



class CustomUser(AbstractUser):
    """
    Custom user model that uses a UUID as the primary key and includes soft delete functionality.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Use UUID as the primary key
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp for when the user was created
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp for soft delete
    is_deleted = models.BooleanField(default=False)  # Soft delete status

    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of deleting the user, mark them as deleted.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted user by clearing the deleted_at timestamp and setting is_deleted to False.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.username

class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # Name of the template
    description = models.TextField(null=True, blank=True)  # Short description of the template
    preview_image = models.ImageField(upload_to='templates/', null=True, blank=True)  # Preview image of the React template
    demo_url = models.URLField(null=True, blank=True)  # Link to a live demo of the React template (Netlify, Vercel, etc.)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp for soft delete
    is_deleted = models.BooleanField(default=False)  # Soft delete status

    objects = DeletedQuerySet().as_manager()

    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of removing the template, set is_deleted to True and mark deleted_at timestamp.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted template by setting is_deleted to False and clearing the deleted_at timestamp.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="portfolios")  # Link to the User model
    template = models.ForeignKey('Template', on_delete=models.SET_NULL, null=True, blank=True)  # Selected template
    title = models.CharField(max_length=255)  # Portfolio title (e.g., "John Doe's Developer Portfolio")
    bio = models.TextField(null=True, blank=True)  # Short bio or professional summary
    profile_image = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)  # Profile image or avatar
    resume = models.FileField(upload_to='portfolio/resumes/', null=True, blank=True)  # Resume upload field (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Portfolio creation date
    updated_at = models.DateTimeField(auto_now=True)  # Portfolio last update date
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete timestamp
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    objects = DeletedQuerySet().as_manager()

    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of removing the portfolio, set is_deleted to True and mark deleted_at timestamp.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted portfolio by setting is_deleted to False and clearing the deleted_at timestamp.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Portfolio"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='projects')  # Link to Portfolio
    name = models.CharField(max_length=255)  # Name of the project
    description = models.TextField()  # Detailed description of the project
    tech_stack = models.CharField(max_length=255, null=True, blank=True)  # Technologies used (e.g., React, Django)
    role = models.CharField(max_length=255, null=True, blank=True)  # User's role in the project (e.g., Frontend, Backend)
    github_url = models.URLField(null=True, blank=True)  # GitHub repository URL for the project
    live_demo_url = models.URLField(null=True, blank=True)  # Live demo URL (if applicable)
    image = models.ImageField(upload_to='portfolio/projects/', null=True, blank=True)  # Optional image or screenshot of the project
    created_at = models.DateTimeField(auto_now_add=True)  # Project creation date
    updated_at = models.DateTimeField(auto_now=True)  # Last update date
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete timestamp
    is_deleted = models.BooleanField(default=False)  # Soft delete status

    objects = DeletedQuerySet().as_manager()

    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of removing the project, set is_deleted to True and mark deleted_at timestamp.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted project by setting is_deleted to False and clearing the deleted_at timestamp.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='skills')  # Link to Portfolio
    name = models.CharField(max_length=100)  # Name of the skill (e.g., Python, React, Docker)
    proficiency = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)  # Skill added date
    updated_at = models.DateTimeField(auto_now=True)  # Last update date
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete timestamp
    is_deleted = models.BooleanField(default=False)  # Soft delete status

    objects = DeletedQuerySet().as_manager()
    
    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of removing the skill, set is_deleted to True and mark deleted_at timestamp.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()
    
    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted skill by setting is_deleted to False and clearing the deleted_at timestamp.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return self.name



class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='experiences')  # Link to Portfolio
    job_title = models.CharField(max_length=255)  # Job title (e.g., Software Engineer)
    company_name = models.CharField(max_length=255)  # Company name
    location = models.CharField(max_length=255, null=True, blank=True)  # Job location (optional)
    start_date = models.DateField()  # Job start date
    end_date = models.DateField(null=True, blank=True)  # Job end date (null if current position)
    is_current = models.BooleanField(default=False)  # Whether this is the current job
    description = models.TextField(null=True, blank=True)  # Job responsibilities/achievements description
    created_at = models.DateTimeField(auto_now_add=True)  # Entry creation date
    updated_at = models.DateTimeField(auto_now=True)  # Last update date
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete timestamp
    is_deleted = models.BooleanField(default=False) 

    objects = DeletedQuerySet().as_manager()
    
    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of removing the experience, set is_deleted to True and mark deleted_at timestamp.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()
    
    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted experience by setting is_deleted to False and clearing the deleted_at timestamp.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return self.job_title



class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='educations')  # Link to Portfolio
    degree = models.CharField(max_length=255)  # Degree title (e.g., Bachelor of Science in Computer Science)
    institution = models.CharField(max_length=255)  # Educational institution name
    location = models.CharField(max_length=255, null=True, blank=True)  # Location of the institution (optional)
    start_date = models.DateField()  # Start date of education
    end_date = models.DateField(null=True, blank=True)  # End date of education (nullable if ongoing)
    is_current = models.BooleanField(default=False)  # Whether this education is ongoing
    description = models.TextField(null=True, blank=True)  # Additional details (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Entry creation date
    updated_at = models.DateTimeField(auto_now=True)  # Last update date
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete timestamp
    is_deleted = models.BooleanField(default=False)  # Soft delete status
    
    objects = DeletedQuerySet().as_manager()
    
    def delete(self, *args, **kwargs):
        """
        Soft delete: Instead of removing the education, set is_deleted to True and mark deleted_at timestamp.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()
    
    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted education by setting is_deleted to False and clearing the deleted_at timestamp.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return self.degree



class Testimonial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='testimonials')
    author_name = models.CharField(max_length=255)
    author_position = models.CharField(max_length=255, null=True, blank=True)
    author_company = models.CharField(max_length=255, null=True, blank=True)
    author_photo = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    testimonial_text = models.TextField()
    author_linkedin = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp when the testimonial is soft-deleted
    is_deleted = models.BooleanField(default=False)  # Soft-delete status

    objects = DeletedQuerySet.as_manager()

    def delete(self, *args, **kwargs):
        """
        Soft delete: instead of removing the record from the database,
        mark it as deleted by setting the 'is_deleted' field to True and
        recording the timestamp in 'deleted_at'.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted testimonial by setting 'is_deleted' to False
        and clearing 'deleted_at'.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return f"{self.author_name} - {self.user.username}"

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    additional_phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp when the contact is soft-deleted
    is_deleted = models.BooleanField(default=False)  # Soft-delete status

    objects = DeletedQuerySet.as_manager()
    
    def delete(self, *args, **kwargs):
        """
        Soft delete: instead of removing the record from the database,
        mark it as deleted by setting the 'is_deleted' field to True and
        recording the timestamp in 'deleted_at'.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()
    
    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted contact by setting 'is_deleted' to False
        and clearing 'deleted_at'.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"

class SocialLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    url = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='social_links')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp when the social link is soft-deleted
    is_deleted = models.BooleanField(default=False)  # Soft-delete status

    objects = DeletedQuerySet.as_manager()

    def delete(self, *args, **kwargs):
        """
        Soft delete: instead of removing the record from the database,
        mark it as deleted by setting the 'is_deleted' field to True and
        recording the timestamp in 'deleted_at'.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self, *args, **kwargs):
        """
        Restore a soft-deleted social link by setting 'is_deleted' to False
        and clearing 'deleted_at'.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"