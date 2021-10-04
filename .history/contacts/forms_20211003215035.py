from django import forms
from .models import Contact


class ContactCreateForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("vvbb0", "vsvcbd@b.hgf")
