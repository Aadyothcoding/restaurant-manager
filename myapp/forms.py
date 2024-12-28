from django import forms 
from .models import Booking 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date', 'time', 'number_of_guests', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'special_requests': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'date': 'Booking Date',
            'time': 'Booking Time',
            'number_of_guests': 'Number of Guests',
            'special_requests': 'Special Requests (Optional)',
        }