from django.contrib.sitemaps import Sitemap
from  mainapp.models import *
from django.urls import reverse


class BlogSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at
    
    def location(self, obj):
        return obj.get_absolute_url()


class TagSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Tag.objects.all()
    
    def location(self, obj):
        return obj.get_absolute_url()

class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Services.objects.all()

    def location(self, obj: Services) -> str:
        return obj.get_absolute_url()


class PortfolioCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Portfolio_category.objects.all()

    def location(self, obj: Portfolio_category) -> str:
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):

    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'home', 'about', 'services',
            'blogs', 'portfolio',  'contact',
        ]

    def location(self, item):
        return reverse(item)

