
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import modelformset_factory
from .models import Fashion
from . import forms
from .forms import AboutForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.generic import (View,TemplateView,ListView,
                                DetailView,CreateView,UpdateView)
# Create your views here.
def registers(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('anoapp:registers')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('anoapp:registers')
            else:


                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()

                print("Success")
                return redirect('/')
        else:
            messages.info(request,'Password not matching')
            return redirect('anoapp:registers')
        return redirect('/')
    else:
        return render(request,'anoapp/registration.html')


def login_page(request):

    if request.method == 'POST':


        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credetials')
            return redirect('anoapp:login')
    else:
        return render(request,'anoapp/user_login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,'anoapp/home.html')


def about(request):

    form = forms.AboutForm()
    if request.method == 'POST':
        form = forms.AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    else:
        form = AboutForm
    return render(request, 'anoapp/about.html',{'form':form})



class LatestTemplateView(TemplateView):
    template_name = 'anoapp/latest_article.html'


class FashionListView(ListView):
    model = Fashion
    context_object_name = 'fashions'


class FashionDetailView(DetailView):
    model = Fashion
    template_name = 'anoapp/fashion_detail.html'
    context_object_name = 'fashions_detail'


    #def get_object(self):
    #    id_ = self.kwargs.get('pk')
    #    return get_object_or_404(Fashion, pk=id_)


class FashionCreateView(CreateView):
    model = Fashion
    ImageFormset = modelformset_factory
    fields = ('brand_name','product','year')


    def imgform_set():
        ImageFormset = modelformset_factory(Image, fields=('image',), extra=4)
        if request.method == 'POST':

            formset = ImageFormset(request.POST or None, request.Files or None)
            if formset.is_valid():
                for f in formset:
                    try:
                        photo = Image(post=post, image=f.cleaned_data['image'])
                        photo.save()
                    except Exception as e:
                        break
        else:
            formset = ImageFormset(queryset=Image.objects.none())
        return render(request, 'anoapp/fashion_form.html', {'formset':formset})






class FashionUpdateView(UpdateView):
    model = Fashion
    fields = '__all__'
