from django.shortcuts import render
from django.utils import timezone
from .models import Metrostation


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Metrostation.objects.all().order_by('name')
    print(posts)
    return render(request, 'PicketAdminApp/post_list.html',{'posts': posts})