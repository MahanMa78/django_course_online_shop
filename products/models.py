from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('Product Image'),upload_to="product/product_cover/",blank=True)

    datetime_created = models.DateTimeField(default=timezone.now,verbose_name=_('Date Time Of Creation'))
    datetime_modified = models.DateTimeField(auto_now=True)
    
    #baraye namayesh esmha dar pannel admin
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.pk])
    

class ActiveCommentManager(models.Manager):
    def get_queryset(self):#overright method ---> yani dar dakhel khode Class bode
        return super(ActiveCommentManager,self).get_queryset().filter(active=True)
    
class Comment(models.Model):
    PRODUCT_STARS = [
        ('1',_('Very Bad')),
        ('2',_("Bad")),
        ('3',_("Normal")),
        ('4',_("Good")),
        ('5',_("Perfect")),
    ]

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="comments")
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name='Comment author',
        )
    
    body = models.TextField(verbose_name=_('Comment text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS,verbose_name=_('What is your score?'))
    # recommend = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    #manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    
    
    
