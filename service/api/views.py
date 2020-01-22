from django.http import HttpResponse,JsonResponse
from .models import UrlsClass,Urls,PrivateResourcesClass,PrivateResources
from service import settings
import os,time
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    data = list(UrlsClass.objects.order_by('-sortid').values())
    data = {
        'data':data
    }
    return JsonResponse(data)

def urls(request):
    urlclass_id = request.POST['class_id']
    data = list(Urls.objects.filter(href_class=urlclass_id).order_by('-sortid').values())
    data = {
        'data':data
    }
    return JsonResponse(data)

def image(request,file):
    image_path = os.path.join(settings.BASE_DIR,'image',file)
    image_type = file.split('.')
    image_type = image_type[len(image_type)-1]
    with open(image_path,'rb') as f:
        image_file = f.read()
    return HttpResponse(image_file,content_type='image/%s'%(image_type))

def userlogin(request):
    user = request.POST['user']
    password = request.POST['password']
    user = authenticate(request,username=user, password=password)
    data = {}
    if user is not None:
        login(request,user)
        data['state'] = 'success'
    else:
        data['state'] = 'err'
    return JsonResponse(data)

def userlogout(request):
    logout(request)
    return JsonResponse({'state':'success'})

def userresign(request):
    email = request.POST['email']
    user = request.POST['user']
    password = request.POST['password']
    data = {}
    try:
        user = User.objects.create_user(email=email, username=user, password=password)
        user.save()
        data['state'] = 'success'
    except:
        data['state'] = 'err'
    return JsonResponse(data)

def updatepassword(request):
    user = request.POST['user']
    email = request.POST['email']
    data = list(User.objects.filter(username=user).values())
    response = {}
    if(len(data)==0):
        response['state'] = 'err'
    else:
        if(data[0]['email']==email):
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    return JsonResponse(response)

def modifypassword(request):
    data = {}
    try:
        user = request.POST['user']
        password = request.POST['password']
        u = User.objects.get(username=user)
        u.set_password(password)
        u.save()
        data['state'] = 'success'
    except:
        data['state'] = 'err'
    return JsonResponse(data)

def privateresourcesclass(request):
    response = {}
    if(request.user.is_authenticated):
        user = request.POST['user']
        user_index = list(User.objects.filter(username=user).values())[0]['id']
        data = list(PrivateResourcesClass.objects.filter(user=user_index).values())
        response['state'] = 'success'
        response['data'] = data
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def privateresources(request):
    response = {}
    if (request.user.is_authenticated):
        class_id = request.POST['id']
        data = list(PrivateResources.objects.filter(href_class=class_id).values())
        response['state'] = 'success'
        response['data'] = data
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def changeshare(request):
    response = {}
    if (request.user.is_authenticated):
        urlsid = request.POST['id']
        share = request.POST['share']
        data = PrivateResources.objects.get(id=urlsid)
        data.share = bool(share)
        data.share_date = time.strftime("%Y-%m-%d", time.localtime())
        data.save()
        response['state'] = 'success'
    else:
        response['state'] = 'err'
    return JsonResponse(response)