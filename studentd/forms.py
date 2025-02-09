from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'father_name', 'dob', 'phone', 'student_id', 'address']
    
    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        # Check if student_id already exists in the database
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError("Student ID already exists. Please choose a different one.")
        return student_id

# forms.py
from django import forms
from .models import Student

class EditStudentForm(forms.ModelForm):
    current_student_id = forms.CharField(max_length=20, required=True, label="Current Student ID")

    class Meta:
        model = Student
        fields = ['full_name', 'father_name', 'dob', 'phone', 'student_id', 'address']
