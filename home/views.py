from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name':'Bhutu Talukder', 'age': 23},
        {'name':'Bhut Talukder','age':23},
        {'name':'Abhijeet Gupta','age':16},
        {'name':'Sandeep Sharma','age':20},
        {'name':'Vickey Kaushal','age':17}

        
    ]
    vegetables=[
        {'pumpkin','tomatoe','potatoe','carrot'}
    ]


    return render(request, "index.html",context={'peoples':peoples,' vegetables': vegetables})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
    
