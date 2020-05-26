from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from core.models import Document
from core.forms import DocumentForm

import cv2

from core.doti import hello



def home_2(request):

    documents = Document.objects.all()
    path = r'C:\Users\porsc\Desktop\orange-painting.jpg'
    image = cv2.imread(path)
    name = "asdasdsd"
    testt = "hello.test()"
    x = {
     'document' : documents,
     'image' : image,
     'testt' : testt,
     'name':name
    }
    return render(request, 'core/home.html', { 'x': x })

def home(request):
    Brain_Per_All = "0"
    Hole_Pre_Brain = "0"
    ans = "-"
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        ans,Brain_Per_All,Hole_Pre_Brain = hello.run(uploaded_file_url)
        #f = open('C:/Users/porsc/cs402_test/hello/TEST.txt', 'a')
        #xxxx  = "name = "+str(uploaded_file_url)+" || Brain_Per_All = "+str(Brain_Per_All)+" || Hole_Pre_Brain = "+str(Hole_Pre_Brain)+" || ans = "+str(ans)+"\n"
        #xxxx  ="["+filename+","+str(Brain_Per_All)+","+str(Hole_Pre_Brain)+"] ,"+"\n"
        #xxxx  =filename+"	"+str(Brain_Per_All)+"	"+str(Hole_Pre_Brain)+"	"+str(ans)+"\n"
        Brain_Per_All = round(Brain_Per_All , 2)
        Hole_Pre_Brain  = round(Hole_Pre_Brain , 2)
        #f.write(xxxx)
        #f.close()

        x ={
        'uploaded_file_url' : uploaded_file_url ,
        'Brain_Per_All':Brain_Per_All,
        'ans' : ans ,
        'Hole_Pre_Brain':Hole_Pre_Brain,
        }
        return render(request, 'core/index.html', { 'x': x })
    else:
        name = "ERROR"

    x = {
    'Brain_Per_All':Brain_Per_All,
    'ans' : ans ,
    'Hole_Pre_Brain':Hole_Pre_Brain,
    }
    return render(request, 'core/index.html', { 'x': x })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
