from django.shortcuts import render, HttpResponse, redirect
from .models import TeacherProfile, Student
from django.contrib import auth
from .forms import TeacherForm, StudentForm, UserForm
# Create your views here.

def dashboard(request):
	id = request.user.id
	try:
		data = TeacherProfile.objects.get(id=id)
	
	except TeacherProfile.DoesNotExist:
		data = TeacherProfile(name = request.user.username)

	print(data.approval_status)

	if data.approval_status != 'APPROVED':
		print('NotApproved')
		return render(request, 'dashboard.html', {'name' : request.user.username, 'approval_status' : 'NotApproved'})

	elif request.user.is_authenticated:
		print('Approved')
		return render(request, 'dashboard.html', {'name' : request.user.username, 'approval_status' : 'Approved'})
	
	return redirect('login')

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('/dashboard')
	return render(request, 'login.html')


def updateTeacher(request):
	id = request.user.id
	try:
		data = TeacherProfile.objects.get(id=id)
	
	except TeacherProfile.DoesNotExist:
		data = TeacherProfile(name = request.user.username)

	

	form = TeacherForm(request.POST or None , instance=data)
	if request.user.is_authenticated:
		TeacherProfile.objects.get_or_create(user=request.user) #data.user.add(request.user)
	else:
		redirect('/dashboard')
	print(form.errors)
	if form.is_valid():
		form.save()
		

		return redirect('/dashboard')

	return render(request, 'edit.html', {'student':data})

def auth_view(request):
   
    username = request.POST.get('username', False) #['username']
    password = request.POST.get('password', False) #['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        
        return redirect('/dashboard')
    else:
        return HttpResponse('Invalid username and password')   

def addstudent(request):
	if request.method=="POST":
		form = StudentForm(request.POST,request.FILES)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('/dashboard')
	else:
		form = StudentForm()
	return render(request, 'student.html', {'form':form})

def showstudent(request):
	data = Student.objects.all()
	return render(request, 'show.html', {'students':data})

def deletestudent(request,id):
	d = Student.objects.get(id=id)
	d.delete()	
	return redirect('/show')

def updatestudent(request,id):
	data = Student.objects.get(id=id)
	form = StudentForm(request.POST, instance=data)
	if form.is_valid():
		form.save()
		return redirect('/dashboard')
	return render(request, 'edit.html', {'student':data})

def registration(request):
	if request.method=="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Registration Success")		
	else:		
		form = UserForm()
	return render (request,"login1.html")
