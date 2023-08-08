from django.shortcuts import render, redirect
from .forms import AvatarForm
from .models import Avatar


def homepage(req):
    avatars = Avatar.objects.all()
    arr_lenght = len(avatars)
    index = arr_lenght - 1
    
    avatar = avatars[index]
    return render(req, 'app/app.html', {
        'avatar': avatar
    })
    

def avatar_upload(request):
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("../")
    
    form = AvatarForm()
    
    avatars = Avatar.objects.all()
    arr_lenght = len(avatars)
    index = arr_lenght - 1
    
    avatar = avatars[index]
    
    return render(request, "app/avatar_form.html", {
        'form': form,
        'avatar': avatar
        })