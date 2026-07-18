from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    return render(request,"index.html")

# simple mail sending and message

def mail_send(request):
    data = request.POST
    to = data.get('to')
    sub  =data.get('subject')
    message = data.get('message')
    
    send_mail(
        subject=sub,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to],
        # html_message='<h1>Hello TOPS</h1>', # fixed message 
        html_message=message,
        fail_silently=False,
    )
    return render(request,"index.html",{'msg':'Mail Sent Successfully!....'})

# mail with attach html file
def mail_html(request):
    html_message = render_to_string(
        "demo.html",
    )
    email = EmailMultiAlternatives(
        subject="Welcome",
        body="Your email client does not support HTML.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["tailory123@gmail.com"],
    )
    email.attach_alternative(html_message, "text/html")
    email.send()

    return HttpResponse("Mail is Sent...")

#mail with image attach or pdf attach
def mail_attach(request):
    email = EmailMessage(
        subject="Employee Report",
        body = "please find the attach report",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['topstechnologiesda@gmail.com'],
    )

    email.attach_file("media/Report.pdf")
    email.send()
    return HttpResponse("Mail Sent Successfully!...")
