from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from .country_names import COUNTRY_CHOICES
from .languages import LANGUAGE_CHOICES
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
    # CURRENCY = [
    #     ('ETB', 'BIRR'),
    #     ('$', 'USD'),
    # ]
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
    project_manager = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name="project", default = CustomUser)
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

  
    def save(self, *args, **kwargs):      
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.projectName, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.projectName, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Project, self).save(*args, **kwargs)


class Invoice(models.Model):
    TERMS = [
    ('30 days', '30 days'),
    ('45 days', '45 days'),
    ('60 days', '60 days'),
    ('Contract', 'Contract')
    ]

    STATUS = [
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    dueDate = models.DateField(null=True, blank=True)
    paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notes = models.TextField(null=True, blank=True)

    #RELATED fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.number, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)

class Order(models.Model):
    CURRENCY = [
        ('ETB', 'BIRR'),
        ('$', 'USD'),
    ]
    title = models.CharField(null=True, blank=True, max_length=100)
    OrderDate = models.DateField(null=True, blank=True)
    clientDeadline = models.DateField(null=True, blank=True)
    source_languages = models.CharField(null=True, blank=True, max_length=300)
    target_languages = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='ETB', max_length=100)

    # #Related Fields
    invoice = models.ForeignKey(Invoice, blank=True, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE )
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    # def get_absolute_url(self):
    #     return reverse('product-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Order, self).save(*args, **kwargs)


    def total_price(self):
        return self.quantity * self.price
        print(Order.objects.all()[0].total_price)

class Vendor(models.Model):

    #Basic Fields.
    vendorName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    country = models.CharField(blank=True, choices=COUNTRY_CHOICES, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)
    mother_language = models.CharField(blank=True, choices=LANGUAGE_CHOICES, max_length=300)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.vendorName, self.country, self.uniqueId)


    # def get_absolute_url(self):
    #     return reverse('vendor-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.vendorName, self.country, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.vendorName, self.country, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Vendor, self).save(*args, **kwargs)

