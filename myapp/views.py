from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def img_upld(request):
    return render(request,'img_upld.html')
def img_disp(request):
    file_url=False
    if request.method=='POST' and request.FILES:
        image= request.FILES['sam']
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url= fs.url(file)
    return render(request,'img_display.html',context={'file_url':file_url})