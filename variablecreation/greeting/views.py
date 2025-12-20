from django.shortcuts import render
def greetings(request):
    count=23
    return render(request,'index.html',{'count':count})
