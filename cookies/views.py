from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
	return render(request,'cookies/index.html')
def setCookie(request):
    name=request.POST['t1']
    pas=request.POST['t2']
    response = HttpResponse("Cookie Set")
    response.set_cookie('n', name)
    return response
def getCookie(request):
    a  = request.COOKIES['n']
    return HttpResponse("value is "+  a);
def fileupload(request):
     if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'cookies/fileupload.html', {
            'uploaded_file_url': uploaded_file_url
        })
     return render(request, 'cookies/fileupload.html')
