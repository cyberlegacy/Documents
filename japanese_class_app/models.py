from django.db import models
from django.utils import timezone

class SignupRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # Email should ideally be unique
    
    AFFILIATION_CHOICES = [
        ('student', 'Kyoto University Student'),
        ('staff_researcher', 'Kyoto University Staff/Researcher'),
        ('other', 'Other'),
    ]
    affiliation = models.CharField(
        max_length=20,
        choices=AFFILIATION_CHOICES,
        default='student'
    )
    other_affiliation_details = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="If 'Other' affiliation, please specify."
    )

    LEVEL_CHOICES = [
        ('beginner', 'Beginner (N5 Equivalent)'),
        ('elementary', 'Elementary (N4 Equivalent)'),
        ('intermediate', 'Intermediate (N3 Equivalent)'),
        ('upper_intermediate', 'Upper-Intermediate (N2 Equivalent)'),
        ('advanced', 'Advanced (N1 Equivalent)'),
        ('unknown', 'Unsure / Need Assessment'),
    ]
    self_assessed_level = models.CharField(
        max_length=50,
        choices=LEVEL_CHOICES,
        default='unknown',
        verbose_name="Self-Assessed Japanese Level"
    )
    preferred_class_level = models.CharField(
        max_length=50,
        choices=LEVEL_CHOICES,
        default='unknown',
        verbose_name="Preferred Class Level"
    )
    
    previous_experience = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Previous Japanese Learning Experience"
    )
    learning_goals = models.TextField(
        blank=True, 
        null=True,
        verbose_name="What are your learning goals?"
    )
    questions_comments = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Any questions or comments?"
    )
    
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Sign-up Request"
        verbose_name_plural = "Sign-up Requests"
