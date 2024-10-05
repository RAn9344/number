from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from wel.forms import SignUpForm
from django.http import HttpResponseRedirect
def insert(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/login.html',{'f':form})
def delete(request,id):
	e=User.objects.get(id=id)
	e.delete()
	return redirect('/result')
def update(request,id):
	user=User.objects.get(id=id)
	if request.method=="POST":
		form=SignUpForm(request.POST,instance=user)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'m':user})
def index(request):
	return render(request,'apps/index.html')
@login_required
def home(request):
	return render(request,'apps/home.html')
def service(request):
	return render(request,'apps/service.html')
def gallery(request):
	return render(request,'apps/gallery.html')
def contact(request):
	return render(request,'apps/contact.html')
def logout(request):
	return render(request,'apps/logout.html')
def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'apps/signup.html',{'s':form})