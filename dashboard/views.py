from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

class MainView(View):
    def get(self, request):
        template = loader.get_template('dashboard/index.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))
