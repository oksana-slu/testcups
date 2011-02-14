from django.shortcuts import render_to_response
from django.template import RequestContext
from testcups.contact.models import Contact, Middleware
from testcups.contact.forms import ContactForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.template.loader import render_to_string


def contact(request):
    contact = Contact.objects.get(id=1)
    return render_to_response('contact.html',
           context_instance=RequestContext(request, {'contact': contact}))


def middleware(request):
    middleware = Middleware.objects.all().order_by('-id')[0:10]
    return render_to_response('middleware.html',
         context_instance=RequestContext(request, {'middleware': middleware}))


@login_required
def edit_contact(request):
    if request.is_ajax() and request.method == 'POST':
        form = ContactForm(request.POST, instance=Contact.objects.get(id=1))
        status = 'ERROR'
        if form.is_valid():
            form.save()
            status = 'OK'

        responce_text = render_to_string("edit_contact_form.html",
                                                            {'form': form})
        return HttpResponse(simplejson.dumps({'status': status,
               'text': responce_text}), mimetype='application/javascript')

    else:
        form = ContactForm(instance=Contact.objects.get(id=1))
    return render_to_response("edit_contact.html",
                              RequestContext(request, {'form': form}))
