from django.shortcuts import render


# Home page

def home(request):
    return render(request, 'home.html')
  
# About page
def about(request):
    return render(request, 'about.html')  
   
# Projects page
def projects(request):
    return render(request, 'projects.html')
  
# Testimonials page
def testimonials(request):
    return render(request, 'testimonials.html')
  
  
# Hire
def hire(request):
    return render(request, 'hire.html')    