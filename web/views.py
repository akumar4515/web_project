# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserProfile, Message, Courses,Topic, contents, Sub_topic
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
#---------------------------------------------------#----------------------------------#-------------------------

#right here i have created a index view , in which the user which is requested 
# get their profile objects and assign it to room variable and use it in our html code 'index.html'
#created a context dict that store the room objects.
#______________________________________________________________________________________________________________#

def index(request): 
    course=Courses.objects.all()
    if request.user.is_authenticated:
       room=UserProfile.objects.get_or_create(user=request.user)      
       return render(request, "index.html", {'room': room , 'course':course})
    else:
       return render(request, "index.html", {'course':course})
    



#content remain

#------------------------------------------------------------#------------------------------------------#--------
#________________________________________________________________________________________________________________#
def topic(request,courses_id):
    course=Courses.objects.get(id=courses_id)
    topic=Topic.objects.all().filter(courses=course)
    topics=topic.all()
    return render(request,'course.html',{'course': course, 'topic': topic, 'topics':topics})


def subtopic(request, courses_id, topic_id):
    course=Courses.objects.get(id=courses_id)
    topics=Topic.objects.get(id=topic_id)

    sub_topics=Sub_topic.objects.all().filter(topic=topics)
    sub_topicss=sub_topics.all()
    
   

    return render(request, 'sub_topic.html', {'course': course, 'topics': topics, 'sub_topics': sub_topics, 'sub_topicss':sub_topicss})

def content(request, courses_id, topic_id, sub_topic_id):
    course = Courses.objects.get(id=courses_id)
    topic = Topic.objects.get(id=topic_id)
    sub_topic = Sub_topic.objects.get(id=sub_topic_id)
    content = contents.objects.get(sub_topic=sub_topic)


    return render(request, 'content.html', {'course': course, 'topic': topic, 'sub_topic': sub_topic, 'content': content})

#--------------------------------------------------------------#---------------------------------#-------------------------#

# right here i have  created a user sign-up views , that check method==POST 
# assign the input in some var like username,email and password
# check is our user info we getting is not in our user model 
# take input from user and check conditions and if satisfied save it in user model and create user
# and redirect the user to the login page if user created successfully , otherwise return back to the register page

#______________________________________________________________________________________________________________________________#

def register(request):
    if request.method == 'POST':
      
       username = request.POST['username']
       email= request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']
       if password==password2:
           if User.objects.filter(email=email).exists():
               messages.info(request, 'email already exist' )
               return redirect('register')
           elif User.objects.filter(username=username):
               messages.info(request, 'username already exist')
               return redirect('register')
           else:
               user=User.objects.create_user(username=username,email=email , password=password)
               user.save();
               return redirect('login')
       else:
           messages.info(request, 'password is not same')
           return redirect('register')
    else: 
        return render(request, 'register.html')
    
#--------------------------------------------------#------------------------------------------#------------------------#-----#
#_____________________________________________________________________________________________________________________________#
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login')
    
    else:    
      return render(request, 'login.html')
   

   
   

@login_required    
def logout(request):
    auth.logout(request) 
    return redirect('/')   







@login_required
def edit_profile(request):
    user = request.user
    profile = UserProfile.objects.get_or_create(user=user)[0]
    if request.method == 'POST':
        profile.fname = request.POST['fname']
        profile.lname = request.POST['lname']
        profile.bio = request.POST['bio']
        profile.birth_date = request.POST['birth_date']
        profile.country = request.POST['country']
        profile.occupation = request.POST['occupation']
        profile.lnkDn =request.POST['lnkDn']
        new_username = request.POST['username']
        new_email = request.POST["email"]
        user.username = new_username
        user.email = new_email
        if request.FILES.get('profile_image'):
            profile.profile_image = request.FILES['profile_image']
        user.save()
        profile.save()
        return redirect('/')
    else:
        context = {'user': user, 'profile': profile}
        return render(request, 'profile.html', context)






@login_required
def userProfile(request):
    user=request.user
    if UserProfile.objects.filter(user=user):
     room=UserProfile.objects.get(user=user)
    else:
        room=UserProfile.objects.create(user=user) 
    return render(request, "userprofile.html", {"room": room})




@login_required
def contact(request):
    user=request.user
    room=UserProfile.objects.get(user=user)
    message=Message.objects.create(user=user)
    if request.method=="POST":
        message.content= request.POST["content"] 
        message.save()
        return redirect('/')
    else:
        return render(request, 'contact.html', {'room':room })



def adminX(request):
    user = request.user
    if request.user.is_authenticated:
      room=UserProfile.objects.get(user=user)
      context={
        'room':room
    }
      return render(request, 'admin.html', context)
    else:
     return render(request, 'admin.html')

@login_required
@staff_member_required
def contX(request):
   return render(request, 'contX.html')
 
@login_required
@staff_member_required
def admin(request):
    user=request.user
    room=UserProfile.objects.get(user=user)
    msg=Message.objects.all()
    if request.user.is_authenticated: 
   

     return render(request, 'adminMessage.html', {'room':room ,'msg':msg})   
 

