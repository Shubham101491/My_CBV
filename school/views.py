from django.db.models import fields
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                UpdateView,DeleteView)
from django.views.generic.edit import CreateView
from school import models
from school.models import School
from django.urls import reverse_lazy

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Based View Example")

# Practic again
# class IndexView(TemplateView):
#     template_name  = 'school/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context

class IndexView(TemplateView):
    template_name = 'school/home.html'

# Note - context_object_name,model,template_name
# these are the built-in classes of CBV 


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    # If you don't mention template path
    # it will take default template
# template path must be started templates/appname/_.html in CBV

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'school/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','princlipal','location')
    model = School
    # use to reverse url
    success_url = reverse_lazy("school:list")

class SchoolUpdateView(UpdateView):
    fields = ('name','princlipal')
    model = School
    success_url = reverse_lazy("school:list")


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("school:list")