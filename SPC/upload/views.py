from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from upload.models import Foo
from upload.forms import DocumentForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            user_name = request.user.username
        
            newdoc1 = Foo(_user = user_name,_data = request.FILES['docfile'].file.read(), _path = request.FILES['docfile'].file.path)
            newdoc1.save()
# newdoc = Document(docfile = request.FILES['docfile'])
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Foo.objects.all()


    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': documents, 
        'form': form}
        )


