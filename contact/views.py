from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from testcups.contact.models import Contact


def contact(request):
    contact = Contact.objects.get(id=1)    
    return render_to_response('contact.html',
                              context_instance=RequestContext(request, {'contact': contact}))
