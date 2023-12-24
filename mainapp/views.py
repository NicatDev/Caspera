from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from mainapp.models import *
from django.urls import translate_url
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings

def home(request):
    portfolio_categories = Portfolio_category.objects.all()
    portfolio = Portfolio.objects.all().select_related('category')
    services = Services.objects.all()
    blogs = Blog.objects.all().select_related('category').only('category','category__name','title','content_without_ck','mainimage','backimage')
    context = {
        'blogs':blogs,
        'portfolio':portfolio,
        'services':services,
        'portfolio_categories':portfolio_categories
    }
    return render(request,'home.html',context)


def about(request):
    portfolio = Portfolio.objects.all().select_related('category')
    if len(portfolio) > 5:
        portfolio = portfolio[0:5]
    context = {
        'portfolio':portfolio,
    }
    return render(request,'about.html',context)


def portfolio(request):
    portfolio_categories = Portfolio_category.objects.all()
    portfolio = Portfolio.objects.all().select_related('category')
    context = {
        'portfolio':portfolio,
        'portfolio_categories':portfolio_categories
    }
    
    return render(request,'portfolio.html',context)

from django.shortcuts import get_object_or_404

def portfolioSingle(request,slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    next_portfolio = Portfolio.objects.filter(created_at__gt=portfolio.created_at).exclude(id=portfolio.id).order_by('created_at').first()
    previous_portfolio = Portfolio.objects.filter(created_at__lt=portfolio.created_at).exclude(id=portfolio.id).order_by('-created_at').first()
    if not next_portfolio:
        next_portfolio = Portfolio.objects.exclude(id=portfolio.id).exclude(id=previous_portfolio.id).first()
    if not previous_portfolio:
        previous_portfolio = Portfolio.objects.exclude(id=portfolio.id).exclude(id=next_portfolio.id).first()
    context = {
        'next':next_portfolio,
        'pre':previous_portfolio,
        'portfolio':portfolio
    }
    return render(request, 'portfolio-single.html',context)


def services(request):
    services = Services.objects.all()

    context = {
        'services':services,
    }
    
    return render(request,'services.html',context)

def serviceSingle(request,slug):
    service = get_object_or_404(Services, slug=slug)
    related_services =  Services.objects.all().only('name','icon','description_without_ck').exclude(id=service.id)

    if len(related_services) > 4:
        related_services = related_services[0:4]

    context = {
        'service':service,
        'related_services':related_services
    }

    return render(request, 'service-single.html',context)


def blogs(request):
    blog_list = Blog.objects.all().only('mainimage','title','content_without_ck','category__name')
    paginator = Paginator(blog_list, 4)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    print(total_pages)
    context = {
        'blogs':blogs,
        'total_pages':total_pages
    }
    
    return render(request,'bloglist.html',context)