from django.shortcuts import render,redirect
from .models import Schedule,user_list
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse


# Create your views here

@login_required(login_url="/login/")
def schedule_list(request):
	schedules=Schedule.objects.filter(user_name=request.user).order_by('end_time')
	return render(request, 'schedule/schedule_list.html',{'schedules':schedules})

@login_required(login_url="/login")
def new_task_view(request):
	if request.method == 'POST':
		form=forms.newtask(request.POST,request.FILES)
		if form.is_valid():
			sample=user_list.objects.get(user_name=request.user)
			sample.task_index=sample.task_index+1
			sample.save()
			instance=form.save(commit=False)
			instance.user_name = request.user
			instance.task_id=sample.task_index
			instance.save()
			return redirect('schedule_list')
	else:
		form=forms.newtask()
		instance=user_list.objects.get_or_create(user_name=request.user)
		instance=user_list.objects.get(user_name=request.user)
		index=instance.task_index
	return render(request,'schedule/new_task.html',{'form':form , 'id':index})

@login_required(login_url="/login")
def delete_view(request):
	if request.method == 'POST':
		index= request.POST.get('data')
		print("index......", index)
		Schedule.objects.filter(task_id=int(index),user_name=request.user).delete()
		return HttpResponse('success')


@login_required(login_url="/login")
def detail_view(request):
	if request.method == "GET":
		return render(request,'schedule/schedule_detail.html')