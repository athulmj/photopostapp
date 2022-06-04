from django.shortcuts import redirect, render
from photouploader.forms import UserImageForm



def request_image(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            return render(request, 'display_photo.html', {'form':form,'img_obj':img_object})
    else:
        form = UserImageForm()
    return render(request,'display_photo.html', {'form': form})


