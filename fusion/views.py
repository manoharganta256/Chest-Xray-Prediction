from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from fusion.forms import ImageForm,UserProfileForm
from fusion.predict import predict_image
from fusion.profile import image
from fusion.models import UserProfile,Image
# Create your views here.

@login_required
def start(request):
    return HttpResponseRedirect('/fusion/home/')
def index(request):
    #context_dict = {'boldmessage': 'Manohar'}
    return render(request,'fusion/index.html')
@login_required
def home(request):
    uploaded = False
    prediction = ''
    probability = ''
    if request.method == 'POST':
        form = ImageForm(data=request.POST)
        if form.is_valid() and 'fileUpload' in request.FILES:
            profile = form.save(commit=False)
            profile.user = request.user
            print(profile.user)
            profile.chest_xray = request.FILES['fileUpload']
            uploaded = True
            profile.save()
            prediction,prob = predict_image('./media/'+profile.chest_xray.name)
            profile.prediction = prediction
            probability = str(prob)[:6]
            profile.probability = probability
            profile.save()
    return render(request,'fusion/home.html',{'uploaded':uploaded,'prediction':prediction,
    'probability':probability})

def result(request):
    pass

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/fusion/')

@login_required
def profile(request):
    try:
        profile_form = UserProfile.objects.get(user=request.user)
        profile_form.limit = len(Image.objects.filter(user=request.user))
        profile_form.save()
    except:
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.user = request.user
            profile_form.profile_picture = image()
            profile_form.limit = len(Image.objects.filter(user=request.user))
            profile_form.save()
        else:
            print('Profile form Invaild')
            print(form.errors)
    image_history = Image.objects.filter(user=request.user)
    #print(image_history)
    return render(request,'fusion/profile.html',{'profile_form':profile_form,'history':image_history})

@login_required
def delete(request):
    Image.objects.filter(user=request.user).delete()
    return HttpResponseRedirect('/fusion/profile/')