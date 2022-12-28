from django import forms
from django.contrib.auth.forms import UserCreationForm

from Dmsapp.models import Notification, Login , internal_mark


class DateInput(forms.DateInput):
    input_type = 'date'


gender_choice = (
    ("Male", "Male"),
    ("Female", "Female"),
)

department_choice = (
    ('BSC Physics', 'BSC Physics'),
    ('BSC Maths', 'BSC Maths'),
    ('BSC ComputerScience', 'BSC ComputerScience'),
    ('BCA', 'BCA'),
    ('BSC Chemistry', 'BSC Chemistry'),
    ('BA English', 'BA English'),
    ('BA Malayalam', 'BA Malayalam'),
    ('BBA ', 'BBA'),
)

class StudentForm(UserCreationForm):
    gender = forms.ChoiceField(choices=gender_choice, required=True, widget=forms.RadioSelect)
    date_of_birth = forms.DateField(widget=DateInput)
    department = forms.ChoiceField(choices=department_choice)

    class Meta:
        model = Login
        fields = (
        'username', 'name', 'guardian_name', 'gender','Admission_No','blood_group', 'date_of_birth', 'department', 'mobile_no', 'address', 'photo',
        'password1', 'password2')


class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notification
        fields = '__all__'

class internal_form(forms.ModelForm):
    class Meta:
        model = internal_mark
        fields = '__all__'