from django.shortcuts import render, redirect
from .models import ContactSubmission, Certificate

def index(request):
    if request.method == 'POST':
        ContactSubmission.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        return redirect('home')

    context = {
        'name': 'Raphid',
        'title': 'Full-Stack Developer',
        'about': 'I build modern, scalable web applications with clean code and great user experiences.',
        'skills': [
            {'name': 'Python/Django', 'level': 90},
            {'name': 'JavaScript', 'level': 85},
            {'name': 'React', 'level': 80},
            {'name': 'HTML/CSS', 'level': 90},
            {'name': 'PostgreSQL', 'level': 75},
            {'name': 'Docker', 'level': 70},
        ],
        'projects': [
            {'title': 'Project Alpha', 'desc': 'A full-stack web application', 'tech': 'Django + React'},
            {'title': 'Project Beta', 'desc': 'REST API platform', 'tech': 'Django REST Framework'},
            {'title': 'Project Gamma', 'desc': 'Real-time dashboard', 'tech': 'React + WebSockets'},
        ],
        'certificates': Certificate.objects.all(),
        'socials': {
            'github': 'https://github.com/raphid',
            'linkedin': 'https://linkedin.com/in/raphid',
            'twitter': 'https://twitter.com/raphid',
        },
    }
    return render(request, 'home/index.html', context)
