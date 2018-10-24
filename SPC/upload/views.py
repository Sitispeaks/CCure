from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from upload.models import Document
from upload.forms import DocumentForm


def list(request):
    if request.user.is_authenticated:
        # Handle file upload
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                user_name = request.user.username
                path = request.POST.get('filepath','')
                newdoc = Document(_user = user_name,_file_path = path,_data = request.FILES['docfile'].file.read())
                newdoc.save()

                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('list'))
            
        else:
            form = DocumentForm() # A empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()


        # Render list page with the documents and the form
        return render(request, 'list.html', {'documents': documents, 'form': form})

    else:
        return HttpResponseRedirect("/")
