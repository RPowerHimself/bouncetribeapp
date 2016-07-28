from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import GetFeedbackProjectForm




def home(request):
	header = "Get Feedback"
	form = GetFeedbackProjectForm(request.POST or None)
	context = {
		'header': header,
		'form': form,
	}
	
	template = 'contact.html'
	return render(request, template, context)
















# def home(request):
# 	title = "Contact Us"
# 	form = ContactForm(request.POST or None)
	


# 	confirm_message = None

# 	if form.is_valid():
# 		comment = form.cleaned_data['comment']
# 		name = form.cleaned_data['name']
# 		sbj = 'Message from The Feedback Lounge'
# 		msg = '%s %s' %(comment, name)
# 		frm = form.cleaned_data['email']
# 		to_us = [settings.EMAIL_HOST_USER]
# 		print sbj, msg, frm, to_us
# 		send_mail(sbj, msg, frm,
#     		to_us, fail_silently=True)
# 		title = 'Thank you'
# 		confirm_message = """
# 		Thank you for your message.
# 		"""



# 		form = None

# 	context = {
# 		'title': title,
# 		'form': form,
# 		'confirm_message': confirm_message
# 	}
	
# 	template = 'contact.html'
# 	return render(request, template, context)