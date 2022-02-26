from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from random import randint, randrange
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def index(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        phoneNumber = request.POST["phoneNumber"]
  
        numberGenerated = randint(1, 99999)
        userCodeInitials = firstName[:2].upper() + lastName[:2].upper()
        userCodeNumber = numberGenerated
        uzrCode = str(userCodeInitials) + str(userCodeNumber)
         
        userForm = userRefer(
            firstName=firstName,
            lastName=lastName,
            email=email,
            phoneNumber=phoneNumber,
            userCode=str(userCodeInitials) + str(userCodeNumber),
            userCodeInitials=userCodeInitials,
            userCodeNumber=userCodeNumber,
            
            )
        userForm.save()
        return render(request, 'base.html',{'userCodezz':uzrCode})
    # else:
    #     return render(request, 'base.html')
    return render(request, "base.html")