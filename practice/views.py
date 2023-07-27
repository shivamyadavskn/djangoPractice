from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect


def HomePage(request):
    return render(request,'index.html')

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
    return render(request,'freelancer.html')

def job(request):
    return render(request,'job.html')

def form(request):
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
    return render(request,'form.html',{'name':data})

def userform(request):
    name=request.POST['fname']
    return HttpResponse(name)

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
    
