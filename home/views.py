from multiprocessing import context

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# This is a simple view that returns a HttpResponse with a message indicating that the Django server is running successfully.
def home(request):
    
    peoples = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 16},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 28},
        {"name": "Eve", "age": 17.9},
    ]
    
    vegetables = ["tomato", "Tomato" ,"patatpo", "carrot", "onion", "potato", "cucumber", "lettuce", "spinach", "broccoli"]
    
    text = "ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    # return HttpResponse("<h1>Hey i am a Django server and i am running successfully</h1>")   
    
    # Alternatively, you can render a template instead of returning a simple HttpResponse.
    # context is a dictionary that contains the data you want to pass to the template. In this case, we are passing a list of people with their names
    # and ages.
    ctx = {'page':'home'}
    return render(request, 'home/index.html', context={'peoples': peoples, 'text': text , 'vegetables': vegetables , context: ctx})

def about(request):
    context = { 'page': 'about'}
    return render(request, 'home/about.html' , context=context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, 'home/contact.html' , context=context)