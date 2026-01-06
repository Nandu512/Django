from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import string, random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ShortURL
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@login_required 
def add_url(request):
    if ShortURL.objects.filter(user=request.user).count() >= 5:
        messages.error(request, "You can only add 5 URLs")
        return redirect('list_urls')

    if request.method == "POST":
        title = request.POST['title']
        original_url = request.POST['original_url']

        short_code = generate_short_code()

        ShortURL.objects.create(
            user=request.user,
            title=title,
            original_url=original_url,
            short_code=short_code
        )
        return redirect('list_urls')

    return render(request, 'add_url.html')


@login_required
def list_urls(request):
    query = request.GET.get('q')

    urls = ShortURL.objects.filter(user=request.user).order_by('-created_at')

    if query:
        urls = urls.filter(
            title__icontains=query
        ) | urls.filter(
            original_url__icontains=query
        )

    paginator = Paginator(urls, 3)  # 3 URLs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list_urls.html', {'page_obj': page_obj})



def redirect_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    return HttpResponseRedirect(url.original_url)
@login_required
def edit_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)

    if request.method == "POST":
        url.title = request.POST['title']
        url.original_url = request.POST['original_url']
        url.save()
        return redirect('list_urls')

    return render(request, 'edit_url.html', {'url': url})
@login_required
def delete_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)
    url.delete()
    return redirect('list_urls') 






