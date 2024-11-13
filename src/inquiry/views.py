from threading import Thread
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from b2b.settings import EMAIL_HOST_USER
from .forms import InquiryForm


def send_async_login_email(subject, message, from_email, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
    )


def inquiry_page(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_phone = form.cleaned_data['contact_phone']
            inquiry_subject = form.cleaned_data['inquiry_subject']
            inquiry_message = form.cleaned_data['inquiry_message']
            cc_myself = form.cleaned_data['cc_myself']
            
            # send email here
            recipient_list = [EMAIL_HOST_USER]
            if cc_myself:
                recipient_list.append(contact_email)
            
            thr = Thread(target=send_async_login_email,
                         args=[
                             inquiry_subject,
                             inquiry_message,
                             EMAIL_HOST_USER,
                             recipient_list
                         ]
                         )
            thr.start()
            # TODO: add a success message to let the user know that their inquiry has been sent
            messages.success(
                request,
                "Check your email, we've sent you a ???"
            )
            
            return redirect('/')
    
    return render(request, 'inquiry/inquiry_page.html', {'form': InquiryForm()})
