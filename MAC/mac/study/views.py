from django.shortcuts import render
from .models import studyresource

# Create your views here.
def study_resource_list(request):
    allPosts= studyresource.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'study_resource_list.html', context)