from django.shortcuts import render, reverse
from django.views import generic
from .forms import ContactForm
from django.conf import settings
from django.contrib impor messages
from django.core.mail import sen_email


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        message.info(
            self.request, "Gracias por tu opinion, nos pondremos en contacto lo mas pronto posible")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        fill_message = f """
            Mensaje recibido de {name}, {email}
            ___________________________________

            {message}
            """
            send_mail(
                subject = "Mensaje recibido"
                message =  full_messge
                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [settings.NOTIFY_EMAIL]
            )
            return super(ContactView, self).form_valid(form)
# Create your views here.
