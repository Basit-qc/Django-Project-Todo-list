# Create your views here.
""" Views for todo list """
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.views.generic.simple import redirect_to
from todosproject.todos.models import Todo_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
#login user by maintaining his session name and id
def user_login(request):
    """ login user by maintaining his session name and id """
    if 'id' in request.session:
        return HttpResponseRedirect("/home.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password )
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['name'] = username
                request.session['id'] = user.id
                return redirect_to(request,"/home.html")
            else:
                return HttpResponse("disabled account")
                # Return a 'disabled account' error message
        else:
            return HttpResponse("Invalid login")

    elif request.method == 'GET':
        return render(request,'todos/login.html')

#The function which is bind to the home page
def index(request):
    """ The function which is bind to the home page """
    if not 'id' in request.session:
        return HttpResponseRedirect("/login")
    todolist = Todo_task.objects.all()
    totaltodos = 0
    if todolist:
        for value in todolist:
            if value.user.id == request.session['id']:
                totaltodos = totaltodos+1
    return render_to_response( 'todos/home.html', 
                               context_instance=RequestContext( request, {
                                                        'todo_list': todolist,
                                                        'total':totaltodos,
                                    }))
    
#logout the current user    
def logout_view(request):
    """ logout the current user """ 
    logout( request )
    return HttpResponseRedirect('/login')

#add todo task to database
def addtodo_form(request):
    """ add todo task to database """
    addedsummary = request.POST['summary']
    addeddescription = request.POST['description']
    addedurl = request.POST['url']
    if(addedsummary == ""):
        return HttpResponse('add field')
    uid = int(request.session['id'])
    addeduser = User.objects.get(id=uid)
    add = Todo_task(summary = addedsummary,
                  description = addeddescription,
                  url_address = addedurl,
                  user = addeduser)
    add.save()
    return HttpResponseRedirect('/home.html/')

#email todo task to himself
def email_todo(request):
    """ email todo task to himself """
    task_summary = request.GET['summary']
    task_description = request.GET['description']
    task_url = request.GET['url']
    to_email = User.objects.get(username=request.session['name']).email
    send_mail( task_summary, 
               task_description+' \n'+"URL: "+task_url, 
               'afnannazir.qc@gmail.com',
               [to_email], 
               fail_silently=False)
    return HttpResponse("successful")

#delete todo task from database
def delete_todo(request):
    """ delete todo task from database """
    task_summary = request.GET['summary']
    task_description = request.GET['description']
    task_url = request.GET['url']
    uid = request.session['id']
    query = Todo_task.objects.filter(summary = task_summary,
                                   description = task_description,
                                   url_address = task_url,
                                   user = uid)
    query.delete()
    return HttpResponseRedirect('/home.html')
    
    

        
