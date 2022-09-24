from django.shortcuts import render
from .models import Gallery
from django.core.paginator import Paginator

def gallery(request):
    gallery = Gallery.objects.all().order_by('-upload_date')
    paginator = Paginator(gallery, 7)
    page_number = request.GET.get('page')
    gallery_obj = paginator.get_page(page_number)
    return render(request, 'gallery.html', {'gallery_obj': gallery_obj})