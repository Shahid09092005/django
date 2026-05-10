from django.shortcuts import render
from .models import Receipe


# Create your views here.
def receipies(request):
    if request.method == 'POST':
        data= request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        
        return render(request, 'receipies.html')
    return render(request, 'receipies.html') 