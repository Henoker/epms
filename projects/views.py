from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *
# from .functions import *
from accounts.models import CustomUser
# from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4
from django.db.models import Avg, Sum, F, Count
from django.http import HttpResponse

from django.template.loader import render_to_string
import os
from django.utils import timezone
from django.template.loader import get_template
import weasyprint
from weasyprint import HTML, CSS
import tempfile
from datetime import timedelta, datetime



# #Anonymous required
# def anonymous_required(function=None, redirect_url=None):

#    if not redirect_url:
#        redirect_url = 'dashboard'

#    actual_decorator = user_passes_test(
#        lambda u: u.is_anonymous,
#        login_url=redirect_url
#    )

#    if function:
#        return actual_decorator(function)
#    return actual_decorator


# def index(request):
#     context = {}
#     return render(request, 'invoice/index.html', context)



@login_required
def dashboard(request):
    all_orders = Order.objects.order_by('-OrderDate')[:10]
    clients = Client.objects.all().count()
    vendors = Vendor.objects.all().count()
    invoices = Invoice.objects.all().count()
    purchase_orders = PurchaseOrder.objects.all().count()
    jobs = Job.objects.all().count()
    projects = Project.objects.all().count()
    paidInvoices = Invoice.objects.filter(status='PAID').count()
    paidPos = PurchaseOrder.objects.filter(status='PAID').count()
    completedProjects = Project.objects.filter(status='Approved').count()
    pendingProjects = projects-completedProjects
    completedJobs = Job.objects.filter(status='Approved').count()
    total_order = Order.objects.aggregate(total_value=Sum(F('price') * F('quantity')))
    total_project_value = total_order['total_value']
    total_budget = Project.objects.aggregate(total_cost=Sum(F('budgetedamount')))
    total_budgeted_cost = total_budget['total_cost']
    last_seven_days_projects = Project.objects.filter(date_created__gte=timezone.now() - timedelta(days=7))
    order_due_today = Order.objects.filter(clientDeadline=timezone.now()+timedelta(days=0))
    overdue_orders = Project.objects.filter(due_date__lt=timezone.now())
    overdue_project_orders = Project.objects.filter(status='Overdue')
    invoice_due_today = Invoice.objects.filter(dueDate=timezone.now()+timedelta(days=0))
    rated_jobs = Rating.objects.all().count()
    green_rated = Rating.objects.filter(rate='3').count()
    yellow_rated = Rating.objects.filter(rate='2').count()
    red_rated = Rating.objects.filter(rate='1').count()
    novice = Vendor.objects.filter(lingustic_level='NOVICE').count()
    b1 = Vendor.objects.filter(lingustic_level='B1').count()
    b2 = Vendor.objects.filter(lingustic_level='B2').count()
    c1 = Vendor.objects.filter(lingustic_level='C1').count()
    c2 = Vendor.objects.filter(lingustic_level='C2').count()
    category_list = Rating.objects.values('rate').annotate(category_count=Count('rate'))
    if projects == 0:
        pending_proj_percentage = 0
    else:
        pending_proj_percentage = (completedProjects / projects) * 100
    if invoices == 0:
        paidInv_percentages = 0
    else:
        paidInv_percentages = (paidInvoices / invoices) * 100
    if purchase_orders == 0:
        paidPos_percentages = 0
    else:
        paidPos_percentages = (paidPos / purchase_orders) * 100
    if jobs == 0:
        pending_jobs_percentage = 0
    else:
        pending_jobs_percentage = (completedJobs / jobs) * 100
    if jobs == 0:
        rated_jobs_percentage = 0
    else:
        rated_jobs_percentage = (rated_jobs / jobs) * 100
    


    context = {}
    context['clients'] = clients
    context['vendors'] = vendors
    context['invoices'] = invoices
    context['purchase_orders'] = purchase_orders
    context['jobs'] = jobs
    context['projects'] = projects
    context['paidInvoices'] = paidInvoices
    context['paidPos'] = paidPos
    context['completedProjects'] = completedProjects
    context['completedJobs'] = completedJobs
    context['total_project_value'] = total_project_value 
    context['total_budgeted_cost'] = total_budgeted_cost
    context['pendingProjects'] = pendingProjects
    context['last_seven_days_projects'] = last_seven_days_projects
    context['rated_jobs'] = rated_jobs
    context['green_rated'] = green_rated
    context['yellow_rated'] = yellow_rated
    context['red_rated'] =  red_rated
    context['order_due_today'] = order_due_today
    context['invoice_due_today'] = invoice_due_today
    context['all_orders'] = all_orders
    context['category_list'] = category_list
    context['pending_proj_percentage'] = pending_proj_percentage
    context['paidInv_percentages'] = paidInv_percentages
    context['paidPos_percentages'] = paidPos_percentages
    context['pending_jobs_percentage'] = pending_jobs_percentage
    context['rated_jobs_percentage'] =  rated_jobs_percentage
    context['novice'] = novice
    context['b1'] = b1
    context['b2'] = b2
    context['c1'] = c1
    context['c2'] = c2
    context['overdue_orders'] = overdue_orders
    context['overdue_project_orders'] = overdue_project_orders


    return render(request, 'dashboard.html', context)




