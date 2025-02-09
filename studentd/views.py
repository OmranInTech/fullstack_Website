from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Student
from .forms import StudentForm



#function of registration //registration form backend

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        
        if form.is_valid():
            # Save the student to the database
            form.save()
            return redirect('all_students')  # Redirect to 'All Students' page after successful registration
        else:
            # If form is not valid, return to the registration page with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = StudentForm()  # If GET request, create a blank form
    
    return render(request, 'register.html', {'form': form})



#function of all students //all students backend

def all_students(request):
    students = Student.objects.all()  # Get all student records
    return render(request, 'allstudents.html', {'students': students})


#function for search students//search by id and name backend

def search_student1(request):
    students = None
    if request.method == "POST":
        name = request.POST.get("search_name")
        student_id = request.POST.get("search_id")
        
        # Filter students based on name and ID
        students = Student.objects.filter(
            full_name__icontains=name,  # Case-insensitive partial match for name
            student_id=student_id       # Exact match for ID
        )

    return render(request, 'search.html', {'students': students})



#function for the edit students //update details backend

def edit_student(request):
    if request.method == 'POST':
        current_name = request.POST.get('current_name')
        current_id = request.POST.get('current_id')

        # Fetch the student using the provided ID
        try:
            student = Student.objects.get(student_id=current_id, full_name=current_name)
            
            # Update fields if new data is provided
            new_name = request.POST.get('new_name')
            new_father_name = request.POST.get('new_father_name')
            new_dob = request.POST.get('new_dob')
            new_phone = request.POST.get('new_phone')
            new_address = request.POST.get('new_address')

            if new_name:
                student.full_name = new_name
            if new_father_name:
                student.father_name = new_father_name
            if new_dob:
                student.dob = new_dob
            if new_phone:
                student.phone = new_phone
            if new_address:
                student.address = new_address

            student.save()
            return redirect('all_students')  # Redirect to the All Students page after success

        except Student.DoesNotExist:
            error_message = "Student with the provided name and ID does not exist."
            return render(request, 'edit.html', {'error_message': error_message})

    return render(request, 'edit.html')


#function for search by id //quick access in home page

def search_student(request):
    query = request.GET.get('search_query')  # Get the query from the GET request
    student = None

    if query:  # Check if a query exists
        try:
            student = Student.objects.get(student_id=query)  # Search for a student by ID
        except Student.DoesNotExist:
            student = None  # If no student is found, set to None

    context = {
        'query': query,  # To display the search query
        'student': student  # Pass the student object (if found)
    }
    return render(request, 'home.html', context)
