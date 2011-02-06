from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from testcups.contact.models import Contact, Middleware
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.contrib.admin import widgets


def contact(request):
    contact = Contact.objects.get(id=1)
    return render_to_response('contact.html',
           context_instance=RequestContext(request, {'contact': contact}))


class ContactForm(ModelForm):    
    class Meta:
        model = Contact
        widgets = {
            'birth': widgets.AdminDateWidget
        }


def middleware(request):
    middleware = Middleware.objects.all().order_by('-id')[0:10]
    return render_to_response('middleware.html',
         context_instance=RequestContext(request, {'middleware': middleware}))


@login_required
def edit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=Contact.objects.get(id=1))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm(instance=Contact.objects.get(id=1))
    return render_to_response("edit_contact.html",
                              RequestContext(request, {'form': form}))
