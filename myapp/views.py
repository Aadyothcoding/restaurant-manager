from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import *
from . forms import BookingForm
# Create your views here.

def home(request):
    return HttpResponse("Hello, world!")

def about(request):
    return ()

def book(request):
    return ()

def menu(request):
    # Step 10: Add view logic
    menu_data = Menu.objects.all()  # Fetch all menu items from the database
    main_data = {"menu": menu_data}  # Create a context dictionary
    return render(request, 'myapp/menu.html', main_data)  

from django.shortcuts import render, get_object_or_404
from .models import Menu  # Ensure Menu is imported

def display_menu_items(request, pk=None):
    if pk:
        menu_item = get_object_or_404(Menu, pk=pk)
    else:
        menu_item = ""  # Assign empty string if pk is not provided

    return render(request, 'myapp/menu_item.html', {'menu_item': menu_item})


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to the success page
    else:
        form = BookingForm()
    return render(request, 'myapp/book.html', {'form': form})

def success(request):
    return render(request, 'myapp/success.html')  # Render a success page after booking