
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Skill
from .models import Hobby
from .models import Responsibility
from .models import Experience
from .forms import PostForm
from .forms import SkillForm
from .forms import HobbyForm
from .forms import ExperienceForm
from .forms import ResponsibilityForm
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext



def cv(request):
    skills = Skill.objects.all()
    experience=Experience.objects.all()
    hobbies=Hobby.objects.all()
    responsibilities=Responsibility.objects.all()
    return render(request, 'blog/cv.html', {'skills': skills,'experience': experience,'hobbies': hobbies,'responsibilities': responsibilities})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def skill_new(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.author = request.user
            skill.save()
            return redirect('cv')
    else:
        form = SkillForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def hobby_new(request):
    if request.method == "POST":
        form = HobbyForm(request.POST)
        if form.is_valid():
            hobby = form.save(commit=False)
            hobby.save()
            return redirect('cv')
    else:
        form = HobbyForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def experience_new(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv')
    else:
        form = ExperienceForm()
    return render(request, 'blog/post_edit.html', {'form': form})    
def responsibility_new(request):
    if request.method == "POST":
        form = ResponsibilityForm(request.POST)
        if form.is_valid():
            responsibility = form.save(commit=False)
            responsibility.save()
            return redirect('cv')
    else:
        form = ResponsibilityForm()
    return render(request, 'blog/post_edit.html', {'form': form})    


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
