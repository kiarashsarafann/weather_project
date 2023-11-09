from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactUsModelForm


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
