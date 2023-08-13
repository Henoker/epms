from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
from .country_names import COUNTRY_CHOICES
from .languages import LANGUAGE_CHOICES
from accounts.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.dispatch import receiver





class Client(models.Model):

    #Basic Fields.
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    clientLogo  = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
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


    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})


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
    due_date = models.DateField(null=True, blank=True)


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

    def check_overdue_status(self):
        if (
            self.due_date is not None
            and self.due_date < timezone.now().date()
            and self.status not in ['Delivered', 'Complained', 'Approved']
        ):
            self.status = 'Overdue'

    @receiver(pre_save, sender='projects.Project')
    def update_project_status(sender, instance, **kwargs):
        if (
            instance.due_date is not None
            and instance.due_date < timezone.now().date()
            and instance.status not in ['Delivered', 'Complained', 'Approved']
        ):
            instance.status = 'Overdue'

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
    paymentTerms = models.CharField(choices=TERMS, default='30 days', max_length=100)
    status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notes = models.TextField(null=True, blank=True)

    #RELATED fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    def total_amount(self):
        return sum(order.total_price() for order in self.orders.all())


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


    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


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

    # @receiver(post_save, sender=Order)
    # def update_project_status(sender, instance, **kwargs):
    #     instance.project.update_status()

class Vendor(models.Model):
    LINGUISTIC_LEVEL = [
        ('NOVICE', 'NOVICE'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),

    ]
    EDUCATION_LEVEL = [
        ('CERTIFICATE', 'CERTIFICATE'),
        ('DIPLOMA', 'DIPLOMA'),
        ('UNIVERSITY DEGREE', 'UNIVERSITY DEGREE'),
        ('GRADUATE DEGREE', 'GRADUATE DEGREE'),
        ('DOCTORIAL LEVEL', 'DOCTORIAL LEVEL'),
    ]

    #Basic Fields.
    vendorName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    country = models.CharField(blank=True, choices=COUNTRY_CHOICES, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)
    mother_language = models.CharField(blank=True, choices=LANGUAGE_CHOICES, max_length=300)
    language_skills = models.CharField(blank=True, null=True, max_length=300)
    lingustic_level = models.CharField(blank=True, choices=LINGUISTIC_LEVEL, max_length=100)
    education_level = models.CharField(blank=True, choices=EDUCATION_LEVEL, max_length=100)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.vendorName, self.country, self.uniqueId)


    def get_absolute_url(self):
        return reverse('vendor-detail', kwargs={'slug': self.slug})

    
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.vendorName, self.country, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.vendorName, self.country, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Vendor, self).save(*args, **kwargs)


class PurchaseOrder(models.Model):
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
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.number, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})
    
    def total_price(self):
        return sum(job.rate() for job in self.job.all())


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(PurchaseOrder, self).save(*args, **kwargs)


class Job(models.Model):
    JOBTYPE = [
    ('TRANSLATION', 'TRANSLATION'),
    ('REVISION', 'REVISION'),
    ('EDITING', 'EDITING'),
    ('TRANSCREATION', 'TRANSCREATION'),
    ('COPY WRITING', 'COPY WRITING'),
    ('PROOFREADING', 'PROOFREADING'),
    ('DTP', 'DTP'),
    ('SUBTITLING', 'SUBTITLING'),
    ('INTREPRETATION', 'INTREPRETATION'),
    ('VOICEOVER', 'VOICEOVER'),
    ]

    STATUS = [
        ('In Preparation', 'In Preparation'),
        ('Requested', 'Requested'),
        ('Assigned-waiting', 'Assigned-waiting'),
        ('In Progress', 'In Progress'),
        ('Overdue', 'Overdue'),
        ('Delivered', 'Delivered'),
        ('Complained', 'Complained'),
        ('Approved', 'Approved'),
    ]
    CURRENCY = [
    ('ETB', 'BIRR'),
    ('$', 'USD'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    source_language = models.CharField(blank=True, choices=LANGUAGE_CHOICES, max_length=300)
    target_language = models.CharField(blank=True, choices=LANGUAGE_CHOICES, max_length=300)
    job_type = models.CharField(choices=JOBTYPE, default='TRANSLATION', max_length=100)
    quantity = models.FloatField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='ETB', max_length=100)
    project_manager = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name="assigned_by")
    startDate = models.DateField(blank=True, null=True)
    deadlineDate = models.DateField(blank=True, null=True)
    status = models.CharField(choices=STATUS, default='In Preparation', max_length=100)
    evaluated = models.BooleanField(default=False)


    #Related Fields
    purchaseOrder = models.ForeignKey(PurchaseOrder, blank=True, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE, related_name="Main_Project")
    assigned_to = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.CASCADE, related_name="Job_owner")

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Job, self).save(*args, **kwargs)


    def total_price(self):
        if self.quantity is None or self.rate is None:
            return 0  # Return a default value, such as 0, when either quantity or rate is None
        return self.quantity * self.rate
    
    def check_overdue_status(self):
       if (
            self.deadlineDate is not None
            and self.deadlineDate < timezone.now().date()
            and self.status not in ['Delivered', 'Complained', 'Approved']
        ):
            self.status = 'Overdue'

    @receiver(pre_save, sender='projects.Job')
    def update_project_status(sender, instance, **kwargs):
        if (
            instance.deadlineDate is not None
            and instance.deadlineDate < timezone.now().date()
            and instance.status not in ['Delivered', 'Complained', 'Approved']
        ):
            instance.status = 'Overdue'


       


class Rating(models.Model):
    RATE_CHOICES = [
        (1, 'Below Expectation greater than 0.02'),
        (2, 'Meet Expectaion 0.02'),
        (3, 'Exceed Expectaions less than 0.02'),
    ]
    
    reviewer = models.ForeignKey(CustomUser, related_name="evaluator", on_delete=models.CASCADE, null=True, blank=True)
    reviewee = models.ForeignKey(Vendor, null=True, blank=True, related_name="evaluated_vendor", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True, related_name='jobrate')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=200, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.reviewer, self.job)
    
    


class Settings(models.Model):
    #Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    clientLogo = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
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


    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)


class Quotation(models.Model):
    TERMS = [
    ('30 days', '30 days'),
    ('45 days', '45 days'),
    ('60 days', '60 days'),
    ('Contract', 'Contract')
    ]

    STATUS = [
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('EXPIRED', 'EXPIRED'),
    ('ACCEPTED', 'ACCEPTED'),
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
        return reverse('quotation-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Quotation, self).save(*args, **kwargs)

class Request(models.Model):
    CURRENCY = [
        ('ETB', 'BIRR'),
        ('$', 'USD'),
    ]
    title = models.CharField(null=True, blank=True, max_length=100)
    RequestDate = models.DateField(null=True, blank=True)
    proposedStartDate = models.DateField(null=True, blank=True)
    clientDeadline = models.DateField(null=True, blank=True)
    source_languages = models.CharField(null=True, blank=True, max_length=300)
    target_languages = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='ETB', max_length=100)

    # #Related Fields
    quote = models.ForeignKey(Quotation, blank=True, null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Request, self).save(*args, **kwargs)


    def total_price(self):
        return self.quantity * self.price
       