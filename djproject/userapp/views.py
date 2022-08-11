from django.shortcuts import render
from django.shortcuts import redirect
#import mysql.connector as mysql
from django.db import connection
#from userapp.models import newtable
from django.contrib import messages
from .models import newtable

def index(request):
	return render(request,'index.html')
def register(request):
	return render(request,'register.html')	
def delete(request):
	data = newtable.objects.all().values()
	return render(request,'home.html',{'data':data})	
def edit(req):
	return render(req,'edit.html')			
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
               return redirect('/studentinfo')                       
     messages.error(req,"invalid user") 
     return redirect('/index')    
#     conn.commit()
     conn.close()       
     return redirect('/index')    
def deletetask(req):
	try:
		userid=req.POST.get("ID")
		conn = connection.cursor()
		data = newtable.objects.get(id=userid)
		data.delete()
		messages.success(req,"user deleted")
		return redirect('/studentinfo')
	except:
		messages.success(req,"invalid userid")
		return redirect('/delete')
def studentinfo(request):
    stud =newtable.objects.all()
    return render(request,'admin.html',{'stu': stud})  
    
    
def update(req):
	try:
		userid=req.POST.get("ID")
		Name1=req.POST.get("Name")
		Email1=req.POST.get("Email")
		pasd1=req.POST.get("pasd")
		conn = connection.cursor()
		data = newtable.objects.get(id=userid)
		data.Name=Name1
		data.Email=Email1
		data.pasd=pasd1
		data.save()
		messages.success(req,"update successfully")
		return redirect('/studentinfo')   
	except:
		messages.success(req,"invalid userid")
		return redirect('/edit')     

