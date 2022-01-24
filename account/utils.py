from django.core.mail import send_mail


def send_welcome_email(email):
    message = f'Dear {email}, Welcome to Burger King'
    send_mail(
        'Welcome to Burger King',
        message,
        'burgerkingadmin@burger.net',
        [email],
        fail_silently=False
    )
