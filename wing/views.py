from django.shortcuts import render, get_object_or_404
from .models import Wing, Course
from django.core.paginator import Paginator

def winglist(request):
    wings = Wing.objects.all()
    return render(request, 'wing/wing_list.html', {'wings': wings})


def wing_detail(request, id, slug):
    # matching_courses = Course.objects.filter(wing__slug)
    wing = get_object_or_404(Wing, id=id, slug=slug)
    matching_courses = Course.objects.filter(wing_id__id=id)
    paginator = Paginator(matching_courses, 2)
    page_number = request.GET.get('page')
    courses_obj = paginator.get_page(page_number)
    return render(request, 'wing/wing_detail.html', {'courses': courses_obj, 'wing':wing,})
