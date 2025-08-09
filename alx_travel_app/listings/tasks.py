from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation(recipient_email, booking_details):
    subject = 'Your Booking Confirmation'
    message = f"""
    Thank you for your booking!
    
    Booking Details:
    - Property: {booking_details['property_name']}
    - Check-in: {booking_details['check_in']}
    - Check-out: {booking_details['check_out']}
    - Total Price: ${booking_details['total_price']}
    
    We look forward to hosting you!
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )
