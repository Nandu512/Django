from django.shortcuts import render
def greeting(request):
    if request.GET:
        email = request.GET.get('email')
        return render(request,'form-data.html',{
            'formData':request.GET,
            'email': email
        })
    return render(request,'index.html' )