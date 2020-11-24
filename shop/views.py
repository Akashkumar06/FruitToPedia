from django.shortcuts import render
from .models import Team, Contact
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError


def contect(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        message= 'Dear ' + fullname +',\n\n      Your message sent successfully to Khetihar App.'+'\n      We will respond soon....Thanks.\n\n\n Regards From Team\n AgroAcres💚\n A Smart Agriculture\n  Platform'
        try:
            send_mail('!!Welcome To  AgroAcres!!',message,'agroacresteambbsr@gmail.com', [email, ])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        contact = Contact(fullname=fullname, email=email, phone=phone, msg=msg)
        contact.save()
        return HttpResponseRedirect('/')
    team = Team.objects.all()
    context = {'team': team}
    return render(request, 'index.html', context)
