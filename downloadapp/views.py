import email
from django.conf import settings
from django.forms import forms
from django.shortcuts import render ,  get_object_or_404
from django.template import context
from django.contrib import messages
from django.test import client
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from cmsapp.models import Category
from downloadapp.models import File, Subject
from .forms import ClientForm
from .models import Client 
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
import os
from django.db.models import Count

# Create your views here.

def download(request):
    categorys = Category.objects.all()
    subjects = Subject.objects.filter(approved=True)
    files = File.objects.filter(approved=True)
    client = Client.objects.all()
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(subjects,num_of_items)
    topfile = File.objects.all().annotate(num_file = Count('client')).order_by('-num_file')[:5]

    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        subjects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        subjects = paginator.page(page)

    context = {'categorys' : categorys , 'subjects' : subjects , 'files' : files , 'client' : client , 'paginator' : paginator , 'topfile' : topfile} 
    return render(request,'download/download.html' , context)


def client_add(request , pk):
    file = get_object_or_404(File,pk=pk)
    categorys = Category.objects.all()
    intaial_data = {
        'file' : file
    }

    form = ClientForm(initial= intaial_data)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES , )
        if form.is_valid():
            client = form.save(commit=False)
            client.file = file
            client.save()
            messages.success(request, 'Save success')
            
            title = 'ดาวน์โหลดไฟล์'+file.name 
            body = file.name + '''
                <h3>ขอบคุณความสนใจสำหรับดาวน์โหลดไฟล์ เพื่อประโยชน์แก่ผู้เรียน (โรงเรียนลำปลายมาศพัฒนา)</h3>
                 <p>สนใจงานอบรม ติดต่อ
                    นางสาวพรรณทิพย์พา  ทองมี (ครูต๋อย)
                    โรงเรียนลำปลายมาศพัฒนา
                    162 หมู่ 13  ต.โคกกลาง อ.ลำปลายมาศ
                    จ.บุรีรัมย์ 31130  โทร.080-4748288  
I                   D Line 0804748288  </p>
            '''
            email = EmailMessage(subject=title , body=body , from_email='weblpmp@lpmp.org' , to=[client.email])
            email.content_subtype = 'html'
            email.send()
            return HttpResponseRedirect(reverse('client_add' , args=(file.pk,)))
        messages.error(request, 'Save failed')
    context = {'form' : form , 'file' : file , 'categorys' : categorys }
    return render(request ,'download/add.html' , context)

def download_list(request , pk):
    subject = get_object_or_404(Subject,pk=pk)
    categorys = Category.objects.all()
    context = {'subject' : subject , 'categorys' : categorys }
    return render(request,'download/download_list.html' ,context)

from django.core.mail import EmailMessage


    