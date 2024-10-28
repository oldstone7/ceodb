
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db.models import Q, Max
from django.db.models import OuterRef, Subquery
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_list')  # Redirect to user list after registration
    else:
        form = UserRegisterForm()
    return render(request, 'chat/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_list(request):
    user = request.user
    show_finance = False
    show_sales = False
    show_operations = False

    if user.id == 3:
        show_finance = show_sales = show_operations = True
    elif user.username.startswith('f'):
        show_finance = True
    elif user.username.startswith('s'):
        show_sales = True
    elif user.username.startswith('o'):
        show_operations = True

    
    users = User.objects.exclude(id=request.user.id)
    print("User list")
    
    last_message_subquery = Message.objects.filter(
        Q(sender=OuterRef('pk'), receiver=request.user) |
        Q(sender=request.user, receiver=OuterRef('pk'))
    ).order_by('-timestamp')

    # Retrieve the last message content, file, and timestamp
    last_message_content = Subquery(last_message_subquery.values('content')[:1])
    last_message_file = Subquery(last_message_subquery.values('file')[:1])
    last_message_timestamp = Subquery(last_message_subquery.values('timestamp')[:1])

    users = users.annotate(
        last_message=last_message_content,
        last_message_file=last_message_file,
        last_message_timestamp=last_message_timestamp
    )

    return render(request, 'chat/user_list.html', {'users': users, 'show_finance': show_finance,'show_sales': show_sales,'show_operations': show_operations})

@login_required(login_url='login')
def chat(request, user_id):
    user = request.user
    show_finance = False
    show_sales = False
    show_operations = False

    if user.id == 3:
        show_finance = show_sales = show_operations = True
    elif user.username.startswith('f'):
        show_finance = True
    elif user.username.startswith('s'):
        show_sales = True
    elif user.username.startswith('o'):
        show_operations = True

    users = User.objects.exclude(id=request.user.id)
    other_user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')

    # Handle message and file upload
    if request.method == 'POST':
        content = request.POST.get('message')
        file = request.FILES.get('file')

        # Create a new message instance
        message = Message(sender=request.user, receiver=other_user, content=content)
        
        if file:
            message.file = file  # Save the file in the Message model
        else:
            message.file = None  # Ensure file is set to None if no file is uploaded

        message.save()  # Save the message object

        return redirect('chat', user_id=user_id)

    # Subquery to get the last message for each user relative to the logged-in user
    last_message_subquery = Message.objects.filter(
        Q(sender=OuterRef('pk'), receiver=request.user) |
        Q(sender=request.user, receiver=OuterRef('pk'))
    ).order_by('-timestamp')

    last_message_content = Subquery(last_message_subquery.values('content')[:1])
    last_message_file = Subquery(last_message_subquery.values('file')[:1])
    last_message_timestamp = Subquery(last_message_subquery.values('timestamp')[:1])

    users = users.annotate(
        last_message=last_message_content,
        last_message_file=last_message_file,
        last_message_timestamp=last_message_timestamp
    )

    return render(request, 'chat/chat.html', {
        'other_user': other_user,
        'messages': messages,
        'users': users,
        'show_finance': show_finance,'show_sales': show_sales,'show_operations': show_operations
    })
