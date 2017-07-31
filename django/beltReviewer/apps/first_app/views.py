from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect# the index function is called when root is visited
from .models import User, Books
from .forms import UserCreateForm, LoginForm, AddBooksAndReviews

def index(request):
	return render(request, 'firstapp/index.html')

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
        "all_books" : Books.objects.all()
    }

    return render(req,'first_app/books_home.html', context)

def BookAndReview(request):

    form  = AddBooksAndReviews()
    context = {
        "form" : form
    }
    return render(request,'first_app/add_book_reviews.html', context)


def addBookAndReview(request):
    addBk_Rw  = AddBooksAndReviews(request.POST)

    users = User.objects.get(name = request.session['user_logged_in'])
    print("1. printing name")
    print(users.name)
    print("done")



    if addBk_Rw.is_valid():


        print("100")
        obj = addBk_Rw.save(commit=False)
        obj.save()
        obj.user_of_book.add(users)
        addBk_Rw.save_m2m()
        print("200")


        return redirect("bk_review")
    context = {
        "form" : AddBooksAndReviews()
    }
    return render(request,'first_app/add_book_reviews.html', context)




# def this_book(request, title):
#     context = {
#         "title" : title
#     }
#     return render(request, 'firstapp/dynamic_ninja.html', context)
#



def logout(req):
    # req.session['user_logged_in'] = None
    return redirect('/welcome')

def home(req):
    return redirect('/welcome')

