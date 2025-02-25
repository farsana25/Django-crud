from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib import messages
from .models import mode  # Use 'mode' model


def phn(request):
    students = mode.objects.all()  
    return render(request, 'mode.html', {'students': students})

# Add a student
def add_student(request):
    if request.method == "POST":
        # Manually extract data from request.POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        # Simple validation to check if any field is empty
        if not name or not email or not age or not gender:
            msg = "All fields are required!"
        else:
            try:
                # Save the new student to the database
                student = mode(name=name, email=email, age=age, gender=gender)  # Using 'mode' model
                student.save()
                msg = "Student added successfully!"
            except Exception as e:
                msg = f"Error adding student: {e}"

        # Get all students from the database to display
        students = mode.objects.all()  # Use 'mode' model
        return render(request, 'mode.html', {'students': students, 'msg': msg})


    students = mode.objects.all()  # Use 'mode' model
    return render(request, 'mode.html', {'students': students})

def updateData(request, id):
    if request.method == "POST":
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        try:
            # Get the student by id and update the data
            student = mode.objects.get(id=id)
            student.name = name
            student.email = email
            student.age = age
            student.gender = gender
            student.save()

            messages.success(request, "Data Updated Successfully!")
            return redirect("phn")  # Redirect to another page or back to the list

        except mode.DoesNotExist:
            messages.error(request, "Student not found.")
            return redirect("phn")  # Redirect to a list or other page if student not found

    # GET method: Render the update form pre-filled with student's data
    try:
        student = mode.objects.get(id=id)
        context = {"student": student}
        return render(request, "mode2.html", context)
    except mode.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect("phn")



 # Make sure you import the correct model

def delete_student(request, student_id):
    # Get the student object or raise 404 if not found
    student = get_object_or_404(mode, id=student_id)
    
    # Delete the student
    student.delete()

    # Redirect to the same page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

