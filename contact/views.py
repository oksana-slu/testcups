from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from testcups.contact.models import Contact, ContactForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse


def contact(request):
    contact = Contact.objects.get(id=1)
    return render_to_response('contact.html',
           context_instance=RequestContext(request, {'contact': contact}))
           
           
def edit_contact(request):
    initial = None
    if request.user.is_authenticated():
        user = request.user
        item_contact = Contact.objects.get(name=user)
        initial = dict(name=item_contact.name,
                       last_name=item_contact.last_name,
                       birth=item_contact.birth,
                       bio=item_contact.bio,
                       email=item_contact.email,
                       jabber=item_contact.jabber,
                       skype=item_contact.skype,
                       other_contacts=item_contact.other_contacts)                       
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if request.user.is_authenticated():
                item_contact.name=cleaned_data['name']
                item_contact.last_name=cleaned_data['last_name']
                item_contact.birth=cleaned_data['birth']
                item_contact.bio=cleaned_data['bio']
                item_contact.email=cleaned_data['email']
                item_contact.jabber=cleaned_data['jabber']
                item_contact.skype=cleaned_data['skype']
                item_contact.other_contacts=cleaned_data['other_contacts']
                item_contact.save()
            else:
                Contact_object = Contact(name=cleaned_data['name'],
                                     last_name=cleaned_data['last_name'],
                                     ibirth=cleaned_data['birth'],
                                     bio=cleaned_data['bio'],
                                     email=cleaned_data['email'],
                                     jabber=cleaned_data['jabber'],
                                     skype=cleaned_data['skype'],
                                     other_contacts=cleaned_data['other_contacts'])            
                Contact_object.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm(initial=initial)
    return render_to_response('edit_contact.html', {},
           context_instance=RequestContext(request, {'form': form}))    
