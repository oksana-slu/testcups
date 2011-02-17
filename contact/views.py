from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from testcups.contact.models import Contact, Middleware
from testcups.contact.forms import ContactForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.template.loader import render_to_string
from django.contrib import messages


def contact(request):
    contact = Contact.objects.get(id=1)
    return render_to_response('contact.html',
           context_instance=RequestContext(request, {'contact': contact}))


@login_required
def middleware(request):
    if request.method == 'POST':
        item = Middleware.objects.get(id=request.POST['id'])
        item.priority = int(request.POST['priority'])
        item.save()
        messages.success(request, 'Changes successfully saved.')
        return redirect('contact_middleware')

    priority_sort_prefix = '-'
    if 'sort' in request.GET and request.GET['sort']=='1':
        priority_sort_prefix = ''
    sort = '1' if priority_sort_prefix == '' else '0'

    middleware = Middleware.objects.all().order_by('%spriority' % priority_sort_prefix, '-id')[0:10]

    return render_to_response('middleware.html',
         context_instance=RequestContext(request, {'middleware': middleware,
                                                   'sort': sort}))


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
