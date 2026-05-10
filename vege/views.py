from django.shortcuts import render

# Create your views here.
def receipies(request):
    return render(request, 'receipies.html')