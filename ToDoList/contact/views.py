from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact_detail.html'

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'phone_number']
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'phone_number']
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')
