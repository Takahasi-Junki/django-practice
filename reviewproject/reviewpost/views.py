from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import ReviewModels
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupview(request):
  print('Sign UP view')
  if request.method == 'POST':
    username_data = request.POST['username_data']
    email_data = request.POST['email_data']
    password_data = request.POST['password_data']

    print('POST DESU')
    print('username_data : '+username_data)
    print('email_data : '+email_data)
    print('password_data : '+password_data)

    try:
      user = User.objects.create_user(username_data, email_data, password_data)
    except:
      return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
  else:
    print(User.objects.all())
  return render(request, 'signup.html',{})


def loginview(request):
  if request.method == 'POST':
    username_data = request.POST['username_data']
    email_data = request.POST['email_data']
    password_data = request.POST['password_data']
    user = authenticate(request, username = username_data, email = email_data, password = password_data)
    if user is not None:
      login(request, user)
      return redirect('list')

    else:
      return redirect('login')      

  return render(request, 'login.html')

def sampleview(request):
  if request.method == 'POST':
    return redirect('login')
  else:
    return render(request, 'login.html', {})


@login_required
def listview(request):
  object_list = ReviewModels.objects.all()
  return render(request, 'list.html', { 'object_list':object_list })


def detailview(request, pk):
  object = ReviewModel.object.get(pk=pk)
  return render(request, 'detail.html', {'object':object}) 


class CreateClass(CreateView):
  template_name ='create.html'
  model = ReviewModels
  fields = ('title', 'content', 'auteor', 'images', 'evaluation')
  success_url=reverse_lazy('list')

def logoutview(request):
  logout(request)
  return redirect('login')

def evaluationview(request, pk):
  post = ReviewModel.objects.get(pk=pk)
  author_name = request.user.get_username() + str(request.user.id)
  if author_name in post.useful_review_record:
    return redirect('list')
  else:
    post.useful_review = post.useful_review + 1
    post.useful_review = post.useful_review_record +author_name
    post.save()
    return render('list')