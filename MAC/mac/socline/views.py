from django.shortcuts import render, HttpResponse, redirect
from .models import Contact, Server, ServerRoom
from django.contrib import messages
# from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# HTML Pages
def home(request):
    # return HttpResponse("This is home")
    return render (request, 'home/home.html')

def about(request):
    # return HttpResponse("This is about")
    return render (request, 'home/about.html')

# def contact(request):
#     messages.warning(request, "Welcome to Contact")
#     if request.method=='POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         content = request.POST['content']
#         if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
#             messages.error(request, "Please fill the form correctly")
#         else:
#             contact = Contact(name=name, email=email, phone=phone, content=content)
#             contact.save()  
#             messages.success(request, "Your messages has been successfully sent")
#         # print(name, email, phone, content)
#     return render (request, 'home/contact.html')

# def search(request):
#     query=request.GET['query']
#     if len(query)>78:
#         allPosts=Post.objects.none()
#     else:
#         allPostsTitle= Post.objects.filter(title__icontains=query)
#         allPostsAuthor= Post.objects.filter(author__icontains=query)
#         allPostsContent =Post.objects.filter(content__icontains=query)
#         allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
#     if allPosts.count()==0:
#         messages.warning(request, "No search results found. Please refine your query.")
#     params={'allPosts': allPosts, 'query': query}
#     return render(request, 'home/search.html', params)

# Authentication APIs 
def serverHome(request):
    allServers= Server.objects.all()
    print(allServers)
    context={'allPosts': allServers}
    return render(request, "server/serverlist.html", context)

def handleSignup(request):
    if request.method=='POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        # Usename should be under 10 characters
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect("home")
        # Username should be alpha numeric
        if pass1!=pass2:
            messages.error(request, "Passwords do not match")
            return redirect("home")
        # Passwords should match
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect("home")
        
        # Create the users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.lastt_name = lname
        myuser.save()
        messages.success(request, "Your iCoder account has been successfully created")
        return redirect("home")

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again!")
            return redirect('home')
        
    return HttpResponse('404 - Not found')
    return HttpResponse('login')

def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
    return HttpResponse('handleLogout')

def messagePost(request, slug): 
    post=Server.objects.filter(slug=slug).first()
    comments= Server.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "server/serverroom.html", context)

def PostMessage(request):
    if request.method == "POST":
        message=request.POST.get('message')
        user=request.user
        sno =request.POST.get('sno')
        post= Server.objects.get(sno=sno)
       
        comment=ServerRooms(message= message, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/server/{post.slug}")