@login_required
def invoices(request):
    context = {}
    invoices = Invoice.objects.all().order_by('-date_created')
    context['invoices'] = invoices

    return render(request, 'invoice/invoices.html', context)

@login_required
def quotes(request):
    context = {}
    quotes = Quotation.objects.all().order_by('-date_created')
    context['quotes'] = quotes

    return render(request, 'invoice/quotes.html', context)

@login_required
def orders(request):
    context = {}
    orders = Order.objects.all().order_by('-date_created')
    context['orders'] = orders

    return render(request, 'invoice/orders.html', context)

@login_required
def requests(request):
    context = {}
    requests = Request.objects.all().order_by('-date_created')
    context['requests'] = requests

    return render(request, 'invoice/requests.html', context)

@login_required
def jobs(request):
    context = {}
    jobs = Job.objects.all().order_by('-date_created')
    context['jobs'] = jobs

    return render(request, 'invoice/jobs.html', context)

@login_required
def clients(request):
    context = {}
    clients = Client.objects.all().order_by('-date_created')
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm()
        context['form'] = form
        return render(request, 'projects/clients.html', context)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('clients')


    return render(request, 'projects/clients.html', context)

@login_required
def projects(request):
    context = {}
    projects = Project.objects.all().order_by('-date_created')
    context['projects'] = projects

    if request.method == 'GET':
        form = ProjectForm()
        context['form'] = form
        return render(request, 'projects/projects.html', context)
    return render(request, 'projects/projects.html', context)

