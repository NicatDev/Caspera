from django.db import models
from django.contrib.auth import get_user, get_user_model
from mainapp.utils import *
from datetime import datetime
from django.utils.text import slugify

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True,blank=True,null=True,)
    seo_title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    seo_keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    seo_alt = models.CharField(max_length=1200,null=True,blank=True)
    seo_description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
    
    class Meta:
        abstract = True

class Services(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    description_without_ck = models.CharField(max_length = 200)
    icon = models.ImageField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    bottomdescription = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Services.objects.filter(slug=new_slug).exists():
            count = 0
            while Services.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Services, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length = 200)

class Tag(models.Model):
    name = models.CharField(max_length = 120)

class Blog(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length = 200)
    mainimage = models.ImageField()
    backimage = models.ImageField(null=True,blank=True)
    content = models.TextField()
    content_without_ck = models.CharField(max_length = 200)
    content_2 = models.TextField()
    content_without_ck_2 = models.CharField(max_length = 200)
    in_home = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.title)
        self.slug = new_slug
        if Blog.objects.filter(slug=new_slug).exists():
            count = 0
            while Blog.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.title)}-{count}"
                count += 1
        super(Blog, self).save(*args, **kwargs)



class Blog_images(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = 'blog_images')
    image = models.ImageField()

    def __str__(self):
        return self.blog.title
    

class Portfolio_category(models.Model):
    name = models.CharField(max_length = 200)

class Portfolio(BaseMixin):
    category = models.ForeignKey(Portfolio_category,on_delete = models.CASCADE, related_name = 'portfolio')
    name = models.CharField(max_length = 800)
    description = models.TextField()
    image = models.ImageField()
    second_image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Portfolio.objects.filter(slug=new_slug).exists():
            count = 0
            while Portfolio.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Portfolio, self).save(*args, **kwargs)

class Message(models.Model):
    full_name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    

    
    

    



    # def save(self, *args, **kwargs):
    #     self.pk = 1  
    #     super(HomeHeader, self).save(*args, **kwargs)
        