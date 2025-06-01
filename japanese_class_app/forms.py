from django import forms
from .models import SignupRequest, AFFILIATION_CHOICES, LEVEL_CHOICES

class SignupForm(forms.ModelForm):
    # You can customize widgets or add specific form fields here if needed
    # For example, if you want to use a RadioSelect for affiliation:
    # affiliation = forms.ChoiceField(choices=AFFILIATION_CHOICES, widget=forms.RadioSelect)
    
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
            'affiliation': forms.Select(attrs={'id': 'id_affiliation'}), # Add id for JS if needed
            'other_affiliation_details': forms.TextInput(attrs={'placeholder': 'Please specify if "Other"'})
        }
        labels = {
            'full_name': "Full Name",
            'email': "Email Address",
            'other_affiliation_details': "Details for 'Other' Affiliation",
        }

    def clean_other_affiliation_details(self):
        """
        Custom validation: Ensure 'other_affiliation_details' is provided if 'affiliation' is 'other'.
        """
        affiliation = self.cleaned_data.get('affiliation')
        other_details = self.cleaned_data.get('other_affiliation_details')

        if affiliation == 'other' and not other_details:
            raise forms.ValidationError("Please provide details for your 'Other' affiliation.")
        
        if affiliation != 'other' and other_details:
            # Optionally clear it if not 'other'
            # return ""
            pass # Or let it be, depends on desired behavior

        return other_details
