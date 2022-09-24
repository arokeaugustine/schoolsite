from django.shortcuts import render
from .models import Gallery
from django.core.paginator import Paginator

def gallery(request):
    gallery = Gallery.objects.all().order_by('-upload_date')
    paginator = Paginator(gallery, 3)
    page_number = request.GET.get('page')
    gallery_obj = paginator.get_page(page_number)
    # this next code is a hack for solving the pagination 
    nums = 'a' * gallery_obj.paginator.num_pages
    return render(request, 'gallery.html', {'gallery_obj': gallery_obj, 'nums':nums, })


