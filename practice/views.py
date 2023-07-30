from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForms
from service.models import userFormsDemo
from news.models import newsModels


def HomePage(request):
    databasedata=userFormsDemo.objects.all().order_by('-email')
    data=[]
    for i in databasedata:
        data.append({i.fname+i.lname})
        data.append({i.email})
    return render(request,'index.html',{"name":data})

def about(request):
    datas=""
    try:
        if request.method=='GET':
            output=request.GET['data']
            datas=output
    except:
        pass
    return render(request,'about.html',{'newdata':datas})

def freelancer(request):
    obj=newsModels.objects.all()
    return render(request,'freelancer.html',{'news':obj})

def job(request):
    return render(request,'job.html')

def form(request):
    importedform=userForms()
    data=""
    try:
        if request.method=='POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            data=fname+lname
            url='/about/?data={}'.format(data)
            return redirect(url)
    except:
        pass
    return render(request,'form.html',{'fn':importedform,'name':data})

def userform(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    name=fname+lname
    return HttpResponse(name)


def newDemo(request,slug):
    objs=newsModels.objects.get(news_slug=slug)
    return render(request,'newdemo.html',{'obj':objs})

def filterData(request):
    objs=newsModels.objects.all()
    try:
        if request.method=="GET":
            queriess=request.GET['queriesss']
            objs=newsModels.objects.filter(news_desc__contains=queriess)
    except:
        pass    
    return render(request,'filters.html',{'objs':objs})

    



#  we can use HttpsResposeRedirect or django.shortcut redirect function both for  same work
# def form(request):
#     data=""
#     try:
#         if request.method=='POST':
#             fname=request.POST['fname']
#             lname=request.POST['lname']
#             data=fname+lname
#             url='/about/?data={}'.format(data)
#             return HttpResponseRedirect(url)
#     except:
#         pass
#     return render(request,'form.html',{'name':data})
    
