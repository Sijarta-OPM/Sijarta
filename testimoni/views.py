from django.shortcuts import render

# Create your views here.

def testimoni(request):
    return render(request, 'testimoni_form.html')