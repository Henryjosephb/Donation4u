from django.shortcuts import render, redirect
from .forms import DonorForm

def home(request):
    return render(request, 'donations/home.html')


def donor_form_view(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # we'll create this next
    else:
        form = DonorForm()
    return render(request, 'donations/donor_form.html', {'form': form})
