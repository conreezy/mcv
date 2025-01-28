import os

from django.http import StreamingHttpResponse
#from RETS_Manager.settings import BASE_DIR
#from ddf_manager import manager as ddf_manager

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
import requests
from requests import Request, Session
import json

from .forms import ContactForm
#from .models import Address

#Home Page view. Loads the documenation
# def home_page(request):
#     content = open(os.path.join(BASE_DIR, 'documenation.txt')).read()
#     response = StreamingHttpResponse(content)
#     response['Content-Type'] = 'text/plain; charset=utf8'
#     return response

#test_ddf view. Performs a sample update then displays the log file.
# def test_ddf(request):
#     ddf_manager.update_server(sample=True)
#     content = open(os.path.join(BASE_DIR, 'ddf_client.log')).read()
#     response = StreamingHttpResponse(content)
#     response['Content-Type'] = 'text/plain; charset=utf8'
#     return response

def home_page(request):
    title = "Home"

    #listings = Address.objects.filter(City="Ottawa")
    context = {
                "title": title,
                #'listings': listings
              }
    template_name = "index.html"
    return render(request, template_name, context)

def idx_page(request):
    title = "IDX"

    #listings = Address.objects.filter(City="Ottawa")
    context = {
                "title": title,
                #'listings': listings
              }
    template_name = "idx.html"
    return render(request, template_name, context)

def listings_page(request):
    title = "Listings"

    #listings = Address.objects.filter(City="Ottawa")
    context = {
                "title": title,
                #'listings': listings
              }
    template_name = "listings.html"
    return render(request, template_name, context)

def home_search_page(request):
    my_title = "Home Search"

    ### --- DDF api
    url = 'https://data.crea.ca/Login.svc/Login'

    headers = {'username': '40re0H4jZqvcTSOaxBji22S0',
               'password': 'QB4zjCqcLSJgfZfKnDfjJe0m'} 

    session = Session()
    session.headers.update(headers)
    response = session.get(url)
    ddf_info = json.loads(response.text)

    template_name = "home_search.html"
    context = {"title": my_title}
    return render(request, template_name, context)

def buyer_seminar_page(request):
    my_title = "FIRST TIME HOME BUYER SEMINAR OTTAWA"
    context = {"title": my_title}
    return render(request, "buyer_seminar.html", context)

def buyer_guide_page(request):
    my_title = "HOME BUYER GUIDE"
    context = {"title": my_title}
    return render(request, "buyer_guide.html", context)

def mortgage_calc_page(request):
    my_title = "MORTGAGE CALCULATOR"
    context = {"title": my_title}
    return render(request, "mortgage-calc.html", context)

def cash_flow_page(request):
    my_title = "CASH FLOW CALCULATOR"
    context = {"title": my_title}
    return render(request, "cashflow-calc.html", context)

def consultation_page(request):
    my_title = "LISTING CONSULTATION"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    return render(request, "consultation.html", context)

def move_list_page(request):
    my_title = "MOVING CHECKLIST"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    return render(request, "move-list.html", context)

def resources_page(request):
    my_title = "RESOURCES"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    return render(request, "resources.html", context)

def renters_page(request):
    my_title = "RENTERS"
    context = {"title": my_title}
    return render(request, "renters.html", context)

def neighbourhood_page(request):
    my_title = "ABOUT US"
    context = {"title": my_title}
    return render(request, "neighbourhoods.html", context)

def contact_page(request):
    my_title = "CONTACT US"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    template_name = "contact.html"
    return render(request, template_name, context)

def testimonials_page(request):
    my_title = "TESTIMONIALS"
    context = {"title": my_title}
    template_name = "testimonials.html"
    return render(request, template_name, context)