from django.shortcuts import render, redirect
from . models import Product, Metrics, Goals,Sales,Finance,Operations, Goals2, Goals1,Room, Message
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test

def user_is_authenticated(user):
    return user.is_authenticated





class CustomLoginView(LoginView):
    template_name = 'login.html'

'''
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            # Passwords do not match, handle the error
            return render(request, 'partials/register.html', {'error_message': 'Passwords do not match'})

        # Check for existing user with the same username or email
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            # User already exists, handle the error
            return render(request, 'partials/register.html', {'error_message': 'User already exists'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Redirect to a success page or login page
        return redirect('login')
    else:
        return render(request, 'partials/register.html')


'''
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")


    context = {'registerform':form}
    return render(request, 'partials/register.html', context=context)



def my_login(request):
    form = LoginForm()
    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            if username:
                x = username[0]

            else:
                x=''    

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)

                
                if user.is_authenticated:
                    if x == 'f':
                        return redirect('finance')
                    elif x == 's':
                        return redirect('sales')
                    elif x == 'o':
                        return redirect('op')
                    elif x == 'c':
                        return redirect('home')
                    else:
                        return redirect('login')


    context = {'loginform':form}

    return render(request, 'partials/login.html', context=context)


def user_logout(request):

    logout(request)

    return redirect("chartapp/index.html")

def login_invalid_redirect(request):
    return render(request,"partials/login.html",{'login_invalid':'Username or password is incorrect'}) 


@login_required(login_url="login")
def home(request):

    metric1 = Metrics.objects.get(id = 1)
    metric2 = Metrics.objects.get(id = 2)
    metric3 = Metrics.objects.get(id = 3)
    metric4 = Metrics.objects.get(id = 4)
    
    goals = Goals.objects.all()
    goals1 = Goals1.objects.all()
    goals2 = Goals2.objects.all()
    mile = Goals.objects.get(id=14)

    sale = Sales.objects.all()

    fin = Finance.objects.all()
    

    return render(request, 'partials/home.html',{'metric1': metric1, 'metric2': metric2, 'metric3': metric3, 'metric4': metric4,
     'goals': goals, 'goals1': goals1, 'goals2': goals2, 'mile':mile,'fin':fin,'sale':sale})




@login_required(login_url="login")
def finance(request):
    fin = Finance.objects.all()
    

    return render(request, 'partials/finance.html',{'fin':fin})


@login_required(login_url="login")
def sales(request):
    sale = Sales.objects.all()
    


    return render(request, 'partials/sales.html',{'sale':sale})

@login_required(login_url="login")
def chat(request):
    registered_users = User.objects.all()
    
    
    return render(request, 'partials/chat.html', {'registered_users': registered_users})


@login_required(login_url="login")
def op(request):

    inv1 = Operations.objects.get(id=1)
    inv2 = Operations.objects.get(id=2)
    inv3 = Operations.objects.get(id=3)
    inv4 = Operations.objects.get(id=4)
    inv = Operations.objects.all()

    return render(request, 'partials/op.html', {'inv1':inv1, 'inv2':inv2, 'inv3':inv3, 'inv4':inv4, 'inv':inv})



def index(request):

    return render(request, 'chartapp/index.html')

       
                

@login_required(login_url="login")
def enterchat(request):
    return render(request, 'partials/enterchat.html')




def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'partials/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})





      





