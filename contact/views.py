from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from testcups.contact.models import Contact
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm


def contact(request):
    contact = Contact.objects.get(id=1)
    return render_to_response('contact.html',
           context_instance=RequestContext(request, {'contact': contact}))
        
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact

           
@login_required
def edit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=Contact.objects.get(id=1))
        if form.is_valid():
            form.save()
    else:
        form = ContactForm(instance=Contact.objects.get(id=1))
    return render_to_response("edit_contact.html", RequestContext(request, {'form': form}))

