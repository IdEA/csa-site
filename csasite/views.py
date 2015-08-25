from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

class MainView(View):
	@login_required
	def get(self, request):
		template = loader.get_template('csasite/index.html')
		context = RequestContext(request)
		return HttpResponse(template.render(context))
