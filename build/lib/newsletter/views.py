from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.

def home(request):
    title = "Welcome"
    if request.user.is_authenticated:
            title = "Hello %s"%(request.user)

    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        # print (instance)
        # print (request.POST)
        if not instance.full_name:
            instance.full_name = "Name is not supplied"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request,"home.html",context)



def contact(request):
    form = ContactForm(request.POST or None)
    
    context = {
        "form":form,
    }

    if form.is_valid():
        for key in form.cleaned_data:
            print (key, form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = """
        %s:%s via %s
        """%(form_full_name, form_message, form_email)

        html_message = """
        <h1>hello %s</h1>
        """%(form_full_name)
        send_mail(subject, contact_message, from_email, to_email, html_message=html_message)



    return render(request,"forms.html",context)