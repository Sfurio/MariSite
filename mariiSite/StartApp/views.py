from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.dispatch import Signal
from datetime import datetime



def contact(request):
    return render(request, 'contact.html')

def home(request):
    images = ['WelcomePage.JPEG', 'WelcomePage2.JPEG', 'WelcomePage3.JPEG', 'WelcomePage4.JPEG', 'WelcomePage5.JPEG', 'WelcomePage6.JPEG' ]
    return render(request, 'homes.html', {'images': images})

def gallery(request):

    images = [

        {'src': 'WelcomePage.JPEG', 'caption': 'Image 1'},
        {'src': 'WelcomePage2.JPEG', 'caption': 'Image 2'},
        {'src': 'WelcomePage3.JPEG', 'caption': 'Image 3'},
        {'src': 'WelcomePage4.Jpeg', 'caption': 'Image 1'},
        {'src': 'WelcomePage5.Jpeg', 'caption': 'Image 2'},
        {'src': 'WelcomePage6.Jpeg', 'caption': 'Image 3'},
        {'src': 'hybrid.png', 'caption': 'Image 1'},
        {'src': 'IMG_7021.JPEG', 'caption': 'Image 2'},
        {'src': 'IMG_7022.JPEG', 'caption': 'Image 3'},
        {'src': 'IMG_7023.jpg', 'caption': 'Image 1'},
        {'src': 'IMG_7024.JPEG', 'caption': 'Image 2'},
        {'src': 'MegaVolume.png', 'caption': 'Image 1'},
        {'src': 'Volume.png', 'caption': 'Image 2'},
        {'src': 'montage.png', 'caption': 'Image 3'},
        {'src': 'Logo.png', 'caption': 'Image 1'},
        # Add more images here
    ]
    context = {'images': images}
    return render(request, 'gallery.html', context)

def services(request):
    return render(request, 'services.html')
def format_hour_military_to_normal(hour):
    military_time = datetime.strptime(hour, "%H")
    return military_time.strftime("%I %p")

def schedule(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        services = request.POST.get('services')
        date = request.POST.get('date')
        hour = (request.POST.get('hour'))

        # Check if the selected hour is 5 PM or later
        # Prepare email content
        subject = f'{name} {services} Appointment on {date} at {format_hour_military_to_normal(hour)}'
        message = f"Name: {name}\nEmail:: {email}\nPhone Number: {phone}\n Service chosen: {services}\nDate: {date}\nPreferred Hour: {format_hour_military_to_normal(hour)}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['slayedbymarillc@gmail.com']  # Change to your desired recipient email

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        # Render a success page or redirect the user
        return render(request, 'consent_success.html')

    return render(request, 'schedule.html')


def thanks(request):
    return  render(request, 'consent_success.html')

def consent(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        signaturedata = request.POST.get('signature-data')

        is_signed = bool(signaturedata)
        signed_status = "Yes" if is_signed else "No"

        # Prepare email content
        subject = f'Eyelash Extensions Consent Form Submission {firstname} {lastname}'
        message = f"First Name: {firstname}\nLast Name: {lastname}\nSignature: {signed_status}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['slayedbymarillc@gmail.com']  # Change to your desired recipient email

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        # Render a success page or redirect the user
        return render(request, 'consent_success.html')

    return render(request, 'consent.html')
