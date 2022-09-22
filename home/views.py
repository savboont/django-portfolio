from django.shortcuts import render
from .models import User, Project, Skill, CompletedCourse, UncompletedCourse

# Create your views here.


def home(request):
	skills = Skill.objects.order_by('-grade')
	comp_courses = CompletedCourse.objects.all()
	uncomp_courses = UncompletedCourse.objects.all()
	context = {
		'skills': skills,
		'comp_courses': comp_courses,
		'uncomp_courses': uncomp_courses,
	}
	return render(request, 'home/home.html', context=context)


def projects(request):
	proj = Project.objects.all()
	context = {
		'proj': proj,
	}
	return render(request, 'home/projects.html', context=context)


def contact(request):
	contacts = User.objects.get(name='Alexey', surname='Matveev')
	return render(request, 'home/contact.html', context={
		'contacts': contacts
	})

