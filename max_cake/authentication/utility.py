import random

import string

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.conf import settings

def password_generator():

    password = ''.join(random.choices(string.ascii_letters+string.digits,k=8))

    return password

# Email Integration

def sending_email(subject,template,context,recipient):

    print(recipient)

    sender = settings.EMAIL_HOST_USER

    email_obj = EmailMultiAlternatives(subject, from_email=sender, to=[recipient])

    content = render_to_string(template,context)

    email_obj.attach_alternative(content, 'text/html')

    email_obj.send()

    print('Mail snt')