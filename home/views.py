from email.mime import image
from django.shortcuts import render, redirect
from home.models import Image
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage

# function to render index page
def index(request):
    images = Image.objects.all()
    if request.method == "POST":
        if "searchName" in request.POST:
            # search by image name
            search = request.POST.get('search')
            image_object = Image.objects.filter(name=search)
            if image_object.exists():
                images = image_object
        elif "addImage" in request.POST:
            # a post request to submit the form and add it to add it to database
            name = request.POST.get('name')
            url = request.POST.get('url')
            detail = request.POST.get('detail')
            image = Image(name=name,url=url,detail=detail)
            image.save()
            messages.success(request, 'Image details added successfully.')
    # adding pagination 9 images per page
    p = Paginator(images,9)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
        
    context = {
        'images' : page,
    }
    return render(request,'index.html',context)


# function to render add new image page
def new(request):   
    return render(request,'new.html')

# function to render add edit image page
def edit(request,id):
    if request.method == "POST":
        # a post request to edit the image details by id
        image_object = Image.objects.get(id=id)
        image_object.url = request.POST.get('url')
        image_object.detail = request.POST.get('detail')
        image_object.save()
        return redirect("home")
    image_obj = Image.objects.get(id=id)
    context = {
        'image' : image_obj
    }
    return render(request,'edit.html',context)

# function to render view image page by id
def show(request, id):
    image_object = Image.objects.get(id=id)
    context = {
        'image' : image_object
    }
    return render(request,'view.html',context)


# function to delete a image from gallery
def delete(request, id):
    image_object = Image.objects.filter(id=id).delete()
    return redirect("home")
    