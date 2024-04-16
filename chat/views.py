from django.contrib.auth.decorators import login_required
from chat.models import Thread
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import Thread, ChatMessage
from .forms import FileUploadForm
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)



class ChatView(ListView):
    template_name = 'chat/chat.html'
    context_object_name = 'threads'

    def get_queryset(self):
        return Thread.objects.by_user(user=self.request.user)

class FileUploadView(CreateView):
    template_name = 'chat/upload_file.html'
    form_class = FileUploadForm

    def form_valid(self, form):
        thread_id = self.kwargs.get('thread_id')
        thread = Thread.objects.get(id=thread_id)
        form.instance.thread = thread
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        thread_id = self.kwargs.get('thread_id')
        return reverse('chat:chat', kwargs={'thread_id': thread_id})
    



def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file
            uploaded_file = form.save(commit=False)
            # Associate the file with the current user or any other logic you require
            uploaded_file.user = request.user
            uploaded_file.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('upload_file')  # Redirect to the same page after upload
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

