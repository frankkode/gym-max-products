from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Subject = form.cleaned_data['Subject']
            Email = form.cleaned_data['Email']
            Message = form.cleaned_data['Message']+ '\n' + form.data['Email']
            try:
                send_mail(Subject, Message, Email, ['frankmasabo55@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def SuccessView(request):
    return render(request, 'success.html')
