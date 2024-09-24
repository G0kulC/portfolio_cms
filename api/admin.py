from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Portfolio, Project, Skill, Experience, Education, 
    Contact, SocialLink, Testimonial, Template, CustomUser
)

# CustomUserAdmin to manage the CustomUser model in the admin panel
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_deleted', 'deleted_at']

   
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('user__username', 'title')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'name', 'tech_stack', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name', 'tech_stack', 'portfolio__title')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'name', 'proficiency', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name', 'portfolio__title')
    list_filter = ('is_deleted', 'proficiency')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'job_title', 'company_name', 'start_date', 'end_date', 'is_current', 'is_deleted')
    search_fields = ('job_title', 'company_name', 'portfolio__title')
    list_filter = ('is_deleted', 'is_current')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'degree', 'institution', 'start_date', 'end_date', 'is_current', 'is_deleted')
    search_fields = ('degree', 'institution', 'portfolio__title')
    list_filter = ('is_deleted', 'is_current')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone', 'created_at', 'updated_at', 'is_deleted')  # Removed 'portfolio'
    search_fields = ('email', 'phone', 'user__username')  # Removed 'portfolio__title'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'url', 'created_at', 'updated_at')  # Use 'name' and 'url'
    search_fields = ('name', 'url', 'user__username')  # Ensure you're using the correct field names
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'author_name', 'author_company', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('author_name', 'author_company', 'user__username')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'updated_at')
