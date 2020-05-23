from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def home(request):
    context={'home' : 'active'}
    return render(request,'core/home.html',context)

def contact(request):
    context = {'contact' : 'active' }
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            Name = request.POST['Name']
            emailin = request.POST['emailin']
           

            messages.success(request,('there was error please redirect'))
            #return redirect('join') 
            return render (request,'core/contact.html',{'Name':Name,
            'emailin':emailin,
            })
        messages.success(request,('your from has been sucessfully added'))    
        return redirect('contact')

    else:
        return render(request,'core/contact.html',{})
    return render(request,'core/contact.html',{})    

def sys(request):
    all_members = Member.objects.all
    return render(request,'core/sys.html',{'all':all_members})    