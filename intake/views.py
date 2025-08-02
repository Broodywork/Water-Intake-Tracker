from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WaterIntake
from .forms import WaterIntakeForm
from datetime import date
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
def home(request):
    return render(request, 'home.html')

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful. Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
@login_required
def add_intake(request):
    today = date.today()
    if WaterIntake.objects.filter(user=request.user, date=today).exists():
        messages.error(request, "You already added today's intake.")
        return redirect('intake_list')

    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user
            intake.save()
            return redirect('intake_list')
    else:
        form = WaterIntakeForm()
    return render(request, 'add_intake.html', {'form': form})
@login_required
def intake_list(request):
    entries = WaterIntake.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(entries, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'intake_list.html', {'page_obj': page_obj})
@login_required
def edit_intake(request, id):
    intake = get_object_or_404(WaterIntake, id=id, user=request.user)
    form = WaterIntakeForm(request.POST or None, instance=intake)
    if form.is_valid():
        form.save()
        return redirect('intake_list')
    return render(request, 'edit_intake.html', {'form': form})

@login_required
def delete_intake(request, id):
    intake = get_object_or_404(WaterIntake, id=id, user=request.user)
    if request.method == 'POST':
        intake.delete()
        return redirect('intake_list')
    return render(request, 'delete_confirm.html', {'intake': intake})

@login_required
def compare_intake(request):
    result = None
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        try:
            intake1 = WaterIntake.objects.get(user=request.user, date=date1)
            intake2 = WaterIntake.objects.get(user=request.user, date=date2)
            result = abs(intake1.quantity_ml - intake2.quantity_ml)
        except:
            messages.error(request, "One or both dates not found.")
    return render(request, 'compare.html', {'result': result})
