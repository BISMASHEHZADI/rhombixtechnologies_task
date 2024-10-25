from django.shortcuts import render
from .forms import Commant_Form
from .models import Commant

# Create your views here.
def home(request):
    return render(request, 'front.html')

def Commant_view(request):
    if request.method == 'POST':
        form = Commant_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the comment
            sav = Commant.objects.create(email=email, comment=message)
        else:
            sav = None
    else:
        form = Commant_Form()
        sav = None
    
    return render(request, 'comment.html', {'form': form, 'fm': sav})
def project(request):
    return render(request, 'project.html')