@login_required
def addProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        client_form = ClientSelectForm(request.POST, initial_client=None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectForm()
            context = {
                'created': created,
                'form': form,
            }
            messages.success(request, 'New Project Added')
            # return render(request, 'projects/addProject.html', context)
            return redirect('projects')
        elif client_form.is_valid() and 'client' in request.POST:
            client_form.save()
            messages.success(request, "Client added to invoice succesfully")
            return redirect('projects')
        else:
            messages.error(request, 'Problem processing your request')
            return render(request, 'projects/addProject.html', context)
    else:
        form = ProjectForm()
        client_form = ClientSelectForm(initial_client=None)

        context = {
            'form': form,
            'client_form': client_form,
        }
        return render(request,'projects/addProject.html', context)
    
   

@login_required
def vendors(request):
    context = {}
    vendors = Vendor.objects.all().annotate(
    averagerating=Avg("evaluated_vendor__rate")
).order_by('-date_created')
    context['vendors'] = vendors
    

    if request.method == 'GET':
        form = VendorForm()
        context['form'] = form
        return render(request, 'projects/vendors.html', context)

    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Vendor Added')
            return redirect('vendors')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('vendors')


    return render(request, 'projects/vendors.html', context)

@login_required
def purchaseOrders(request):
    context = {}
    purchase_orders = PurchaseOrder.objects.all().order_by('-date_created')
    context['purchase_orders'] = purchase_orders

    return render(request, 'invoice/purchase-orders.html', context)

# @login_required
# def logout(request):
#     auth.logout(request)
#     return redirect('login')


# ###--------------------------- Create Invoice Views Start here --------------------------------------------- ###

@login_required
def createInvoice(request):
    #create a blank invoice ....
    number = 'INV-'+str(uuid4()).split('-')[1]
    newInvoice = Invoice.objects.create(number=number)
    newInvoice.save()

    inv = Invoice.objects.get(number=number)
    return redirect('create-build-invoice', slug=inv.slug)

def createBuildInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    orders = Order.objects.filter(invoice=invoice)


    context = {}
    context['invoice'] = invoice
    context['orders'] = orders

    if request.method == 'GET':
        order_form  = OrderForm()
        inv_form = InvoiceForm(instance=invoice)
        client_form = ClientSelectForm(initial_client=invoice.client)
        context['order_form'] = order_form
        context['inv_form'] = inv_form
        context['client_form'] = client_form
        return render(request, 'invoice/create-invoice.html', context)

    if request.method == 'POST':
        order_form  = OrderForm(request.POST)
        inv_form = InvoiceForm(request.POST, instance=invoice)
        client_form = ClientSelectForm(request.POST, initial_client=invoice.client, instance=invoice)

        if order_form.is_valid():
            obj = order_form.save(commit=False)
            obj.invoice = invoice
            obj.save()

            messages.success(request, "Invoice product added succesfully")
            return redirect('create-build-invoice', slug=slug)
        elif inv_form.is_valid and 'paymentTerms' in request.POST:
            inv_form.save()

            messages.success(request, "Invoice updated succesfully")
            return redirect('create-build-invoice', slug=slug)
        elif client_form.is_valid() and 'client' in request.POST:

            client_form.save()
            messages.success(request, "Client added to invoice succesfully")
            return redirect('create-build-invoice', slug=slug)
        else:
            context['order_form'] = order_form
            context['inv_form'] = inv_form
            context['client_form'] = client_form
            messages.error(request,"Problem processing your request")
            return render(request, 'invoice/create-invoice.html', context)


    return render(request, 'invoice/create-invoice.html', context)


def viewPDFInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    orders = Order.objects.filter(invoice=invoice)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')

    #Calculate the Invoice Total
    invoiceCurrency = ''
    invoiceTotal = 0.0
    if len(orders) > 0:
        for x in orders:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y
            invoiceCurrency = x.currency

    context = {}
    context['invoice'] = invoice
    context['orders'] = orders
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)
    context['invoiceCurrency'] = invoiceCurrency

    return render(request, 'invoice/invoice-view.html', context)
    # # Open the view in a new tab
    # response = HttpResponse(render(request, 'invoice/invoice-view.html', context))
    # response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    # response['Content-Type'] = 'application/pdf'
    # response['X-Content-Type-Options'] = 'nosniff'
    # response['Cache-Control'] = 'private, no-cache, no-store, must-revalidate'
    # response['Expires'] = '-1'
    # response['Pragma'] = 'no-cache'
    # response['Content-Security-Policy'] = "frame-ancestors 'none'"

    # return response


def viewDocumentInvoice(request, slug):
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    orders = Order.objects.filter(invoice=invoice)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')

    #Calculate the Invoice Total
    invoiceTotal = 0.0
    if len(orders) > 0:
        for x in orders:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y
    
    context = {}
    context['invoice'] = invoice
    context['orders'] = orders
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)

    html_string = render_to_string(
        'invoice/pdf-template.html',context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # # http response
    # response = HttpResponse(content_type='application/pdf;')
    # response['Content-Disposition'] = 'inline; filename=problem_list.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'
    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, 'rb')
    #     response.write(output.read())

    # return response
    # http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=invoice.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    response['Content-Security-Policy'] = "frame-ancestors 'none'"
    response['Cache-Control'] = 'private, no-cache, no-store, must-revalidate'
    response['Expires'] = '-1'
    response['Pragma'] = 'no-cache'

    # Set the headers to open the view in a new tab
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response








    


# ###--------------------------- Create Purchase Order Views Start here --------------------------------------------- ###


