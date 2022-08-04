from django.shortcuts import render
from django.shortcuts import redirect
#import mysql.connector as mysql
from django.db import connection
#from userapp.models import newtable
from django.contrib import messages

def index(request):
	return render(request,'index.html')
def register(request):
	return render(request,'register.html')
def home(request):
	return render(request,'home.html')		
def insert(req):
    Name=req.POST.get("Name")
    Email=req.POST.get("Email")
    pasd=req.POST.get("pasd")    
    conn = connection.cursor()
    query = "insert into userapp_newtable values({0},'{1}','{2}','{3}')".format(0,Name,Email,pasd)
    conn.execute(query)
 #   conn.commit()
    conn.close()   
    messages.success(req,"You are register sucessfully login Now") 
    return redirect('/index')	
 
def logintask(req):
     Email=req.POST.get("email")
     pasd=req.POST.get("pass")    
     conn = connection.cursor()
     conn.execute("select* from userapp_newtable")    
     while True:
          row=conn.fetchone()
          if row is None:
          	break;
          elif row[2]==Email and row[3]==pasd:
               return redirect('/home')                       
     messages.error(req,"invalid user") 
     return redirect('/index')    
#     conn.commit()
     conn.close()       
     return redirect('/index')    
     

