from django.contrib import admin
from .models import SignupRequest

@admin.register(SignupRequest)
class SignupRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'affiliation', 'preferred_class_level', 'timestamp')
    list_filter = ('affiliation', 'preferred_class_level', 'timestamp')
    search_fields = ('full_name', 'email')
    readonly_fields = ('timestamp',) # Makes timestamp non-editable in admin

    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'timestamp')
        }),
        ('Affiliation & Level', {
            'fields': ('affiliation', 'other_affiliation_details', 'self_assessed_level', 'preferred_class_level')
        }),
        ('Additional Information', {
            'fields': ('previous_experience', 'learning_goals', 'questions_comments'),
            'classes': ('collapse',) # Collapsible section
        }),
    )