@login_required
def createPo(request):
    #create a blank Po ....
    number = 'PO-'+str(uuid4()).split('-')[1]
    newPo = PurchaseOrder.objects.create(number=number)
    newPo.save()

    po = PurchaseOrder.objects.get(number=number)
    return redirect('create-build-po', slug=po.slug)


def createBuildPo(request, slug):
    #fetch that po
    try:
        purchaseOrder = PurchaseOrder.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('purchase-orders')

    #fetch all the products - related to this invoice
    jobs = Job.objects.filter(purchaseOrder=purchaseOrder)


    context = {}
    context['purchaseOrder'] = purchaseOrder
    context['jobs'] = jobs

    if request.method == 'GET':
        job_form  = JobForm()
        po_form = PurchaseOrderForm(instance=purchaseOrder)
        Vendor_form = VendorSelectForm(initial_vendor=purchaseOrder.vendor)
        context['job_form'] = job_form
        context['po_form'] = po_form
        context['Vendor_form'] = Vendor_form
        return render(request, 'invoice/create-po.html', context)

    if request.method == 'POST':
        job_form  = JobForm(request.POST)
        po_form = PurchaseOrderForm(request.POST, instance=purchaseOrder)
        Vendor_form = VendorSelectForm(request.POST, initial_vendor=purchaseOrder.vendor, instance=purchaseOrder)

        if job_form.is_valid():
            obj = job_form.save(commit=False)
            obj.purchaseOrder = purchaseOrder
            obj.save()

            messages.success(request, "PO and Job added succesfully")
            return redirect('create-build-po', slug=slug)
        elif po_form.is_valid and 'paymentTerms' in request.POST:
            po_form.save()

            messages.success(request, "PO updated succesfully")
            return redirect('create-build-po', slug=slug)
        elif Vendor_form.is_valid() and 'vendor' in request.POST:

            Vendor_form.save()
            messages.success(request, "Client added to invoice succesfully")
            return redirect('create-build-po', slug=slug)
        else:
            context['job_form'] = job_form
            context['po_form'] = po_form
            context['Vendor_form'] = Vendor_form
            messages.error(request,"Problem processing your request")
            return render(request, 'invoice/create-po.html', context)


    return render(request, 'invoice/create-po.html', context)

def viewDocumentPO(request, slug):
    #fetch that invoice
    try:
        purchaseOrder = PurchaseOrder.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('purchase-orders')

    #fetch all the products - related to this invoice
    jobs = Job.objects.filter(purchaseOrder=purchaseOrder)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')

    #Calculate the Invoice Total
    poCurrency = ''
    poTotal = 0.0
    if len(jobs) > 0:
        for x in jobs:
            y = float(x.quantity) * float(x.rate)
            poTotal += y
            poCurrency = x.currency

    context = {}
    context['purchaseOrder'] = purchaseOrder
    context['jobs'] = jobs
    context['p_settings'] = p_settings
    context['poTotal'] = "{:.2f}".format(poTotal)
    context['poCurrency'] = poCurrency

    return render(request, 'invoice/po-view.html', context)

