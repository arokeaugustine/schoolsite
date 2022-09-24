from django.shortcuts import render, get_object_or_404
from .models import Wing, Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def winglist(request):
    wings = Wing.objects.all()
    return render(request, 'wing_list.html', {'wings': wings})


@login_required
def wing_detail(request, id, slug):
    # matching_courses = Course.objects.filter(wing__slug)
    wing = get_object_or_404(Wing, id=id, slug=slug)
    matching_courses = Course.objects.filter(wing_id__id=id)
    paginator = Paginator(matching_courses, 2)
    page_number = request.GET.get('page')
    courses_obj = paginator.get_page(page_number)
    return render(request, 'wing_detail.html', {'courses': courses_obj, 'wing':wing,})


# search needs to be refactored so that it will work with get request and not post
#  search view for courses

@login_required
def search_courses(request):
    # checking the type of request
    if request.method=='GET':
        # passing the seach input to our variable
        search = request.GET['search']
        # query database by search input
        courses = Course.objects.filter(title__contains=search)

        paginator =Paginator(courses, 5)

        page_number = request.GET.get('page')
        courses_obj = paginator.get_page(page_number)
        return render(request, 'search_courses.html', {'courses':courses_obj, 'search': search})
    else:
        return render(request, 'search_courses.html')