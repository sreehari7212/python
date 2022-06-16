
from django import forms

from aa_app.models import Student


class StudentForm(forms.ModelForm):
   class Meta:
       model=Student
       fields=('name','address')