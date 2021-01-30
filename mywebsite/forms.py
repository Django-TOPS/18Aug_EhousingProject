from django import forms
from .models import signup
# for Complain  matecomplainForm

from .models import complain
# for contact form 

from .models import contact




class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

#for Complain 

class complainForm(forms.ModelForm):
    class Meta:
        model=complain
        fields='__all__'

# for contact form

class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'