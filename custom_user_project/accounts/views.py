from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm


def registerView(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})