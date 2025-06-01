document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signup-form');
    const formFeedbackDiv = document.getElementById('form-feedback');

    if (signupForm) {
        signupForm.addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default HTML form submission

            formFeedbackDiv.innerHTML = ''; // Clear previous feedback
            formFeedbackDiv.className = 'form-feedback'; // Reset class

            // Get CSRF token from the form
            const csrfToken = signupForm.querySelector('[name=csrfmiddlewaretoken]').value;

            // Collect form data
            const formData = new FormData(signupForm);
            const data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });

            // Remove csrfmiddlewaretoken from data to be sent as JSON payload
            // as it's sent in headers
            delete data.csrfmiddlewaretoken; 

            try {
                const response = await fetch(signupForm.action, { // Using form's action attribute
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken, // Crucial for Django's CSRF protection with AJAX
                    },
                    body: JSON.stringify(data),
                });

                const result = await response.json();

                if (response.ok && response.status === 201) { // Successfully created
                    formFeedbackDiv.textContent = result.message || 'Sign-up request successful!';
                    formFeedbackDiv.classList.add('success');
                    signupForm.reset(); // Clear the form
                     // Optionally hide the 'other_affiliation_details' field again if it was visible
                    const affiliationSelect = document.getElementById('id_affiliation');
                    if (affiliationSelect) {
                        const otherAffiliationField = document.getElementById('other_affiliation_details_field');
                        if (otherAffiliationField && affiliationSelect.value !== 'other') {
                             otherAffiliationField.style.display = 'none';
                        }
                    }
                } else {
                    // Handle errors (validation errors or other server errors)
                    let errorMessage = result.message || 'An error occurred.';
                    if (result.errors) {
                        errorMessage = 'Please correct the following errors:<ul>';
                        for (const field in result.errors) {
                            result.errors[field].forEach(error => {
                                errorMessage += `<li>${field.replace(/_/g, ' ')}: ${error}</li>`;
                            });
                        }
                        errorMessage += '</ul>';
                    }
                    formFeedbackDiv.innerHTML = errorMessage;
                    formFeedbackDiv.classList.add('error');
                }
            } catch (error) {
                console.error('Error submitting form:', error);
                formFeedbackDiv.textContent = 'A network error occurred. Please try again.';
                formFeedbackDiv.classList.add('error');
            }
        });
    }

    // JS for toggling 'other_affiliation_details' field visibility
    // (This is also in signup.html's script block, can be consolidated here if preferred)
    const affiliationSelect = document.getElementById('id_affiliation');
    const otherAffiliationField = document.getElementById('other_affiliation_details_field');
    // const otherAffiliationInput = document.getElementById('id_other_affiliation_details'); // Already defined if used from HTML

    function toggleOtherAffiliationField() {
        if (affiliationSelect && otherAffiliationField) { // Check if elements exist
            if (affiliationSelect.value === 'other') {
                otherAffiliationField.style.display = 'block';
            } else {
                otherAffiliationField.style.display = 'none';
                // if (otherAffiliationInput) otherAffiliationInput.value = ''; // Optionally clear
            }
        }
    }

    if (affiliationSelect) {
        toggleOtherAffiliationField(); // Initial check on page load
        affiliationSelect.addEventListener('change', toggleOtherAffiliationField);
    }

});
