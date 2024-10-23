from django.shortcuts import render, redirect

from customers.forms import CustomerForm, CustomerRegisterForm


# Create your views here.
def index(request):
    form = CustomerForm()
    return render(request, 'index.html', {'form': form})
def about(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = CustomerRegisterForm()
    return render(request, 'about.html', {'form': form})
def gallery(request):
    return render(request, 'gallery.html')
def signup(request):
    return render(request, 'signup.html')
def contact(request):
    return render(request, 'contact.html')