def viewPDFPO(request, slug):
    #fetch that PO
    try:
        purchaseOrder = PurchaseOrder.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('purchase-orders')

    #fetch all the products - related to this invoice
    jobs = Job.objects.filter(purchaseOrder=purchaseOrder)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')

    #Calculate the Invoice Total
    poCurrency = ''
    poTotal = 0.0
    if len(jobs) > 0:
        for x in jobs:
            y = float(x.quantity) * float(x.rate)
            poTotal += y
            poCurrency = x.currency

    context = {}
    context['purchaseOrder'] = purchaseOrder
    context['jobs'] = jobs
    context['p_settings'] = p_settings
    context['poTotal'] = "{:.2f}".format(poTotal)
    context['poCurrency'] = poCurrency

    html_string = render_to_string(
        'invoice/po-pdf.html',context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=problem_list.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response

# ###--------------------------- Create Quote Views Start here --------------------------------------------- ###

@login_required
def createQuote(request):
    #create a blank invoice ....
    number = 'Quote-'+str(uuid4()).split('-')[1]
    newQuote = Quotation.objects.create(number=number)
    newQuote.save()

    quote = Quotation.objects.get(number=number)
    return redirect('create-build-quote', slug=quote.slug)

def createBuildQuote(request, slug):
    #fetch that Quote
    try:
        quote = Quotation.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('quotes')

    # #fetch all the requests- related to this quote
    requests = Request.objects.filter(quote=quote)


    context = {}
    context['quote'] = quote
    context['requests'] = requests

    if request.method == 'GET':
        request_form  = RequestForm()
        quote_form = QuoteForm(instance=quote)
        client_form = ClientSelectForm(initial_client=quote.client)
        context['request_form'] = request_form
        context['quote_form'] = quote_form
        context['client_form'] = client_form
        return render(request, 'invoice/create-quote.html', context)

    if request.method == 'POST':
        request_form  = RequestForm(request.POST)
        quote_form = QuoteForm(request.POST, instance=quote)
        client_form = ClientSelectForm(request.POST, initial_client=quote.client, instance=quote)

        if request_form.is_valid():
            obj = request_form.save(commit=False)
            obj.quote = quote
            obj.save()

            messages.success(request, "Quote added succesfully")
            return redirect('create-build-quote', slug=slug)
        elif quote_form.is_valid and 'paymentTerms' in request.POST:
            quote_form.save()

            messages.success(request, "Quote updated succesfully")
            return redirect('create-build-quote', slug=slug)
        elif client_form.is_valid() and 'client' in request.POST:

            client_form.save()
            messages.success(request, "Client added to quote succesfully")
            return redirect('create-build-quote', slug=slug)
        else:
            context['request_form'] = request_form
            context['quote_form'] = quote_form
            context['client_form'] = client_form
            messages.error(request,"Problem processing your request")
            return render(request, 'invoice/create-quote.html', context)


    return render(request, 'invoice/create-quote.html', context)


def viewPDFQuote(request, slug):
    #fetch that Quote
    try:
        quote = Quotation.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('quotes')

    #fetch all the products - related to this invoice
    requests = Request.objects.filter(quote=quote)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')

    #Calculate the Invoice Total
    quoteCurrency = ''
    quoteTotal = 0.0
    if len(requests) > 0:
        for x in requests:
            y = float(x.quantity) * float(x.price)
            quoteTotal += y
            quoteCurrency = x.currency

    context = {}
    context['quote'] = quote
    context['requests'] = requests
    context['p_settings'] = p_settings
    context['quoteTotal'] = "{:.2f}".format(quoteTotal)
    context['quoteCurrency'] = quoteCurrency

    return render(request, 'invoice/quote-view.html', context)


def viewDocumentQuote(request, slug):
     #fetch that Quote
    try:
        quote = Quotation.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('quotes')

    #fetch all the products - related to this invoice
    requests = Request.objects.filter(quote=quote)

    #Get Client Settings
    p_settings = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')

    #Calculate the Invoice Total
    
    quoteTotal = 0.0
    if len(requests) > 0:
        for x in requests:
            y = float(x.quantity) * float(x.price)
            quoteTotal += y
           

    context = {}
    context['quote'] = quote
    context['requests'] = requests
    context['p_settings'] = p_settings
    context['quoteTotal'] = "{:.2f}".format(quoteTotal)


    html_string = render_to_string(
        'invoice/pdf-quote-template.html',context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=problem_list.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
    

   

@login_required
def deleteInvoice(request, slug):
    try:
        Invoice.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    return redirect('invoices')

@login_required
def deleteQuote(request, slug):
    try:
        Quotation.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('quotes')

    return redirect('quotes')

@login_required
def deleteClient(request, slug):
    try:
        Client.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('clients')

    return redirect('clients')

@login_required
def deleteVendor(request, slug):
    try:
        Vendor.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('vendors')

    return redirect('vendors')

@login_required
def deleteOrder(request, slug):
    try:
        Order.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('orders')

    return redirect('orders')


@login_required
def deleteJob(request, slug):
    try:
        Job.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('jobs')

    return redirect('jobs')

@login_required
def deleteRequest(request, slug):
    try:
        Request.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('requests')

    return redirect('requests')

@login_required
def deleteProject(request, slug):
    try:
        Project.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('projects')

    return redirect('projects')

@login_required
def updateClient(request, slug):
    context = {}
    client = Client.objects.get(slug=slug)
    context['client'] = client
    form = ClientForm(request.POST or None, instance=client)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Client updated')
        return redirect('clients')
    else:
        messages.error(request, 'Problem processing your request')
        return render(request, 'projects/updateClient.html', context)
        
    

# @login_required  
# def updateProject(request, slug):
#     context = {}
#     project = Project.objects.get(slug=slug)
#     context['project'] = project
#     form = ProjectForm(request.POST or None, instance=project)
#     client_form = ClientSelectForm(request.POST or None, initial_client=project.client, instance=project)
   
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Project updated')
#         return redirect('projects')
#     elif client_form.is_valid() and 'client' in request.POST:
#             client_form.save()
#             messages.success(request, "Client updated for the project")
#             return redirect('projects')
#     else:
#         messages.error(request, 'Problem processing your request')

#     return render(request, 'projects/updateProject.html', context)

@login_required
def updateProject(request, slug):
    context = {}
    project = Project.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        client_form = ClientSelectForm(request.POST, initial_client=project.client)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated')
            return redirect('projects')
        elif client_form.is_valid() and 'client' in request.POST:
            client_form.save()
            messages.success(request, "Client updated for the project")
            return redirect('projects')
        else:
            messages.error(request, 'Problem processing your request')
    else:
        form = ProjectForm(instance=project)
        client_form = ClientSelectForm(initial_client=project.client)
    
    context.update({
        'form': form,
        'client_form': client_form,
        'project': project,
    })
    
    return render(request, 'projects/updateProject.html', context)
    
@login_required
def updateOrder(request, slug):
    context = {}
    order = Order.objects.get(slug=slug)
    context['order'] = order
    form = OrderForm(request.POST or None, instance=order)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Order updated')
        return redirect('orders')
    else:
        messages.error(request, 'Problem processing your request')
        return render(request, 'invoice/updateOrder.html', context)

@login_required
def updateRequest(request, slug):
    context = {}
    requests = Request.objects.get(slug=slug)
    context['requests'] = requests
    form = RequestForm(request.POST or None, instance=requests)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Request updated')
        return redirect('requests')
    else:
        messages.error(request, 'Problem processing your request')
        return render(request, 'invoice/updateRequest.html', context)


@login_required
def updateJob(request, slug):
    context = {}
    job = Job.objects.get(slug=slug)
    context['job'] = job
    form = JobForm(request.POST or None, instance=job)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Job updated')
        return redirect('jobs')
    else:
        messages.error(request, 'Problem processing your request')
        return render(request, 'invoice/updateJob.html', context)

@login_required
def updateVendor(request, slug):
    context = {}
    vendor = Vendor.objects.get(slug=slug)
    context['vendor'] = vendor
    form = VendorForm(request.POST or None, instance=vendor)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Vendor updated')
        return redirect('vendors')
    else:
        messages.error(request, 'Problem processing your request')
        return render(request, 'projects/updateVendor.html', context)

@login_required
def deletePo(request, slug):
    try:
        PurchaseOrder.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('purchase-orders')

    return redirect('purchase-orders')   

@login_required   
def rating(request):
    context = {}
    ratings = Rating.objects.all()    
    context['ratings'] = ratings

    if request.method == 'GET':
        form = RatingForm()
        context['form'] = form
        return render(request, 'projects/rating.html', context)
    return render(request, 'projects/rating.html', context)

@login_required
def addRating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = RatingForm()
            context = {
                'created': created,
                'form': form,
            }
            messages.success(request, 'New Rating Added')
            return redirect('rating')
        else:
            messages.error(request, 'Problem processing your request')
            return render(request, 'projects/addRating.html', context)
    else:
        form = RatingForm()
        context = {
            'form': form,
        }
        return render(request,'projects/addRating.html', context)

@login_required
def companySettings(request):
    company = Settings.objects.get(clientName='Ethiostar Translation and Localization PLC')
    context = {'company': company}
    return render(request, 'invoice/company-settings.html', context)







