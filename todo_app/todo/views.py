from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


from .models import Tasks


# Create your views here.


class TaskList(ListView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskview.html'


#
# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse_lazy('task')

#

#     login = login.objects.all()
#     form= LoginForm()
#     if request.method == 'POST' :
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/task/')
#     context = {'login':login, 'form':form}
#     return render(request,'login.html',context)

#
# def login_fun(request):
#     context = {}
#     s = LoginForm(request.POST)
#     if s.is_valid():
#         s.save()
#         return redirect('/task')
#     context['form'] = s
#     return render(request, "login.html", context)


#def register_fun(request):
    # register = register.objects.all()
    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/task/')
    # context = {'register': register, 'form': form}
    # return render(request, 'register.html', context)

    # context = {}
    # s = RegisterForm(request.POST)
    # if s.is_valid():
    #     s.save()
    #     return redirect('/task')
    # context['form'] = s
    # return render(request, "register.html", context)
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"You created an account!")

        return redirect('login')

    return render(request,'register.html')


class CustomLogin(LoginView):
    template_name='login.html'
    fields ='_all_'
    success_url = reverse_lazy('task')
    redirected_authenticated_user=True

    def get_success_url(self):
        return self.success_url