from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# -------------------SIGNUP-----------------------------
def signup(request):
    # Checks if the request is a GET or POST resquest
    if request.method == 'POST':
        # User has info and wants an account now! We check if the password they entered matches in both sections
        if request.POST.get('password1', False) == request.POST.get('password2', False):
            # Here we have a Try except
            try:
                # First we check to if the username has been used before and throw an error if it does
                user = User.objects.get(username = request.POST.get('username', False))
                return render(request,'accounts/signup.html',{'error': 'Username has already been taken.'})
            except User.DoesNotExist:
                # In the case that the username hasnt been used before the create the users account and direct them to the homepage
                user = User.objects.create_user(request.POST.get('username', False), password=request.POST.get('password1'))
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error': 'Passwords must be the same.'})

    else:
        # User wants to enter info
        return render(request,'accounts/signup.html')
# --------------------LOGIN--------------------
def login(request):
    # Checks if the request is a GET or POST resquest
    if request.method == 'POST':
        # In the case that the request is a POST request we need to authenicate the users(username and password)
        user = auth.authenticate(username= request.POST.get('username', False),password= request.POST.get('password', False))
        #In the case that this user exists we want to log them in and direct them to the home page
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error': 'Try again, the Password or Username may be incorrect.'})

    else:
        return render(request,'accounts/login.html')
# --------------------LOGOUT--------------------
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
