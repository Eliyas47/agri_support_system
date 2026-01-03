from django.shortcuts import render, redirect
from .models import CropProblem
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    problems = CropProblem.objects.all()
    return render(request, 'dashboard.html', {'problems': problems})

@login_required
def post_problem(request):
    if request.method == 'POST':
        CropProblem.objects.create(
            farmer=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('dashboard')
    return render(request, 'post_problem.html')
