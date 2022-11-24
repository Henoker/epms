from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from .country_names import COUNTRY_CHOICES
# from .languages import LANGUAGE_CHOICES
from accounts.models import CustomUser


class Client(models.Model):

    #Basic Fields.
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    # clientLogo  = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
    country = models.CharField(blank=True, choices=COUNTRY_CHOICES, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.country, self.uniqueId)


    # def get_absolute_url(self):
    #     return reverse('client-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)

class Project(models.Model):
    CURRENCY = [
        ('ETB', 'BIRR'),
        ('$', 'USD'),
    ]
    STATUS = [
        ('In Preparation', 'In Preparation'),
        # ('Requested', 'Requested'),
        # ('Assigned-waiting', 'Assigned-waiting'),
        ('In Progress', 'In Progress'),
        ('Overdue', 'Overdue'),
        ('Delivered', 'Delivered'),
        ('Complained', 'Complained'),
        ('Approved', 'Approved')


    ]
    projectName = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    startDate = models.DateTimeField(blank=True, null=True)
    deadlineDate = models.DateTimeField(blank=True, null=True) 
    source_languages = models.TextField(null=True, blank=True)
    target_languages = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(choices=CURRENCY, default='R', max_length=100)
    project_manager = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name="project", default = None)
    status = models.CharField(choices=STATUS, default='In Preparation', max_length=100)
    budgetedamount = models.PositiveIntegerField()


    #RELATED fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.projectName, self.uniqueId)

    # def get_absolute_url(self):
#         return reverse('PurchaseOrder-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):      
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.projectName, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.projectName, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Project, self).save(*args, **kwargs)
    

