from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from testcups.middleware.models import Middleware


def middleware(request):
    middleware = Middleware.objects.all().order_by('-id')[0:10]
    return render_to_response('middleware.html',
         context_instance=RequestContext(request, {'middleware': middleware}))
