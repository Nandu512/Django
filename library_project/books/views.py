from django.shortcuts import render
from .forms import LoginModelForm
def greeting(request):
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'form-data.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = LoginModelForm()
    return render(request,'index.html',{'form':form})

def aboutUs(request):
    return render(request,'about-us.html')
def page(request, title):
    return render(request,'page.html',{'title':title})
def count(request, num):
    return render(request,'count.html',{'num':num})