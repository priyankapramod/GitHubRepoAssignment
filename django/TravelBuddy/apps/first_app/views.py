from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect# the index function is called when root is visited
from .models import User,Trip,Destination
from .forms import UserCreateForm, LoginForm, TripPlanner, DestinationForm



def welcome(req):
    context = {
        "form1" : UserCreateForm(),
        "form2" : LoginForm()
    }
    return render(req,'first_app/welcome.html', context)



def register(req):
    bound_form1 = UserCreateForm(req.POST)

    if bound_form1.is_valid():
        print('in if')
        print(bound_form1)
        bound_form1.save()
        return HttpResponse("Yay, we are good")

    context = {
        "form1" : bound_form1,
    }
    return render(req,'first_app/welcome.html', context)




def login(req):
    login_form = LoginForm(req.POST)
    if login_form.is_valid():
        email_of_user_logged_in = login_form.cleaned_data.get('email')
    users = User.objects.get(email = email_of_user_logged_in)
    req.session['user_logged_in'] = users.name


    context = {
                'trip_form' : TripPlanner(),
                'dest_form' : DestinationForm()
            }
    return render(req,'first_app/add_plan.html', context)




def add_plan(request):


        trip_form = TripPlanner(request.POST)
        dest_form = DestinationForm(request.POST)

        users = User.objects.get(name = request.session['user_logged_in'])


        if dest_form.is_valid():
            dest_model = dest_form.save()

        print(dest_model.id, "dest id")
        print(dest_model.destination_name, "dest name")

        my_dest = Destination.objects.get(destination_name = dest_model.destination_name)
        print(my_dest)

        if trip_form.is_valid():
            obj = trip_form.save()
            print("hello")
            # obj.user_trip.add(users)
            print(my_dest.id)
            obj.dest_trip = my_dest
            obj.save()
            trip_form.save()
            return render(request,'first_app/add_plan.html')







def add_plan_link(req):
    # req.session['user_logged_in'] = None
    return redirect('/add_plan')


def logout(req):
    # req.session['user_logged_in'] = None
    return redirect('/welcome')

def home(req):
    return redirect('/welcome')

# add_plan_form = TripPlanner(request.POST)
#     dest_form = DestinationForm()
#     dest = request.POST.get['dest']
#
#     users = User.objects.get(name = request.session['user_logged_in'])
#     dest_user_obj = Destination.objects.filter(place = dest)
#     if dest_form.is_valid():
#         obj = dest_form.save(commit=False)
#         obj.save()
#         obj.user_travelling.add(users)
#         dest_form.save_m2m()
#
#     if add_plan_form.is_valid():
#         obj1 = add_plan_form.save(commit=False)
#         obj1.save()
#         obj1.user_trip.add(users)
#         obj1.dest_trip.add(dest_user_obj)
#         dest_form.save_m2m()
#
#         return redirect("/add_plan_link")
#     context = {
#         "form": TripPlanner()
#     }
