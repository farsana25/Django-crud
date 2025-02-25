from django.shortcuts import render, redirect
from .models import crud

def phn(request):
    return render(request, 'crud.html')
def addnumber(request):
    phndic = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name', '')
            phnnumber = request.POST.get('number', '')

            # Validate inputs
            if not name:
                phndic['msg'] = 'Name cannot be empty'
                return render(request, 'crud.html', phndic)

            if not phnnumber:
                phndic['msg'] = 'Phone number cannot be empty'
                return render(request, 'crud.html', phndic)

            # Ensure phone number is valid
            try:
                phnnumber = int(phnnumber)
            except ValueError:
                phndic['msg'] = 'Invalid phone number format'
                return render(request, 'crud.html', phndic)

            # Check if name already exists
            if crud.objects.filter(name=name).exists():  # use lowercase 'name'
                phndic['msg'] = 'Name already exists'
                return render(request, 'crud.html', phndic)

            # Save new record
            emplist = crud(name=name, phonenumber=phnnumber)  # use lowercase 'name' and 'phonenumber'
            emplist.save()
            phndic['msg'] = 'Name and number added successfully'
            return render(request, 'crud.html', phndic)

    except Exception as e:
        phndic['msg'] = f'Error adding name: {str(e)}'
        return render(request, 'crud.html', phndic)
def display(request):
    empdtls = crud.objects.all()  # This fetches all records from the 'crud' table
    print(empdtls)  # For debugging purposes, let's check what's in the queryset
    return render(request, 'crud.html', {'emp': empdtls})  # Pass the queryset to the template


def update(request):
    try:
        if request.method == 'POST':
            oldname = request.POST.get('oldname', '')
            newname = request.POST.get('newname', '')

            # Validate inputs
            if not oldname or not newname:
                return render(request, 'crud.html', {'msg': 'Both names are required'})

            if oldname == newname:
                return render(request, 'crud.html', {'msg': 'Old and new names are the same'})

            # Check if old name exists
            if not crud.objects.filter(name=oldname).exists():  # use lowercase 'name'
                return render(request, 'crud.html', {'msg': 'Old name does not exist'})

            # Update name in database
            crud.objects.filter(name=oldname).update(name=newname)  # use lowercase 'name'
            return render(request, 'crud.html', {'msg': 'Name updated successfully'})

    except Exception as e:
        return render(request, 'crud.html', {'msg': f'Update failed: {str(e)}'})
def delete(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('dlt', '')
            
            # Check if name exists
            if not crud.objects.filter(name=name).exists():  # use lowercase 'name'
                return render(request, 'crud.html', {'msg': 'Name does not exist'})

            # Delete the record
            crud.objects.filter(name=name).delete()  # use lowercase 'name'
            return redirect('display')  # Redirect to display to see updated records

    except Exception as e:
        return render(request, 'crud.html', {'msg': f'Deletion failed: {str(e)}'})
