from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

class MainView(View):
	def get(self, request):
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = authenticate(username=username, password=password)
		template = loader.get_template('csasite/index.html')
		context = RequestContext(request)
		if user is not None:
			if user.is_active:
				login(request, user)
				# Redirect to a success page.
				context["auth"] = "You're authourized"
			else:
				# Return a 'disabled account' error message
				context["auth"] = "Disabled account"
		else:
			# Return an 'invalid login' error message.
			context["auth"] = "Invalid login"
		return HttpResponse(template.render(context))
