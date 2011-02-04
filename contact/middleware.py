from testcups.middleware.models import Middleware


class RequestMiddleware(object):
    def process_request(self, request):
        if request.user.is_anonymous():
            user = None
        else:
            user = request.user
        if 'LANG' in request.META:
            lang = request.META['LANG']
        else:
            lang = ''
        inst = Middleware()
        inst.user = user
        inst.lang = lang
        inst.path_info = request.META['PATH_INFO']
        inst.remote_addr = request.META['REMOTE_ADDR']
        inst.save()
