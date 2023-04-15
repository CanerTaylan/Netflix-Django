from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profil

# Create your views here.


def profilePage(request):
    # * giriş yapan kullanıcıya göre filtreledik
    profils = Profil.objects.filter(user=request.user)

    if request.method == "POST":
        button = request.POST.get("submit")
        if button == "profil-create":
            if len(profils) < 4:        # * profils sayısı 4'e kadar olacak şekilde sınırladık
                name = request.POST.get("name")
                image = request.FILES.get("image")

                profil = Profil(title=name, image=image, user=request.user)
                profil.save()

                return redirect('profilePage')
        elif button == "profil-password":
            password = request.POST.get("password")
            profilid = request.POST.get("profilid")
            profil = Profil.objects.get(id=profilid)
            if profil.password == password:         #* dataki şifre modal formdan gelen şifre ile aynı mı
                return redirect("/netflix/" + profilid + "/")
            else:
                messages.warning(request,"Hatalı şifre !!")



    context = {
        "profils": profils,
    }
    return render(request, 'user/profile.html', context)


def accountPage(request):
    context = {
    }
    return render(request, 'user/hesap.html', context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Hoşgeldiniz")
            return redirect('profilePage')
        else:
            messages.warning(request, "Kullanıcı adı veya şifre yanlış !!")
            return redirect('loginUser')     

    context = {
    }
    return render(request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerUser(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():

                    user = User.objects.create_user(
                        username=username, password=password1, first_name=fname, email=email)
                    user.save()
                    messages.success(
                        request, "Kaydınız başarıyla oluşturuldu.")
                    return redirect("loginUser")
                else:
                    messages.warning(
                        request, "Bu mail adresi sistemimizde kayıtlı!!!")
                    hata = "email"
                    # return redirect('registerUser')
            else:
                messages.warning(
                    request, "Bu kullanıcı adı zaten kullanılıyor!!!")
                hata = "username"
                # return redirect('registerUser')
        else:
            messages.warning(request, "Şifreler aynı değil!!!")
            hata = "password"
            # return redirect('registerUser')
        context = {}            #* context ilk olarak boş olup içini update ile güncelliyoruz.
        if hata == "email":
            context.update({
                "fname": fname,
                "username": username,
                "pasword1": password1,
                "hata": hata,
            })
        elif hata == "username":
            context.update({
                "fname": fname,
                "email": email,
                "pasword1": password1,
                "hata": hata,
            })
        elif hata == "password":
            context.update({
                "fname": fname,
                "email": email,
                "username": username,
                "hata": hata,
            })

        return render(request, 'user/register.html', context)

    context = {}
    return render(request, 'user/register.html', context)

def profilDelete(request, id):
    profil = Profil.objects.get(id=id)
    profil.delete()
    return redirect("profilePage")
