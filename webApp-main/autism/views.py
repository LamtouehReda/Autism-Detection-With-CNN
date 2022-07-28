from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


#function to handle an uploaded file.
from .cnn import cnn

def index(request):
    if request.method == 'POST' and  'cnnBtn' in request.POST:
        upload1 = request.FILES['upload1']
        fss = FileSystemStorage()
        file = fss.save(upload1.name, upload1)
        file_url = fss.url(file)
        img_path='.'+file_url
        classe = cnn(img_path)
        context={'classe': classe,'file_url':file_url}
        return render(request, 'autism/upload.html', context)
    return render(request, 'autism/upload.html')