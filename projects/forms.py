from django import forms
from django.forms import ModelForm, Textarea

# from accounts.models import CustomUser

from .models import *

# import json

# Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = ['clientName', 'clientLogo', 'addressLine1', 'country', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']
        fields = ['clientName',  'addressLine1', 'country', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']
       
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'projectName', 'description', 'status', 'budgetedamount', 'project_manager', 'client'
            ] 
        widgets = {
            'description': Textarea(attrs={"class": "form-control", 'style': 'max-height: 50px;',
                'placeholder': 'Describe the project'}),
           
        }

        labels = {
            'projectName': 'Project Name',
            'budgetedamount': 'Project Budget',
            'project_manager': 'Project Manager',
        }
   
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendorName', 'addressLine1', 'country', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber', 'mother_language']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'project', 'OrderDate', 'clientDeadline', 'source_languages', 'target_languages',
            'description', 'quantity', 'price', 'currency', 
        ]

        widgets = {
            'description': Textarea(attrs={"class": "form-control", 'style': 'max-height: 50px;',
                'placeholder': 'Describe the order'}),
            'OrderDate': DateInput(attrs={'label': 'Start Date'}),
            'clientDeadline': DateInput(attrs={"class": "form-group col-6"}),
        }

        labels = {
            'OrderDate': 'Order Date',
            'clientDeadline' : 'client Deadline Date',
            'source_languages': 'Source language(s)',
            'target_languages': 'Target language(s)',
            'project_manager': 'Project Manager',
        }


class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
    ('30 days', '30 days'),
    ('45 days', '45 days'),
    ('60 days', '60 days'),
    ('Contract', 'Contract'),
    ]
    STATUS_OPTIONS = [
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = forms.CharField(
                    required = True,
                    label='Invoice Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}),)
    paymentTerms = forms.ChoiceField(
                    choices = THE_OPTIONS,
                    required = True,
                    label='Select Payment Terms',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Change Invoice Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    notes = forms.CharField(
                    required = True,
                    label='Enter any notes for the client',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}),)

    dueDate = forms.DateField(
                        required = True,
                        label='Invoice Due',
                        widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('dueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('paymentTerms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notes',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        model = Invoice
        fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']

class PurchaseOrderForm(forms.ModelForm):
    THE_OPTIONS = [
    ('30 days', '30 days'),
    ('45 days', '45 days'),
    ('60 days', '60 days'),
    ('Contract', 'Contract'),
    ]
    STATUS_OPTIONS = [
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = forms.CharField(
                    required = True,
                    label='PO Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter PO Title'}),)
    paymentTerms = forms.ChoiceField(
                    choices = THE_OPTIONS,
                    required = True,
                    label='Select Payment Terms',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Change PO Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    notes = forms.CharField(
                    required = True,
                    label='Enter any notes for the Vendor',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}),)

    dueDate = forms.DateField(
                        required = True,
                        label='PO Due',
                        widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('dueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('paymentTerms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notes',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        model = PurchaseOrder
        fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'description', 'job_type', 'source_language', 'target_language',
            'project_manager', 'quantity', 'rate', 'currency', 'startDate', 'deadlineDate',
            'evaluated', 'project', 'assigned_to', 'status',
        ]

        widgets = {
            'description': Textarea(attrs={"class": "form-control", 'style': 'max-height: 50px;',
                'placeholder': 'Describe the Job here'}),
            'startDate': DateInput(attrs={'label': 'Start Date'}),
            'deadlineDate': DateInput(attrs={"class": "form-group col-6"}),
        }

        labels = {
            'startDate': 'Start Date',
            'deadlineDate' : 'Deadline Date',
            'source_languages': 'Source language',
            'target_languages': 'Target language',
            'project_manager': 'Project Manager',
            'assigned_to': 'Assigned To',
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            'reviewer', 'reviewee', 'job','text', 'rate', 
        ]

        widgets = {
            'text': Textarea(attrs={"class": "form-control", 'style': 'max-height: 50px;',
                'placeholder': 'Describe the rating'}),
        }

        labels = {
            'reviewer': 'Approved by',
            'reviewee' : 'Reviewed Vendor Name',
            'job': 'Rated Job',
            'text': 'Comment',
            'rate': 'Rate',
            
        }
# class SettingsForm(forms.ModelForm):
#     class Meta:
#         model = Settings
#         fields = ['clientName', 'clientLogo', 'addressLine1', 'country', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']


class ClientSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = Client.objects.all()
        self.CLIENT_CHOICES = [('-----', '--Select a Client--')]


        for client in self.CLIENT_LIST:
            d_t = (client.uniqueId, client.clientName)
            self.CLIENT_CHOICES.append(d_t)


        super(ClientSelectForm,self).__init__(*args,**kwargs)

        self.fields['client'] = forms.ChoiceField(
                                        label='Choose a related client',
                                        choices = self.CLIENT_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = Invoice
        fields = ['client']


    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return Client.objects.get(uniqueId=c_client)

class VendorSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_vendor = kwargs.pop('initial_vendor')
        self.VENDOR_LIST = Vendor.objects.all()
        self.VENDOR_CHOICES = [('-----', '--Select a Vendor--')]


        for vendor in self.VENDOR_LIST:
            d_t = (vendor.uniqueId, vendor.vendorName)
            self.VENDOR_CHOICES.append(d_t)


        super(VendorSelectForm,self).__init__(*args,**kwargs)

        self.fields['vendor'] = forms.ChoiceField(
                                        label='Choose a related vendor',
                                        choices = self.VENDOR_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = PurchaseOrder
        fields = ['vendor']


    def clean_vendor(self):
        c_vendor = self.cleaned_data['vendor']
        if c_vendor == '-----':
            return self.initial_vendor
        else:
            return Vendor.objects.get(uniqueId=c_vendor)