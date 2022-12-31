from django.db import models
from django.urls import reverse
from slugify import slugify
from django.db import IntegrityError


class Order(models.Model):
    title = models.CharField(max_length=255, 
                             db_index=True, 
                             verbose_name='Title',
                             blank=True,
                             null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    count = models.FloatField(verbose_name='Value')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, verbose_name='Category')
    has_image = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('order', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=255,
                             db_index=True,
                             verbose_name='Title',
                             blank=False,
                             unique=True)
    slug = models.SlugField(null=True, blank=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            # has_slug = Category.objects.filter(slug=slug).exists()
            # count = 1
            # while has_slug:
            #     count += 1
            #     slug = slugify(self.title)+'-'+str(count)
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})
        # return reverse('category', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Image(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Order', related_name='images')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True, verbose_name='Picture')

    def __str__(self):
        return self.image.url

    class Meta:
        ordering = ['pk']

class Report(models.Model):
    title = models.CharField(max_length=255,
                         db_index=True,
                         verbose_name='Title',
                         blank=False,
                         unique=True)
    file = models.FileField(upload_to='report/%Y/%m/%d/', null=True, blank=True, verbose_name='Report file')
    date_month = models.DateField(verbose_name='Date')
    slug = models.SlugField(null=True, blank=True, editable=False, unique=True)
    revenue = models.IntegerField(default=0, blank=False, null=False)
    expend = models.IntegerField(default=0, blank=False, null=False)
    balance = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_month']

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            self.slug = f'report-{slug}'
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            Report.objects.get(slug=self.slug).delete()
        else:
            super().save(*args, **kwargs)
            

    def get_absolute_url(self):
        return reverse('report', kwargs={"slug": self.slug})
        
