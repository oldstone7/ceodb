from django.shortcuts import render, redirect
from . models import Product, Metrics, Goals,Sales,Finance,Operations, Goals2, Goals1,Room, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm







def user_is_authenticated(user):
    return user.is_authenticated





class CustomLoginView(LoginView):
    template_name = 'login.html'


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")


    context = {'registerform':form}
    return render(request, 'partials/register.html', context=context)



def my_login(request):
    error_message = None
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
                error_message = "Invalid username or password"

        else:
            error_message = "Invalid username or password"            


    context = {'loginform': form,'error_message': error_message}

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

    operations = Operations.objects.all()
    

    return render(request, 'partials/home.html',{'metric1': metric1, 'metric2': metric2, 'metric3': metric3, 'metric4': metric4,
     'goals': goals, 'goals1': goals1, 'goals2': goals2, 'mile':mile,'fin':fin,'sale':sale, 'operations':operations})



@login_required(login_url="login")
def calendar(request):
    

    return render(request, 'partials/calendar.html',context={})


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

from .models import Operations
from .forms import OperationsForm


@login_required(login_url="login")
def op(request):

    context = {}
    form = OperationsForm()
    operations = Operations.objects.all()
    context['operations'] = operations
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = OperationsForm(request.POST)
            else:
                operations = Operations.objects.get(id=pk)
                form = OperationsForm(request.POST, instance=operations)
            form.save()
            form = OperationsForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            operations = Operations.objects.get(id=pk)
            operations.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            operations = Operations.objects.get(id=pk)
            form = OperationsForm(instance=operations)
    context['form'] = form
    return render(request, 'partials/op.html', context)




from .forms import OperationsForm 

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

