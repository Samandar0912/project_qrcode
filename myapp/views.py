import base64
from io import BytesIO
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import random
import qrcode
from qrcode.image.pure import PyPNGImage
from .models import Sertificate
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def sertifikat_list(request):
    sertifikatlar = Sertificate.objects.all()
    return render(request, 'main.html', {'sertifikat': sertifikatlar})


# Create your views here.
def index(request):
    return render(request,'index.html')


def main(request):
    sertifikat = Sertificate.objects.all()
    return render(request,'main.html', {'sertifikat':sertifikat} )


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')  
        serya = request.POST.get('seriya')

        if name and serya:
            sertifikat = Sertificate(name=name, serya=serya)
            sertifikat.save()
            return redirect('main')
        else:
            return render(request, 'add.html', {'error_message': 'Iltimos, barcha maydonlarni to\'ldiring!'})

    else:
        return render(request, 'add.html')


def delate(request,id):
    sertifikat = Sertificate.objects.get(id=id)
    sertifikat.delete()
    return redirect("main")    







def my_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Tizimga kirishda xatolik bor")
            return redirect('login')
    else:
        return render(request, 'login.html')


def my_logout(request):
    logout(request)
    return redirect('login')






















# def register(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         seriya = request.POST.get('seriya')
        
#         # Foydalanuvchi ma'lumotlarini biriktirish
#         data = f"JizPi tomonidan berilgan:, ismi: {name}, Pasport seriyasi: {seriya}"
        
#         img = qrcode.make( 
#                     data,
#                     version = 4,
#                     error_correction = qrcode.constants.ERROR_CORRECT_L,
#                     box_size = 4,
#                     border = 4,
#                     image_factory=PyPNGImage
#                 )
        
#         stream = BytesIO()
#         img.save(stream,kind="PNG")
#         bytes_data = stream.getvalue()
#         qr_image_base64 = base64.b64encode(bytes_data).decode('utf-8')
        
#         context = {
#             "qr_image_base64": qr_image_base64
#         }
#         return render(request, 'register.html', context)
    
#     if request.method == "GET":
#         return render(request, 'register.html')
    
    



