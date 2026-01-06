from django.shortcuts import render, redirect
from .models import CropProblem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact

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
            image=request.FILES.get('image')
        )
        return redirect('dashboard')
    return render(request, 'post_problem.html')


@login_required
def problem_list(request):
    problems = CropProblem.objects.all()
    return render(request, 'problem_list.html', {'problems': problems})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Thanks — your message has been received.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    return render(request, 'contact.html')
