from django.shortcuts import render
from django.views.generic import CreateView


# Create your views here.

class RegistroView(CreateView):
    form_class = DatosUserCreacionForm
    template_name = 'register.html'
    success_url = reverse_lazy('chat')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            login(self.request, self.object)
            return response
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)