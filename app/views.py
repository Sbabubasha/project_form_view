from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.

from django.views.generic import FormView
from app.forms import*

class Student(FormView):
    template_name='student.html'
    form_class=Studentform
    def form_valid(self, form):
        form.save()
        return HttpResponse('data is inserted')