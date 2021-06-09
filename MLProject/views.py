from django.shortcuts import render, HttpResponse, redirect
from ML_model import *
from MLProject.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.
def index(request):
    return render(request, 'index.html')

def prednormal(request):
    if request.method == "POST":
        district = request.POST.get('district')
        variety = str(request.POST.get('variety'))
        year = date.today().year
        no = int(request.POST.get('month'))
        state = request.POST.get('state')
        if state=='Telangana':
            return render(request, 'prednormal.html', context={'variable': round(telangana(district,variety,year,no),3)})
        if state=='Andhra Pradesh':
            return render(request, 'prednormal.html', context={'variable': round(andhrapradesh(district,variety,year,no),3)})    
        if state=='Gujarat':
            return render(request, 'prednormal.html', context={'variable': round(gujarat(district,variety,year,no),3)})    
        if state=='Maharashtra':
            return render(request, 'prednormal.html', context={'variable': round(maharashtra(district,variety,year,no),3)})    
        if state=='Rajasthan':
            return render(request, 'prednormal.html', context={'variable': round(rajasthan(district,variety,year,no),3)})    
        if state=='Tamil Nadu':
            return render(request, 'prednormal.html', context={'variable': round(tamilnadu(district,variety,year,no),3)})    
        # if state doesn't matches
        return render(request, 'prednormal.html', context={'variable': "Error"})
    return render(request, 'prednormal.html')    

def predict(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        if request.method == "POST":
            district = request.POST.get('district')
            variety = str(request.POST.get('variety'))
            year = int(request.POST.get('year'))
            no = int(request.POST.get('month'))
            state = request.POST.get('state')
            if state=='Telangana':
                return render(request, 'predict.html', context={'variable': round(telangana(district,variety,year,no),3)})
            if state=='Andhra Pradesh':
                return render(request, 'predict.html', context={'variable': round(andhrapradesh(district,variety,year,no),3)})    
            if state=='Gujarat':
                return render(request, 'predict.html', context={'variable': round(gujarat(district,variety,year,no),3)})    
            if state=='Maharashtra':
                return render(request, 'predict.html', context={'variable': round(maharashtra(district,variety,year,no),3)})    
            if state=='Rajasthan':
                return render(request, 'predict.html', context={'variable': round(rajasthan(district,variety,year,no),3)})    
            if state=='Tamil Nadu':
                return render(request, 'predict.html', context={'variable': round(tamilnadu(district,variety,year,no),3)})    
            # if state doesn't matches
            return render(request, 'predict.html', context={'variable': "Error"})
        return render(request, 'predict.html')

def pred12month(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        state = request.user.state 
        if request.method == "POST": 
            district = request.POST.get('district')
            variety = str(request.POST.get('variety'))
            year = int(request.POST.get('year'))
            maxi=0
            result = [district]
            if request.user.state=='Telangana':
                for i in range(1,13):
                    inst = round(telangana(district,variety,year,i),3)
                    if maxi<inst:
                        maxi=inst
                    result.append(inst)
            if request.user.state=='Andhra Pradesh':
                for i in range(1,13):
                    inst = round(andhrapradesh(district,variety,year,i),3)
                    if maxi<inst:
                        maxi=inst
                    result.append(inst)
            if request.user.state=='Gujarat':
                for i in range(1,13):
                    inst = round(gujarat(district,variety,year,i),3)
                    if maxi<inst:
                        maxi=inst
                    result.append(inst)
            if request.user.state=='Maharashtra':
                for i in range(1,13):
                    inst = round(maharashtra(district,variety,year,i),3)
                    if maxi<inst:
                        maxi=inst
                    result.append(inst)
            if request.user.state=='Rajasthan':
                for i in range(1,13):
                    inst = round(rajasthan(district,variety,year,i),3)
                    if maxi<inst:
                        maxi=inst
                    result.append(inst)
            if request.user.state=='Tamil Nadu':
                for i in range(1,13):
                    inst = round(tamilnadu(district,variety,year,i),3)
                    if maxi<inst:
                        maxi=inst
                    result.append(inst)                                           
            return render(request, '12_month_prediction.html', context={'gdata': result,
                                                                        'max':maxi,
                                                                        'userstate': state})
                                                                        
        return render(request, '12_month_prediction.html', context={'userstate': state})

def forgraphs(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        state = request.user.state 
        if request.method == "POST":
            
            variety = str(request.POST.get('variety'))
            year = int(request.POST.get('year'))
            result = []
            district = returnDistrict(state)
            if state=='Telangana':
                for dist in district:
                    new = [dist]
                    for i in range(1,13):    
                        new.append(telangana(dist,variety,year,i))
                    result.append(new)
            if state=='Andhra Pradesh':
                for dist in district:
                    new = [dist]
                    for i in range(1,13):    
                        new.append(andhrapradesh(dist,variety,year,i))
                    result.append(new)
            if state=='Gujarat':
                for dist in district:
                    new = [dist]
                    for i in range(1,13):    
                        new.append(gujarat(dist,variety,year,i))
                    result.append(new)
            if state=='Maharashtra':
                for dist in district:
                    new = [dist]
                    for i in range(1,13):    
                        new.append(maharashtra(dist,variety,year,i))
                    result.append(new)
            if state=='Rajasthan':
                for dist in district:
                    new = [dist]
                    for i in range(1,13):    
                        new.append(rajasthan(dist,variety,year,i))
                    result.append(new)
            if state=='Tamil Nadu':
                for dist in district:
                    new = [dist]
                    for i in range(1,13):    
                        new.append(tamilnadu(dist,variety,year,i))
                    result.append(new)
                
            return render(request, 'districtprediction.html', context={'gdata': result,
                                                                'userstate': state})
                                                                       
        return render(request, 'districtprediction.html', context={'userstate': state})
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        state = request.POST.get('state')
        user = User.objects.create_user(username=username,email=email,password=password,state=state)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/predict")
        else:
            # No backend authenticated the credentials
            return redirect("/login")
    return render(request,'register.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/predict")
        else:
            # No backend authenticated the credentials
            return redirect("/login")
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

def test(request):
    return render(request,"gettingdata.html")

def  faq(request):
    return render(request,"faq.html")

def about(request):
    return render(request,"about.html")

def  questionpred(request):
    return render(request,"questionpred.html")
