# japanese_class_app/forms.py
from django import forms
from .models import SignupRequest # Just import the model

class SignupForm(forms.ModelForm):
    # No need to explicitly reference AFFILIATION_CHOICES or LEVEL_CHOICES here
    # for the standard ModelForm fields, as Django handles it.
    
    class Meta:
        model = SignupRequest
        fields = [
            'full_name', 'email', 'affiliation', 'other_affiliation_details',
            'self_assessed_level', 'preferred_class_level',
            'previous_experience', 'learning_goals', 'questions_comments'
        ]
        widgets = {
            'previous_experience': forms.Textarea(attrs={'rows': 3}),
            'learning_goals': forms.Textarea(attrs={'rows': 3}),
            'questions_comments': forms.Textarea(attrs={'rows': 3}),
            'affiliation': forms.Select(attrs={'id': 'id_affiliation'}),
            'other_affiliation_details': forms.TextInput(attrs={'placeholder': 'Please specify if "Other"'})
        }
        labels = {
            'full_name': "Full Name",
            'email': "Email Address",
            'other_affiliation_details': "Details for 'Other' Affiliation",
        }

    def clean_other_affiliation_details(self):
        affiliation = self.cleaned_data.get('affiliation')
        other_details = self.cleaned_data.get('other_affiliation_details')

        if affiliation == 'other' and not other_details:
            raise forms.ValidationError("Please provide details for your 'Other' affiliation.")
        
        # It's good practice to return the cleaned data even if no changes are made
        # if affiliation != 'other' and other_details:
        #    pass # This is fine, but being explicit can be clearer
        
        return other_details