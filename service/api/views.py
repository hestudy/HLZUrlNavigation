from django.http import HttpResponse,JsonResponse
from .models import UrlsClass,Urls,PrivateResourcesClass,PrivateResources,About,WeChat,Comments
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
        user_index = list(User.objects.filter(username=request.user).values())[0]['id']
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
        if(len(list(PrivateResources.objects.filter(share=True,title=data.title).values()))==0):
            data.share = bool(share)
            data.share_date = time.strftime("%Y-%m-%d", time.localtime())
            data.save()
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def ResourcesManageOverView(request):
    response = {}
    if (request.user.is_authenticated):
        user_id = User.objects.get(username=request.user).id
        data = list(PrivateResourcesClass.objects.filter(user=user_id).values())
        response['PrivateResourcesClass'] = data
        data = list(PrivateResources.objects.filter(user=user_id).values())
        response['PrivateResources'] = data
        response['state'] = 'success'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def AddPrivateResourcesClass(request):
    response = {}
    if (request.user.is_authenticated):
        user_id = User.objects.get(username=request.user).id
        add_classname = request.POST['add']
        data = list(PrivateResourcesClass.objects.filter(user=user_id,classname=add_classname).values())
        if(len(data)==0):
            data = PrivateResourcesClass()
            data.classname = add_classname
            data.user = User.objects.get(username=request.user)
            data.save()
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def AddPrivateResources(request):
    response = {}
    if (request.user.is_authenticated):
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        href = request.POST['href']
        href_class = PrivateResourcesClass.objects.get(classname=request.POST['href_class'])
        user = User.objects.get(username=request.user)
        image = request.FILES['image']
        data = len(list(PrivateResources.objects.filter(user=user,href=href).values()))
        if(data==0):
            model = PrivateResources()
            model.title = title
            model.subtitle = subtitle
            model.href = href
            model.href_class = href_class
            model.user = user
            model.image = image
            model.save()
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def UpdatePrivateResourcesClass(request):
    response = {}
    if (request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        classname_id = request.POST['id']
        classname = request.POST['classname']
        data = len(list(PrivateResourcesClass.objects.filter(id=classname_id,user=user)))
        if(data!=0):
            data = len(list(PrivateResourcesClass.objects.filter(classname=classname,user=user).values()))
            if(data==0):
                data = PrivateResourcesClass.objects.get(id=classname_id)
                data.classname = classname
                data.save()
                response['state'] = 'success'
            else:
                response['state'] = 'err'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def geturlsdata(request):
    response = {}
    if (request.user.is_authenticated):
        data = list(PrivateResources.objects.filter(user=request.user).values())
        response['data'] = data
        response['state'] = 'success'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def UpdatePrivateResources(request):
    response = {}
    if (request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        model_id = request.POST['id']
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        href = request.POST['href']
        href_class = request.POST['href_class']
        data = len(list(PrivateResources.objects.filter(user=user,id=model_id).values()))
        if(data==0):
            response['state'] = 'err'
        else:
            data = PrivateResources.objects.get(id=model_id)
            data.title = title
            data.subtitle = subtitle
            data.href = href
            data.href_class = PrivateResourcesClass.objects.get(id=href_class)
            data.save()
            response['state'] = 'success'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def DeletePrivateResourcesClass(request):
    response = {}
    if (request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        class_id = request.POST['id']
        data = len(list(PrivateResourcesClass.objects.filter(user=user,id=class_id).values()))
        if(data!=0):
            data = PrivateResourcesClass.objects.get(id=class_id)
            data.delete()
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def DeletePrivateResources(request):
    response = {}
    if (request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        urls_id = request.POST['id']
        data = len(list(PrivateResources.objects.filter(user=user, id=urls_id).values()))
        if (data != 0):
            data = PrivateResources.objects.get(id=urls_id)
            data.delete()
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def UserShareOrderHot(request):
    data = list(PrivateResources.objects.filter(share=True).order_by('-share_hot').values())
    data = {
        'data':data
    }
    return JsonResponse(data)

def UserShareOrderDate(request):
    data = list(PrivateResources.objects.filter(share=True).order_by('-share_date').values())
    data = {
        'data': data
    }
    return JsonResponse(data)

def AddShareHot(request):
    urls_id = request.POST['id']
    data = PrivateResources.objects.get(id=urls_id)
    data.share_hot+=1
    data.save()
    return JsonResponse({'state':'ok'})

def IsSuperUser(request):
    response = {}
    if (request.user.is_authenticated):
        if(User.objects.get(username=request.user).is_superuser):
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def ReadAbout(request):
    response = {}
    data = list(About.objects.values())[0]
    response['data'] = data
    return JsonResponse(response)

def UpdateAbout(request):
    response = {}
    if (request.user.is_authenticated):
        if (User.objects.get(username=request.user).is_superuser):
            content = request.POST['content']
            content_id = list(About.objects.values())[0]['id']
            data = About.objects.get(id=content_id)
            data.content = content
            data.save()
            response['state'] = 'success'
        else:
            response['state'] = 'err'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def WeChatImage(request):
    data = list(WeChat.objects.values())[0]['image']
    image_path = os.path.join(settings.BASE_DIR,data)
    with open(image_path,'rb') as f:
        data = f.read()
    return HttpResponse(data,content_type='image/jpg')

def CommentsPush(request):
    response = {}
    if (request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        content = request.POST['content']
        data = Comments()
        data.user = user
        data.content = content
        data.save()
        response['state'] = 'success'
    else:
        response['state'] = 'err'
    return JsonResponse(response)

def CommentsData(request):
    data = list(Comments.objects.order_by('-id').values())
    for i in data:
        user = User.objects.get(id=i['user_id']).username
        i['user'] = user
    response = {
        'data':data
    }
    return JsonResponse(response)