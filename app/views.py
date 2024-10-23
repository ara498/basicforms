from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def forms(request):
    return render(request,'forms.html')

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(Topic_name=tn)
        return HttpResponse(f'{tn} is created')

    return render (request,'insert_topic.html')   

def insert_webpage(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    if request.method=='POST':
        tn=request.POST['topic']
        TO=Topic.objects.get(Topic_name=tn)
        name=request.POST['n']
        url=request.POST['u']
        email=request.POST['e']
        wo=Webpage.objects.get_or_create(Topic_name=TO,name=name ,url=url,email=email)
        return HttpResponse('data is inserted')
    return render (request,'insert_webpage.html',d)    

def select_multiple(request):
    TO=Topic.objects.all()
    d={'TO':TO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        EQST=Webpage.objects.none()
        for i in MTN:
            EQST=EQST|Webpage.objects.filter(Topic_name=i)
        d1={'EQST':EQST}
        return render (request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)  

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    
    return render(request,'checkbox.html',d)          

