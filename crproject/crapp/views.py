from django.shortcuts import render,redirect
from .models import Kitchen,Bedroom,Hall,Handles,Doors

##################################################################
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):	
	if request.method == 'GET':
		return render(request, 'accounts/login.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('/home')
		else:
			context = {'error': 'Invalid username/password'}
			return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')

def validate_user(username, password1, password2):
	status = True
	message = ''
	user_existence = User.objects.filter(username=username).exists()
	if user_existence:
		status = False
		message = 'Username already exists'
	if password1 != password2:
		status = False
		message = 'Passwords not matching'
	return status, message


def register_view(request):
	if request.method == 'GET':
		return render(request, 'accounts/register.html')
	elif  request.method == 'POST':
		username = request.POST.get('username')
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email= request.POST.get('email')
		password1= request.POST.get('password1')
		password2= request.POST.get('password2')
		status, message = validate_user(username, password1, password2)
		if status:
			user = User.objects.create_user(username, email=email, password=password1)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			login(request, user)
			return redirect('/home')
		else:
			context = {'error': message}
			return render(request, 'accounts/register.html', context)


##################################################################
@login_required(login_url='/login')
def home_view(request):
	return render(request,'home.html')

def kitchendetails_view(request,id):
	kitchen_cost =Kitchen.objects.get(id=id)
	if request.method == "GET":
		context ={
		'kitchen_cost':kitchen_cost
		}
		return render(request,'k_details.html',context)
	elif request.method == "POST":
		kitchen_cost.length = request.POST.get('kit_length')
		kitchen_cost.width = request.POST.get('kit_width')
		kitchen_cost.cost = request.POST.get('kit_cost')
		kitchen_cost.save()
		return redirect('/k_details/1')


def bedroomdetails_view(request,id):
	wardrobe_cost =Bedroom.objects.get(id=id)
	if request.method == "GET":
		context ={
		'wardrobe_cost':wardrobe_cost
		}
		return render(request,'b_details.html',context)
	elif request.method == "POST":
		wardrobe_cost.length = request.POST.get('bed_length')
		wardrobe_cost.width = request.POST.get('bed_width')
		wardrobe_cost.cost = request.POST.get('bed_cost')
		wardrobe_cost.save()
		return redirect('/b_details/1')

def halldetails_view(request,id):
	hall_cost =Hall.objects.get(id=id)
	if request.method == "GET":
		context ={
		'hall_cost':hall_cost
		}
		return render(request,'h_details.html',context)
	elif request.method == "POST":
		hall_cost.length = request.POST.get('hall_length')
		hall_cost.width = request.POST.get('hall_width')
		hall_cost.cost = request.POST.get('hall_cost')
		hall_cost.save()
		return redirect('/h_details/1')
########################################

def doors_view(request):
	doors = Doors.objects.all()
	context ={'doors': doors}
	return render(request,'doors.html',context)

def edit_door_system(request,id):
    door_instance =Doors.objects.get(id=id)
    if request.method == 'GET':
        context = {'door_instance': door_instance}
        return render(request, 'edit_door_system.html', context)
    elif request.method == 'POST':
        door_instance.quantity = request.POST.get('dquantity')
        door_instance.totalprice = request.POST.get('dtotal')
        door_instance.save()
        return redirect('/doors')


def handle_view(request):
	handles = Handles.objects.all()
	context = {'handles': handles}
	return render(request,'handles.html',context)


def edit_system(request,id):
    handles_system = Handles.objects.get(id=id)
    if request.method == 'GET':
        context = {'handles_system': handles_system}
        return render(request, 'edit_system.html', context)
    elif request.method == 'POST':
        handles_system.quantity = request.POST.get('handle_quantity')
        handles_system.totalprice = request.POST.get('handle_total')
        handles_system.save()
        return redirect('/handles')
####################################################

def cart_view(request,id):
	handles = Handles.objects.get(id=id)
	doors =Doors.objects.get(id=id)
	kitchen_obj = Kitchen.objects.get(id=id)
	wardrobe_obj =Bedroom.objects.get(id=id)
	hall_obj =Hall.objects.get(id=id)

	context ={
		'handles':handles,
		'doors':doors,
		'kitchen_obj':kitchen_obj,
		'wardrobe_obj':wardrobe_obj,
		'hall_obj':hall_obj
	}
	return render(request,'cart.html', context)
######################################################







